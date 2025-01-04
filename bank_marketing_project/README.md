# Cleaning Bank Marketing Campaign Data
Reference: [Data Camp Learning Project](https://projects.datacamp.com/projects/1613)
## Project Overview
This project demonstrates a data engineering workflow for processing and transforming marketing data for analysis. The dataset used is derived from a bank marketing campaign and includes client information, campaign outcomes, and economic indicators. The goal is to clean, transform, and subset the data into meaningful components for downstream analysis. The resulting datasets are saved in CSV format.

## Key Features

- Data Cleaning: Reformatting date fields, replacing invalid values, and standardizing text data.

- Feature Transformation: Converting categorical variables to numeric formats and handling missing values.

- Data Subsetting: Segmenting data into logical groups for ease of use and analysis.

## Technologies Used

- **Python**: Core programming language for data manipulation.

- **Pandas**: For data manipulation and transformation.

- **NumPy**: For handling missing values and mathematical operations.


## Project Outputs

- `client.csv`: Contains client demographics and financial status.

- `campaign.csv`: Contains campaign-related interactions and outcomes.

- `economics.csv`: Contains economic indicators relevant to the clients.

## How to Run Locally
1. Clone or download the project files.
2. Recreate virtual environment with: 
```
python3 -m venv venv
source venv/bin/activate    # For macOS/Linux
.\venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```
3. Run the script:
`python data_processing.py`
4. Verify the generated CSV files in the project directory.


## Learning Outcomes

- Demonstrated ability to clean and preprocess data.

- Implemented feature engineering techniques.


