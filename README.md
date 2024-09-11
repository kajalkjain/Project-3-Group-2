# Project-3-Group-2

## Healthcare

**A Short Project Proposal**

This project is aimed at analyzing healthcare data, cleaning the dataset, and creating a data visualization dashboard using Python. We utilized several libraries and tools for database management, data cleaning, and interactive visualization. The project demonstrates end-to-end data processing, including database queries and visual representation of results.

![image](https://github.com/user-attachments/assets/37a95756-a8c3-410f-b9b3-9311cfa85882)


## Project Title 
**Data Visualisation Track**

## Project Objective

To predict medical test results (Normal, Abnormal, Inconclusive) using synthetic data. The objective of the project is to improve understanding of predictive modelling in healthcare through data manipulation, feature engineering, and model training. Additionally, it will explore trends in patient demographics, cost analysis, and common conditions. By bridging data insights with practical healthcare applications, this project will provide valuable information for healthcare providers, policymakers, and patients, leading to better decision-making, optimised costs, and improved patient outcomes.

**Scope and Research Questions**

- What is the distribution of medical conditions among different age groups?

  Visualization: Bar chart or pie chart.(Jess)

- How do billing amounts vary across different medical conditions?

  Visualization: Box plot or bar chart.(Napat)

- What are the proportions of different admission types (Emergency, Elective, Urgent)?

  Visualization: Pie chart or bar chart.(Jess)

- How do test results (Normal, Abnormal, Inconclusive) vary by medical condition?

  Visualization: Heatmap or bar chart.(Napat)

- What is the average billing amount for different insurance providers?

  Visualization: Bar chart.(Napat)

- How does the length of hospital stay vary by medical condition?

  Visualization: Box plot or bar chart.(Kajal)

- What trends can be observed in test results over time?

  Visualization: Line plot.(Jess)

- How do different blood types correlate with medical conditions?

  Visualization: Heatmap or stacked bar chart.(Kajal)

- What is the distribution of medication types across different medical conditions?

  Visualization: Bar chart or pie chart.(Sima)

- How does the cost of treatment vary with different admission types?

  Visualization: Box plot or bar chart.(Sima)

- What is the distribution of test results across different age groups?

  Visualization: Stacked bar chart or heatmap.(Sima)

- How do patient demographics (age, gender) influence the types of test results?

  Visualization: Heatmap or grouped bar chart. (Kajal)

    
## Data Source

We sourced our data from kaggle. Link: https://www.kaggle.com/datasets/prasad22/healthcare-dataset 

## Data Ethics

We acknowledge the importance of healthcare data privacy and security and emphasise that this dataset is entirely synthetic. It does not contain any real patient information or violate any privacy regulations (This data has been generated using Python's Faker library to mimic real healthcare records, enabling safe learning and experimentation in healthcare analytics.)

## Visualisation Types

Histograms, Bar charts, Pie charts to visualise the proportion of different admission types (Emergency, Elective, Urgent).
Heatmaps to explore correlations between features like age, billing amount, and test results.
Box plots to compare billing amounts across different medical conditions.
Regression plots to analyse the relationship between variables such as age and billing amount, or between medical conditions and test results.

**Tools and Technologies**

1. **Python**
-Core programming language used for data cleaning, manipulation, and visualization. 
2. **Pandas**
-Used for data manipulation and reading CSV files. It was also instrumental in cleaning the data and preparing it for visualization.
3. **Jupyter Notebook**
The notebook (Healthcare_cleaning_dataset_combine.ipynb) was used for performing data cleaning, transformations, and exploratory data analysis (EDA).
4. **CSV Library**
-The built-in CSV library was used for reading and writing CSV files when working with raw and processed datasets.
5. **SQL (PostgreSQL)**
We used PostgreSQL as our relational database. Psycopg2 and SQLAlchemy were utilized to connect Python to the PostgreSQL database and run queries to retrieve data.
6. **Data Visualization**
- Plotly: For creating interactive visualizations integrated into the dashboard.
- Dash: Used to create the interactive dashboard that visualizes the cleaned data.
- Seaborn & Matplotlib: Additional libraries for more static and detailed visualizations during the data exploration phase.
  
## Project Structure

| File Name                             | Description                                           |
|---------------------------------------|-------------------------------------------------------|
| [Healthcare_cleaning_dataset_combine.ipynb](https://github.com/kajalkjain/Project-3-Group-2/blob/main/Healthcare_cleaning_dataset_combine.ipynb) |  Jupyter notebook used for cleaning and manipulating the healthcare dataset.|
| [Data/](https://github.com/kajalkjain/Project-3-Group-2/tree/main/Data) | Directory containing raw and processed datasets.        |
| [Database/](https://github.com/kajalkjain/Project-3-Group-2/tree/main/Database)| Directory with screenshots of SQL queries.         |
| [README.md](https://github.com/kajalkjain/Project-3-Group-2/blob/main/README.md)| This file, detailing the project setup and technologies used.         |
| [dashboard.py](https://github.com/kajalkjain/Project-3-Group-2/blob/main/dashboard.py) | Python script for creating an interactive dashboard using Dash and Plotly.|

<img width="942" alt="Screen Shot 2024-09-11 at 13 48 30" src="https://github.com/user-attachments/assets/0a42b3fa-4b0a-4c43-8de5-134ab664a5a5">


## How to Run the Project
### Prerequisites
- Python 3.x
- PostgreSQL
- Install the required Python libraries using the following commands:
```bash
conda install dash pandas plotly psycopg2 sqlalchemy seabon matplotlib
```
### Steps
1. Clone the repository:
```bash
git clone https://github.com/kajalkjain/Project-3-Group-2.git
```
2. Database Setup:
- Set up a PostgreSQL database and ensure it is populated with the required dataset.
- The queries used for extracting and manipulating the data are stored in the Database/ folder as screenshots.
3. Set Up Database Connection in the Code
- Update the following connection parameters in the code to match your PostgreSQL setup:
- **Install Required Libraries:**
  - Install the libraries to connect and interact with the PostgreSQL database:
    ```bash
    pip install psycopg2-binary sqlalchemy
    ```
- **Set Up Connection in Python Script:**
  - In your Python script, use SQLAlchemy to create the connection and psycopg2 as the driver.
  - Example code for connecting to the database:
    ```python
    from sqlalchemy import create_engine
    import psycopg2

    ```
- **Update Connection Details:**
  ```
    'dbname': 'healthcare',
    
    'user': 'postgres',
    
    'password': 'Ab123456',
    
    'host': 'bootcamp.postgres.database.azure.com',
    
    'port': '5432'
  ```

4. Data Cleaning:
- Open the Jupyter notebook (Healthcare_cleaning_dataset_combine.ipynb) and run it to perform the data cleaning steps.
5. Running the Dashboard:
- Execute the dashboard.py script to run the Dash application
```bash
python dashboard.py
```
- Open a browser window and navigate to (http://127.0.0.1:8050/)
  
This will launch the interactive dashboard where you can explore various visualisations of the cleaned healthcare data.
<img width="1437" alt="image" src="https://github.com/user-attachments/assets/0d05843d-febb-41c0-a016-35a3c380d156">


## Expected Outcomes
- **Goal:** To provide clear insights into how different features impact the prediction of medical test results.

- **How:** Data visualisations such as bar charts, Line plots and scatter plots will be created to explore the distribution of features and their relationships with test results.
the frequency of each medical condition in the dataset, giving an overview of the most common health issues.
average number of days patients stay in the hospital for each medical condition, helping us understand which conditions typically require longer hospital stays.
the market share of different insurance providers among the patients in the dataset.

- **To Target Audience:** Helps healthcare professionals and data scientists understand which factors are most influential in predicting test results, leading to more transparent and interpretable models. Helps inform feature engineering and model development strategies

## Contributions

- Sima :  Code updates, data cleaning, Data visualisation, SQL (Database)

- Kajal Jain : Data visualisation and dashboard integration.

- Napat : Data visualisation and presentations

- Jess :  Data visualisation and dashboard integration.

- Group contributions for database setup and query optimization.


