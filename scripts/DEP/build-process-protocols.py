#!/usr/bin/env python3
"""
Extract protocol sections from process markdown files and build PDFs.

This script finds all process-*.md files in docs/processes/*/ directories,
extracts the content after '# Protocol', removes MyST directives, creates
corresponding protocol-*.md files with proper YAML frontmatter, and then
builds PDFs using MyST.
"""

import re
import subprocess
from pathlib import Path
from typing import List, Tuple


def extract_process_name(filename: str) -> str | None:
    """Extract process name from filename like 'process-name_of_process.md'."""
    match = re.match(r'^process-(.+)\.md$', filename)
    return match.group(1) if match else None


def process_name_to_title(process_name: str) -> str:
    """Convert process name to title case (e.g., 'make-small-molecule-mix' -> 'Make Small Molecule Mix')."""
    # Replace hyphens and underscores with spaces
    words = re.split(r'[-_]', process_name)
    # Capitalize first letter of each word
    return ' '.join(word.capitalize() for word in words)


def extract_protocol_content(input_path: Path) -> List[str]:
    """Extract content after '# Protocol' heading, removing MyST directives except tables and figures."""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    protocol_lines = []
    found_protocol = False
    skip_depth = 0  # Track nesting depth of directives to skip
    keep_depth = 0  # Track nesting depth of directives to keep (table/figure)
    
    for line in lines:
        # Start collecting after we find '# Protocol'
        if line.strip() == '# Protocol':
            found_protocol = True
            protocol_lines.append(line)
            continue
        
        if not found_protocol:
            continue
        
        stripped = line.strip()
        
        # Check for opening directive
        if match := re.match(r'^(:::+)\{([^}]+)\}', stripped):
            fence_length = len(match.group(1))
            directive_type = match.group(2).split()[0]  # Get first word (e.g., 'table' from 'table :label: ...')
            
            # Keep table and figure directives
            if directive_type in ['table', 'figure']:
                keep_depth = fence_length
                protocol_lines.append(line)
            else:
                # Skip all other directives
                skip_depth = fence_length
            continue
        
        # Check for closing directive
        if match := re.match(r'^(:::+)$', stripped):
            fence_length = len(match.group(1))
            
            # If we're in a keep block and this closes it
            if keep_depth > 0 and fence_length == keep_depth:
                protocol_lines.append(line)
                keep_depth = 0
                continue
            
            # If we're in a skip block and this closes it
            if skip_depth > 0 and fence_length == skip_depth:
                skip_depth = 0
                continue
            
            # Otherwise keep the line (might be closing a nested block)
            if keep_depth > 0:
                protocol_lines.append(line)
            continue
        
        # Skip lines inside directives we want to skip
        if skip_depth > 0:
            continue
        
        # Inside a table or figure block - keep everything including :label: and :align:
        if keep_depth > 0:
            protocol_lines.append(line)
            continue
        
        # Skip standalone MyST directive lines like :label: or :align: (only outside kept blocks)
        if re.match(r'^:[a-z_]+:', stripped):
            continue
        
        protocol_lines.append(line)
    
    return protocol_lines


