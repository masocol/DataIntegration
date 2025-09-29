# Sample Data

This directory contains sample datasets for learning, testing, and demonstration purposes.

## Datasets Included

### Educational Datasets
- `iris.csv` - Classic iris flower dataset for classification
- `titanic.csv` - Titanic passenger survival dataset  
- `boston_housing.csv` - Boston housing prices for regression
- `wine_quality.csv` - Wine quality ratings dataset

### Practice Datasets
- `sales_data.csv` - Sample sales transaction data
- `customer_data.csv` - Customer demographics and behavior
- `web_analytics.csv` - Website traffic and user behavior
- `financial_data.csv` - Stock prices and financial indicators

## Data Sources and Attribution

All datasets are either:
1. Public domain datasets commonly used in education
2. Synthetic data generated for educational purposes
3. Properly attributed datasets with appropriate licenses

## Usage Guidelines

### Academic Use
- These datasets are provided for educational purposes only
- Proper citation is required when using in academic work
- Check individual dataset licenses for specific requirements

### File Formats
- **CSV files:** Most common format for structured data
- **JSON files:** For semi-structured and nested data
- **Excel files:** For datasets requiring multiple sheets

### Loading Data

```python
import pandas as pd

# Load CSV data
df = pd.read_csv('sample-data/dataset_name.csv')

# Load JSON data  
df = pd.read_json('sample-data/dataset_name.json')

# Load Excel data
df = pd.read_excel('sample-data/dataset_name.xlsx')
```

## Data Ethics and Privacy

- All sample data is either public domain or anonymized
- No personal identifying information (PII) is included
- Follow data ethics guidelines when working with any dataset
- Always understand the context and source of your data

## Contributing Sample Data

When adding new datasets:
1. Ensure data is appropriate for educational use
2. Include proper attribution and licensing information
3. Add dataset description to this README
4. Keep file sizes reasonable (< 50MB preferred)
5. Include data dictionary or column descriptions

## Need More Data?

For larger or specialized datasets, consider:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [AWS Open Data](https://aws.amazon.com/opendata/)
- [Government Open Data Portals](https://www.data.gov/)

Remember to always check licensing and usage rights for any external datasets.