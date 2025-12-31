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

def get_issues(doc_content: str, style_rules: str) -> str:
    """Get list of issues from Claude."""
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

Please list each issue on a separate line in this format:
[TYPE] Line X: Description of issue"""
            }
        ]
    )
    return message.content[0].text

def get_fix_with_context(doc_content: str, issue: str) -> dict:
    """Get Claude's suggested fix with original and replacement text."""
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"""Given this document and issue, suggest a specific fix.

DOCUMENT:
{doc_content}

ISSUE:
{issue}

Respond in this exact format:
ORIGINAL:
[the exact text from the document that needs fixing]

FIXED:
[the corrected text]"""
            }
        ]
    )
    
    text = message.content[0].text
    
    # Parse the response
    try:
        original_part = text.split("ORIGINAL:")[1].split("FIXED:")[0].strip()
        fixed_part = text.split("FIXED:")[1].strip()
        return {"original": original_part, "fixed": fixed_part}
    except:
        return None

def apply_fix(doc_content: str, fix_dict: dict) -> str:
    """Apply a fix to the document."""
    if not fix_dict:
        return doc_content
    
    original = fix_dict["original"]
    fixed = fix_dict["fixed"]
    
    if original in doc_content:
        return doc_content.replace(original, fixed, 1)
    else:
        print(f"Could not find exact match. Skipping.")
        return doc_content

def parse_issues(issues_text: str) -> list[str]:
    """Extract just the [TYPE] lines from the review."""
    issues = [line.strip() for line in issues_text.split("\n") 
              if line.strip().startswith("[")]
    return issues

def interactive_review(doc_path: str, style_rules: str):
    """Interactively review and fix a document."""
    
    print(f"\n{'='*60}")
    print(f"Reviewing: {doc_path}")
    print('='*60)
    
    try:
        with open(doc_path, "r") as f:
            doc_content = f.read()
        
        # Get full review for overview
        print("\nAnalyzing document...")
        full_review = get_issues(doc_content, style_rules)
        
        print("\n" + full_review)  # Show full review
        
        # Parse into individual issues
        issues = parse_issues(full_review)
        
        print(f"\n{'─'*60}")
        print(f"Found {len(issues)} issue(s)")
        
        # Ask user whether to enter interactive mode or skip
        while True:
            choice = input("\n[i]nteractive mode / [s]kip this document: ").lower().strip()
            
            if choice == "i":
                break
            elif choice == "s":
                print("Skipping this document.")
                return doc_content  # Return unmodified content
            else:
                print("Invalid choice. Try again.")
        
        print(f"\nStarting interactive review of {len(issues)} issue(s)")
        input("Press Enter to begin...")
        
        # Process each issue
        modified_content = doc_content
        for i, issue in enumerate(issues, 1):
            print(f"\n{'─'*60}")
            print(f"Issue {i}/{len(issues)}: {issue}")
            
            # Get suggested fix
            fix_dict = get_fix_with_context(modified_content, issue)
            
            if fix_dict:
                print(f"\nOriginal:\n{fix_dict['original'][:200]}")
                print(f"\nSuggested fix:\n{fix_dict['fixed'][:200]}")
            else:
                print("Could not parse fix suggestion.")
                continue
            
            # User choice
            while True:
                choice = input("\n[y]es / [n]o / [e]dit manually / [s]kip all: ").lower().strip()
                
                if choice == "y":
                    if fix_dict:
                        modified_content = apply_fix(modified_content, fix_dict)
                        print("✓ Fix applied.")
                    break
                
                elif choice == "n":
                    print("✗ Skipped.")
                    break
                
                elif choice == "e":
                    print(f"\nOpening {doc_path} in editor...")
                    import subprocess
                    subprocess.call(["nano", doc_path])
                    # Reload the file
                    with open(doc_path, "r") as f:
                        modified_content = f.read()
                    print("File reloaded.")
                    break
                
                elif choice == "s":
                    print("Skipping remaining issues.")
                    return modified_content
                
                else:
                    print("Invalid choice. Try again.")
        
        return modified_content
    
    except FileNotFoundError:
        print(f"Error: File not found - {doc_path}")
        return None

# Main
with open("scripts/files_to_review.txt", "r") as f:
    files_to_check = [line.strip() for line in f if line.strip()]

with open("scripts/style_guide.md", "r") as f:
    style_rules = f.read()

reviewed_status = load_reviewed_status()

for doc_path in files_to_check:
    if reviewed_status.get(doc_path, {}).get("reviewed"):
        print(f"\nSKIPPED (already reviewed): {doc_path}")
        continue
    
    modified_content = interactive_review(doc_path, style_rules)
    
    if modified_content:
        # Ask if user wants to save
        save_choice = input(f"\nSave changes to {doc_path}? [y/n]: ").lower().strip()
        if save_choice == "y":
            with open(doc_path, "w") as f:
                f.write(modified_content)
            print("File saved.")
            mark_as_reviewed(doc_path)
        else:
            print("Changes discarded.")

print("\n" + "="*60)
print("Review session complete")
print("="*60)