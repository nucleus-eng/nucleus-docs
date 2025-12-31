bash#!/usr/bin/env bash

# build_pages.sh - Initialize Jupyter Book and modify myst.yml

set -e  # Exit on error

# Delete myst.yml if it exists
if [ -f "myst.yml" ]; then
    echo "Removing existing myst.yml..."
    rm myst.yml
fi

echo "Initializing Jupyter Book..."
jupyter book init --write-toc

echo "Modifying myst.yml..."

# Check if myst.yml exists
if [ ! -f "myst.yml" ]; then
    echo "Error: myst.yml not found!"
    exit 1
fi

# Add extends, uncomment and set title
awk '
/^version:/ {print; print "extends:"; print "  - ./site.yml"; next}
/^[[:space:]]*# title:/ {print "  title: Nucleus Distribution"; next}
{print} 
' myst.yml > myst.yml.tmp && mv myst.yml.tmp myst.yml

echo "Writing Table of Contents..."
jupyter book init --write-toc

echo "✓ Jupyter Book initialization complete!"
echo "✓ myst.yml modified with extends and title"
echo "✓ myst.yml table of contents added"
