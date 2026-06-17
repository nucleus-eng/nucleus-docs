#!/bin/bash
# Set up the development environment for building Nucleus docs locally

if [[ "$CONDA_DEFAULT_ENV" == "nucleus-docs" ]]; then
  echo "Please run 'conda deactivate' first, then re-run this script."
  exit 1
fi

# Install Vale if not already present
if ! command -v vale &> /dev/null; then
  if command -v brew &> /dev/null; then
    brew install vale
  else
    echo "WARNING: vale not found and brew is not available."
    echo "  Install vale manually: https://vale.sh/docs/vale-cli/installation/"
    echo "  The pre-commit vale hook will fail until vale is on your PATH."
  fi
fi

# Install mystmd at the pinned version used in CI
if command -v npm &> /dev/null; then
  npm install -g mystmd@1.9.1
else
  echo "WARNING: npm not found. Install Node.js then run: npm install -g mystmd@1.9.1"
fi

# Install lychee if not already present
if ! command -v lychee &> /dev/null; then
  if command -v brew &> /dev/null; then
    brew install lychee
  else
    echo "WARNING: lychee not found and brew is not available."
    echo "  Install lychee manually: https://github.com/lycheeverse/lychee#installation"
    echo "  The check-links script will fail until lychee is on your PATH."
  fi
fi

# Install codespell if not already present
if ! command -v codespell &> /dev/null; then
  brew install codespell
fi

conda env remove -n nucleus-docs 2>/dev/null
conda env create -f environment.yml

echo ""
echo "Installing pre-commit hooks..."
conda run -n nucleus-docs pre-commit install

echo ""
echo "Done! To get started:"
echo "  conda activate nucleus-docs"
echo "  jupyter book start"
