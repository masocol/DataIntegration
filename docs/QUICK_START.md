# Quick Start Guide

Get up and running with your Data Science repository in minutes!

## 🚀 Initial Setup

### 1. Clone and Setup Environment

```bash
# Clone the repository
git clone https://github.com/masocol/DataIntegration.git
cd DataIntegration

# Create and activate virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Start Jupyter

```bash
# Launch Jupyter Notebook
jupyter notebook

# Or launch Jupyter Lab (if preferred)
jupyter lab
```

## 📝 Creating Your First Project

### Using the Project Creation Script

```bash
# Create a new project
python scripts/create_project.py --name "My First Analysis" --subject data-integration --type eda

# Navigate to your project
cd data-integration/projects/my-first-analysis

# Start working on the notebook
jupyter notebook notebooks/my-first-analysis.ipynb
```

### Manual Project Creation

1. Navigate to the appropriate subject directory
2. Create a new folder in the `projects/` subdirectory
3. Copy a template from `project-templates/`
4. Rename and customize for your project

## 📁 Repository Navigation

### Main Subject Areas
- `data-integration/` - ETL, data cleaning, web scraping
- `machine-learning/` - ML algorithms and implementations  
- `statistics/` - Statistical analysis and testing
- `data-visualization/` - Charts, plots, and dashboards
- `databases/` - SQL, database design, and connectivity
- `programming-fundamentals/` - Python basics and data structures

### Support Directories
- `project-templates/` - Ready-to-use notebook templates
- `sample-data/` - Practice datasets
- `scripts/` - Utility scripts and automation
- `docs/` - Documentation and guides

## 🎯 First Steps Checklist

- [ ] Set up virtual environment and install dependencies
- [ ] Launch Jupyter and explore the repository structure
- [ ] Review the main README.md for comprehensive overview
- [ ] Browse subject-specific README files
- [ ] Create your first project using the creation script
- [ ] Explore the EDA template notebook
- [ ] Review documentation in the `docs/` directory

## 💡 Quick Tips

### Working with Notebooks
- Always clear outputs before committing: `Cell → All Output → Clear`
- Use meaningful markdown sections to document your work
- Include data source information and methodology

### Project Organization
- Keep each project in its own directory
- Use descriptive names for notebooks and files
- Maintain README files for each project

### Version Control Best Practices
- Commit frequently with descriptive messages
- Use `.gitignore` to exclude data files and checkpoints
- Create branches for experimental work

## 🆘 Common Issues

### Jupyter Not Starting
```bash
# Reinstall Jupyter
pip install --upgrade jupyter

# Or try with specific port
jupyter notebook --port=8889
```

### Missing Packages
```bash
# Install individual packages
pip install package-name

# Or update requirements.txt and reinstall
pip install -r requirements.txt
```

### Git Issues
```bash
# Check git status
git status

# View current branch
git branch

# Create new branch for experimental work
git checkout -b feature/new-analysis
```

## 📚 Next Steps

1. **Read the Documentation**: Explore files in the `docs/` directory
2. **Try Templates**: Use different project templates for various analysis types
3. **Link Additional Repositories**: Review `docs/LINKING_REPOSITORIES.md`
4. **Customize**: Adapt the structure to your specific needs
5. **Backup**: Set up regular backups of your work

## 🤝 Getting Help

- Check the [FAQ](FAQ.md) for common questions
- Review existing documentation in the `docs/` directory
- Create issues for bugs or feature requests
- Follow academic integrity guidelines for your institution

---

**Ready to start your Data Science journey? Happy coding! 🚀📊**