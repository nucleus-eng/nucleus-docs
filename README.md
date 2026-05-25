# Nucleus Documentation

Documentation for the [Nucleus Distribution](https://docs.nucleus.engineering), built with [Jupyter Book](https://jupyterbook.org/).

## Building locally

### Setup

```bash
git clone https://github.com/nucleus-eng/nucleus-docs.git
cd nucleus-docs
./setup.sh
conda activate nucleus-docs
jupyter book start
```

This starts a local dev server with live reload — any changes you make to `.md` or `.ipynb` files will automatically refresh in the browser.

## DNA parts library

Sequence files (`.gb`) for the plasmids and constructs referenced in these protocols are maintained in a companion repository: [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA). When a protocol page calls for a specific construct (e.g., `pOpen-PURET7-3`), the corresponding GenBank file lives there. The repository is organized by part type:

```
DNA/
├── PURE/
│   ├── cloning/      # pOpen entry vectors for all PURE system proteins
│   └── expression/   # pET28a expression vectors for PURE system proteins
├── assembly/         # MoClo backbone (pOpen-pOpenv3-MCL0)
├── RBS/              # Ribosome binding site and UTR parts
├── promoters/        # Level-matched T7 promoter library (PURET7-1 through -10)
├── reporters/        # Fluorescent protein and chromoprotein reporters
├── terminators/      # T7 terminator variants
└── detectors/        # LacI/TetR circuits and quorum sensing components
```

## License

See [LICENSE.md](LICENSE.md).