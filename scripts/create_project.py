#!/usr/bin/env python3
"""
Create Project Script

This script helps create new data science projects with proper structure
and templates from the project-templates directory.

Usage:
    python scripts/create_project.py --name "My Project" --type eda --subject data-integration
    python scripts/create_project.py --help
"""

import argparse
import os
import shutil
from pathlib import Path
from datetime import datetime


def create_project_structure(project_name, subject, project_type, base_path="."):
    """Create a new project structure with templates."""
    
    # Sanitize project name for directory name
    safe_name = project_name.lower().replace(" ", "-").replace("_", "-")
    
    # Define paths
    base_dir = Path(base_path)
    subject_dir = base_dir / subject
    project_dir = subject_dir / "projects" / safe_name
    
    # Check if subject directory exists
    if not subject_dir.exists():
        print(f"Error: Subject directory '{subject}' does not exist.")
        print("Available subjects:")
        for item in base_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['docs', 'scripts', 'project-templates', 'sample-data']:
                print(f"  - {item.name}")
        return False
    
    # Check if project already exists
    if project_dir.exists():
        print(f"Error: Project '{safe_name}' already exists in {subject}/projects/")
        return False
    
    # Create project directory
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories
    (project_dir / "notebooks").mkdir(exist_ok=True)
    (project_dir / "data").mkdir(exist_ok=True)
    (project_dir / "scripts").mkdir(exist_ok=True)
    (project_dir / "outputs").mkdir(exist_ok=True)
    (project_dir / "docs").mkdir(exist_ok=True)
    
    # Copy appropriate template
    template_mapping = {
        'eda': 'eda_template.ipynb',
        'ml': 'ml_project_template.ipynb',
        'stats': 'statistical_analysis_template.ipynb',
        'integration': 'data_integration_template.ipynb'
    }
    
    template_file = template_mapping.get(project_type, 'eda_template.ipynb')
    template_path = base_dir / "project-templates" / template_file
    
    if template_path.exists():
        notebook_name = f"{safe_name}.ipynb"
        shutil.copy2(template_path, project_dir / "notebooks" / notebook_name)
        print(f"Copied template: {template_file} -> notebooks/{notebook_name}")
    else:
        print(f"Warning: Template '{template_file}' not found. Creating basic notebook.")
        # Create a basic notebook structure
        create_basic_notebook(project_dir / "notebooks" / f"{safe_name}.ipynb", project_name)
    
    # Create project README
    create_project_readme(project_dir, project_name, subject, project_type)
    
    # Create .gitignore for project-specific ignores
    create_project_gitignore(project_dir)
    
    print(f"\n✅ Project '{project_name}' created successfully!")
    print(f"📁 Location: {project_dir}")
    print(f"🚀 Start with: jupyter notebook {project_dir}/notebooks/{safe_name}.ipynb")
    
    return True


def create_basic_notebook(notebook_path, project_name):
    """Create a basic Jupyter notebook if template is not available."""
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {project_name}\n\n",
                    "**Author:** [Your Name]\n",
                    f"**Created:** {datetime.now().strftime('%Y-%m-%d')}\n\n",
                    "## Objective\n",
                    "Describe the main objectives of this project.\n\n",
                    "## Data\n",
                    "Describe the dataset(s) used in this project.\n\n",
                    "## Methodology\n",
                    "Outline your approach and methodology."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Import required libraries\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "\n",
                    "# Set display options\n",
                    "pd.set_option('display.max_columns', None)\n",
                    "plt.style.use('seaborn-v0_8')"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    import json
    with open(notebook_path, 'w') as f:
        json.dump(notebook_content, f, indent=2)


def create_project_readme(project_dir, project_name, subject, project_type):
    """Create a README file for the project."""
    readme_content = f"""# {project_name}

**Subject:** {subject.replace('-', ' ').title()}
**Type:** {project_type.upper()}
**Created:** {datetime.now().strftime('%Y-%m-%d')}

## Overview
Brief description of the project objectives and scope.

## Structure
```
{project_dir.name}/
├── notebooks/          # Jupyter notebooks
├── data/              # Project data files  
├── scripts/           # Python scripts and utilities
├── outputs/           # Results, plots, and reports
├── docs/              # Additional documentation
└── README.md          # This file
```

## Data
- **Source:** [Describe data source]
- **Format:** [Data format and structure]
- **Size:** [Dataset size and dimensions]

## Dependencies
See the main repository's `requirements.txt` for core dependencies.

Additional project-specific requirements:
```
# Add any additional packages here
```

## Usage
1. Navigate to the project directory
2. Start Jupyter: `jupyter notebook`
3. Open `notebooks/{project_dir.name}.ipynb`
4. Follow the notebook instructions

## Results
Summary of key findings and results.

## Next Steps
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## References
- [Reference 1]
- [Reference 2]
"""
    
    with open(project_dir / "README.md", 'w') as f:
        f.write(readme_content)


def create_project_gitignore(project_dir):
    """Create a project-specific .gitignore file."""
    gitignore_content = """# Project-specific ignores
data/*.csv
data/*.xlsx
data/*.json
!data/sample_*
!data/README.md

outputs/*.png
outputs/*.jpg  
outputs/*.pdf
!outputs/README.md

# Temporary files
*.tmp
*.temp
.cache/

# Model files
*.pkl
*.joblib
*.h5
"""
    
    with open(project_dir / ".gitignore", 'w') as f:
        f.write(gitignore_content)


def main():
    parser = argparse.ArgumentParser(
        description="Create a new data science project with proper structure and templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --name "Sales Analysis" --type eda --subject data-integration
  %(prog)s --name "Customer Segmentation" --type ml --subject machine-learning
  %(prog)s --name "A/B Test Results" --type stats --subject statistics
        """
    )
    
    parser.add_argument(
        '--name', '-n',
        required=True,
        help='Name of the project (spaces allowed)'
    )
    
    parser.add_argument(
        '--subject', '-s',
        required=True,
        help='Subject directory (e.g., data-integration, machine-learning, statistics)'
    )
    
    parser.add_argument(
        '--type', '-t',
        choices=['eda', 'ml', 'stats', 'integration'],
        default='eda',
        help='Project type - determines template used (default: eda)'
    )
    
    parser.add_argument(
        '--path', '-p',
        default='.',
        help='Base path for the repository (default: current directory)'
    )
    
    args = parser.parse_args()
    
    success = create_project_structure(
        project_name=args.name,
        subject=args.subject,
        project_type=args.type,
        base_path=args.path
    )
    
    if not success:
        exit(1)


if __name__ == '__main__':
    main()