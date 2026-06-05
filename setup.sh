#!/bin/bash
# Set up the development environment for building Nucleus docs locally

if [[ "$CONDA_DEFAULT_ENV" == "nucleus-docs" ]]; then
  echo "Please run 'conda deactivate' first, then re-run this script."
  exit 1
fi

# Install Vale if not already present
if ! command -v vale &> /dev/null; then
  brew install vale
fi

# Install lychee if not already present
if ! command -v lychee &> /dev/null; then
  brew install lychee
fi

# Install codespell if not already present
if ! command -v codespell &> /dev/null; then
  brew install codespell
fi

conda env remove -n nucleus-docs 2>/dev/null
conda env create -f environment.yml
echo ""
echo "Done! To get started:"
echo "  conda activate nucleus-docs"
echo "  jupyter book start"