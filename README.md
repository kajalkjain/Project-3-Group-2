Project-3-Group-2
Healthcare

**A short project proposal**

The aim of our project is to provide insights into trends, costs and outcomes within the healthcare industry, potentially helping healthcare providers, policymakers and patients to make more informed decisions.

**Project Title: ** Predictive Modelling of Medical Test Results Using Synthetic Healthcare Data 

**Project Objective**

To develop and evaluate a machine learning model to predict medical test results (Normal, Abnormal, Inconclusive) using synthetic data. The project aims to improve understanding of predictive modelling in healthcare through data manipulation, feature engineering, and model training. Additionally, it will explore trends in patient demographics, cost analysis, and common conditions. By bridging data insights with practical healthcare applications, this project will provide valuable information for healthcare providers, policymakers, and patients, leading to better decision-making, optimised costs, and improved patient outcomes.

**Scope and Research Questions**

Patient Demographics: 

    - How do age, gender and blood type relate to different medical conditions?

    - Cost Analysis: What is the cost associated with different medical conditions 
    
    - What are the most common medical conditions in different age groups, and how do they impact healthcare costs? 
    
    - Can we accurately predict medical test results (Normal, Abnormal, Inconclusive) based on patient demographics, medical conditions and treatment data? 
    
    - How does the cost of treatment vary by insurance provider, and what impact does this have on patient outcomes?

    - Compare billing amounts across different medical conditions.

    - How do medical conditions impact the period stay in the hospital
  
    
**Data Source:**

We sourced our data from kaggle. Link: https://www.kaggle.com/datasets/prasad22/healthcare-dataset 

**Data Ethics**

We acknowledge the importance of healthcare data privacy and security and emphasise that this dataset is entirely synthetic. It does not contain any real patient information or violate any privacy regulations (This data has been generated using Python's Faker library to mimic real healthcare records, enabling safe learning and experimentation in healthcare analytics.)

**Visualisation Types**

Histograms, Bar charts, Pie charts to visualise the proportion of different admission types (Emergency, Elective, Urgent).
Heatmaps to explore correlations between features like age, billing amount, and test results.
Box plots to compare billing amounts across different medical conditions.
Regression plots to analyse the relationship between variables such as age and billing amount, or between medical conditions and test results.
Tools and Technologies
Python

  
  **Python Pandas** For data cleaning,transforming and analysis
  **PostreSQL** To store and extra data
  **Data Visulaisation** Python (Matplotlib(bar charts, pie charts),Pandas plotting, hvplot)
                         Seaborn: Providing a more visually appealing and informative set of default styles and colour palettes.
                         Jupyter Notebook: To interactively explore and analyse data

**Expected Outcomes**
Goal: To provide clear insights into how different features impact the prediction of medical test results.
How: Data visualisations such as bar charts, Line plots and scatter plots will be created to explore the distribution of features and their relationships with test results.
the frequency of each medical condition in the dataset, giving an overview of the most common health issues.
average number of days patients stay in the hospital for each medical condition, helping us understand which conditions typically require longer hospital stays.
the market share of different insurance providers among the patients in the dataset.
To Target Audience: Helps healthcare professionals and data scientists understand which factors are most influential in predicting test results, leading to more transparent and interpretable models. Helps inform feature engineering and model development strategies

https://media.licdn.com/dms/image/D5612AQE9qXxEJZB9Kg/article-cover_image-shrink_600_2000/0/1701942603432?e=2147483647&v=beta&t=SaJ3h3bOznZ9mXEOVs_BsupVeThur2AcaByqXJMQltU

![1701942603432](https://github.com/user-attachments/assets/609b2e25-9a62-4acb-ac85-b64158054b2e)


What is the distribution of medical conditions among different age groups?
Visualization: Bar chart or pie chart.

How do billing amounts vary across different medical conditions?
Visualization: Box plot or bar chart.

What are the proportions of different admission types (Emergency, Elective, Urgent)?
Visualization: Pie chart or bar chart.

How do test results (Normal, Abnormal, Inconclusive) vary by medical condition?
Visualization: Heatmap or bar chart.

What is the average billing amount for different insurance providers?
Visualization: Bar chart.

How does the length of hospital stay vary by medical condition?
Visualization: Box plot or bar chart.

What trends can be observed in test results over time?
Visualization: Line plot.

How do different blood types correlate with medical conditions?
Visualization: Heatmap or stacked bar chart.

What is the distribution of medication types across different medical conditions?
Visualization: Bar chart or pie chart.

How does the cost of treatment vary with different admission types?
Visualization: Box plot or bar chart.
What is the distribution of test results across different age groups?
Visualization: Stacked bar chart or heatmap.
How do billing amounts and test results relate to different admission types?
Visualization: Scatter plot or box plot.
What are the most common medical conditions per hospital?
Visualization: Bar chart or heatmap.
How do patient demographics (age, gender) influence the types of test results?
Visualization: Heatmap or grouped bar chart.
What is the frequency of different doctors treating specific medical conditions?
Visualization: Bar chart or heatmap.
