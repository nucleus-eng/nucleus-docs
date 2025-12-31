import anthropic
import json
from pathlib import Path
from datetime import datetime

client = anthropic.Anthropic()

def load_reviewed_status():
    """Load which files have been reviewed."""
    if Path("scripts/reviewed_status.json").exists():
        with open("scripts/reviewed_status.json", "r") as f:
            return json.load(f)
    return {}

def save_reviewed_status(status):
    """Save reviewed status."""
    with open("scripts/reviewed_status.json", "w") as f:
        json.dump(status, f, indent=2)

def mark_as_reviewed(filepath):
    """Mark a file as reviewed."""
    status = load_reviewed_status()
    status[filepath] = {
        "reviewed": True,
        "timestamp": str(datetime.now())
    }
    save_reviewed_status(status)

# Read the list of files to review
with open("scripts/files_to_review.txt", "r") as f:
    files_to_check = [line.strip() for line in f if line.strip()]

# Read the style guide once (reuse for all files)
with open("scripts/style_guide.md", "r") as f:
    style_rules = f.read()

# Load reviewed status
reviewed_status = load_reviewed_status()

# Review each file
for doc_path in files_to_check:
    # Skip if already reviewed
    if reviewed_status.get(doc_path, {}).get("reviewed"):
        print(f"\nSKIPPED (already reviewed): {doc_path}")
        continue
    
    print(f"\n{'='*60}")
    print(f"Reviewing: {doc_path}")
    print('='*60)
    
    try:
        # Read the document
        with open(doc_path, "r") as f:
            doc_content = f.read()
        
        # Create the message
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""Review this document for typos and style issues.

STYLE RULES (follow these):
{style_rules}

DOCUMENT TO REVIEW:
{doc_content}

Please list:
1. Any typos found
2. Any style violations with the rule that was violated
3. Suggestions for fixes"""
                }
            ]
        )
        
        print(message.content[0].text)
        
        # Mark as reviewed after successful review
        mark_as_reviewed(doc_path)
    
    except FileNotFoundError:
        print(f"Error: File not found - {doc_path}")
    except Exception as e:
        print(f"Error reviewing {doc_path}: {e}")

print("\n" + "="*60)
print("Review complete")
print("="*60)

# Show summary
reviewed_count = sum(1 for status in reviewed_status.values() if status.get("reviewed"))
print(f"\nTotal files reviewed: {reviewed_count}/{len(files_to_check)}")