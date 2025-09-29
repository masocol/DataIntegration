# Scripts

This directory contains utility scripts and tools for data science workflows.

## Available Scripts

### Setup and Environment
- `setup_environment.py` - Script to setup virtual environment and install dependencies
- `check_requirements.py` - Verify all required packages are installed

### Data Processing Utilities
- `data_cleaner.py` - Common data cleaning functions
- `data_validator.py` - Data quality validation utilities
- `file_converter.py` - Convert between different data formats (CSV, JSON, Excel)

### Project Management
- `create_project.py` - Create new project structure from templates
- `notebook_cleaner.py` - Clean Jupyter notebook outputs and metadata

### Visualization Helpers
- `plot_utils.py` - Common plotting functions and styles
- `report_generator.py` - Generate HTML reports from notebooks

## Usage

Each script includes detailed documentation and can be run from the command line:

```bash
python scripts/script_name.py --help
```

## Development Guidelines

When adding new scripts:
1. Include proper documentation and help text
2. Add error handling and input validation
3. Follow PEP 8 style guidelines
4. Include example usage in the docstring