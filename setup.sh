#!/bin/bash
# Set up the development environment for building Nucleus docs locally

if [[ "$CONDA_DEFAULT_ENV" == "nucleus-docs" ]]; then
  echo "Please run 'conda deactivate' first, then re-run this script."
  exit 1
fi

conda env remove -n nucleus-docs 2>/dev/null
conda env create -f environment.yml
echo ""
echo "Done! To get started:"
echo "  conda activate nucleus-docs"
echo "  jupyter book start"