def create_protocol_file(input_path: Path) -> Path | None:
    """Process a single process-*.md file and create corresponding protocol-*.md file.
    
    Returns:
        Path to created protocol file, or None if skipped.
    """
    process_name = extract_process_name(input_path.name)
    
    if not process_name:
        print(f"⚠ Skipping '{input_path}': not in format 'process-*.md'")
        return None
    
    # Convert process name to lowercase for consistent filenames
    process_name_lower = process_name.lower()
    
    # Create output path in same directory
    output_path = input_path.parent / f"protocol-{process_name_lower}.md"
    pdf_path = output_path.with_suffix('.pdf')
    
    # Clean up any old protocol files with different casing in the same directory
    # This handles cases where old files had mixed case (e.g., protocol-Make_Thing.md)
    for old_file in input_path.parent.glob('protocol-*.md'):
        # If it's a protocol file but not our target lowercase name, remove it
        if old_file.name.lower() == output_path.name.lower() and old_file != output_path:
            print(f"  Removing old file: {old_file.name}")
            old_file.unlink()
    
    # Also clean up old PDFs with different casing
    for old_pdf in input_path.parent.glob('protocol-*.pdf'):
        if old_pdf.name.lower() == pdf_path.name.lower() and old_pdf != pdf_path:
            print(f"  Removing old PDF: {old_pdf.name}")
            old_pdf.unlink()
    
    # Check if file exists
    file_exists = output_path.exists()
    
    # Generate title (keep original case for title)
    title = process_name_to_title(process_name)
    
    # Create YAML frontmatter (use lowercase in output filename)
    frontmatter = f"""---
title: {title}
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: protocol-{process_name_lower}.pdf
---

"""
    
    # Extract protocol content
    protocol_content = extract_protocol_content(input_path)
    
    # Write output file (this will overwrite if exists)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.writelines(protocol_content)
    
    if file_exists:
        print(f"✓ Overwrote: {output_path}")
    else:
        print(f"✓ Created: {output_path}")
    
    return output_path
    
    return output_path
    return output_path


def build_pdf(protocol_path: Path) -> Tuple[bool, str]:
    """Build PDF from protocol markdown file using myst.
    
    Args:
        protocol_path: Path to the protocol-*.md file
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Determine expected PDF path
        pdf_path = protocol_path.with_suffix('.pdf')
        
        # Remove old PDF if it exists to ensure we're building fresh
        if pdf_path.exists():
            pdf_path.unlink()
        
        # Change to the directory containing the file
        protocol_dir = protocol_path.parent
        
        # Run myst build command
        result = subprocess.run(
            ['myst', 'build', protocol_path.name, '--pdf'],
            cwd=protocol_dir,
            capture_output=True,
            text=True,
            timeout=120  # 120 second timeout (increased from 60)
        )
        
        # Check if PDF was actually created
        if pdf_path.exists():
            return True, f"✓ Built PDF: {pdf_path.name}"
        else:
            # PDF wasn't created, show the error output
            error_msg = result.stderr.strip() if result.stderr else result.stdout.strip()
            if not error_msg:
                error_msg = "PDF file was not created (no error message)"
            return False, f"✗ Failed to build PDF for {protocol_path.name}:\n  {error_msg}"
            
    except subprocess.TimeoutExpired:
        return False, f"✗ Timeout building PDF for {protocol_path.name}"
    except FileNotFoundError:
        return False, "✗ Error: 'myst' command not found. Is MyST installed?"
    except Exception as e:
        return False, f"✗ Error building PDF for {protocol_path.name}: {str(e)}"


def main():
    """Find and process all process-*.md files in docs/processes/*/."""
    print("Searching for process-*.md files in docs/processes/*/")
    print("=" * 50)
    
    # Find all process-*.md files
    docs_path = Path('docs/processes')
    
    if not docs_path.exists():
        print(f"Error: Directory '{docs_path}' not found")
        print("Make sure to run this script from the project root directory")
        return 1
    
    process_files = list(docs_path.glob('*/process-*.md'))
    
    if not process_files:
        print("No process-*.md files found in docs/processes/*/")
        return 0
    
    # Process each file
    created_protocols = []
    for process_file in sorted(process_files):
        protocol_path = create_protocol_file(process_file)
        if protocol_path:
            created_protocols.append(protocol_path)
    
    print("=" * 50)
    print(f"Created {len(created_protocols)} protocol file(s)")
    
    # Build PDFs if any protocols were created
    if created_protocols:
        print("\nBuilding PDFs...")
        print("=" * 50)
        
        build_success = 0
        build_failed = 0
        
        for protocol_path in created_protocols:
            success, message = build_pdf(protocol_path)
            print(message)
            if success:
                build_success += 1
            else:
                build_failed += 1
        
        print("=" * 50)
        print(f"PDFs built: {build_success} succeeded, {build_failed} failed")
    
    return 0


if __name__ == '__main__':
    exit(main())