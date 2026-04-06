
#!/bin/bash
# Set up the development environment for building Nucleus docs locally

conda env create -f environment.yml --force
echo ""
echo "Done! To get started:"
echo "  conda activate nucleus-docs"
echo "  jupyter book start"