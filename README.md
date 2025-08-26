# Walmart Data Analysis

## Project Overview
This project is an end-to-end data analysis solution designed to extract critical business insights from any sales data. Utilizing Python for data processing, visualizating  and analysis, SQL for advanced querying, and structured problem-solving techniques to solve key business questions. The project is stimulated real-world tasks of data analysts.

As a Data Science student, my goal was to move beyond theory and tackle a practical, end-to-end data analysis project. I chose to analyze this sales dataset to solve common business challenges, such as identifying top-performing products and pinpointing opportunities for growth. This project serves as a demonstration of my skills in ETL process, data manipulation, cleansing, visualizing (Python), advanced querying (SQL), and extracting actionable insights that can drive business decisions. 

---

## Table of Contents
- [Tools](#Tools)
- [Files Structure](#Files-Structure)
---

## Tools:
- **Programming Languages:** Python
   - **Python Libraries:**
      - Pandas & NumPy: For data manipulation, cleaning, and transformation.
      - Matplotlib & Seaborn: For creating static and informative data visualizations.
      - SQLAlchemy & psycopg2: For connecting to and interacting with the PostgreSQL database from Python.
- **Database:** PostgreSQL
- **Environment:** Jupyter Notebook

---

## Files Structure:
* README.md: You are here! This file provides a comprehensive overview of the project.
* [ETL.ipynb](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/ETL.ipynb): A Jupyter Notebook that handles the Extract, Transform, Load (ETL) process. It reads the raw data, performs all necessary cleaning and feature engineering, and loads the final dataset into the PostgreSQL database.
* [Visualization.ipynb](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/Visualization.ipynb): This notebook contains all the Python code used for the visual analysis, generating the charts and graphs discussed in the insights section.
* [sql_script_EDA.sql](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/sql_script_EDA.sql): The SQL script containing all queries used for the Exploratory Data Analysis (EDA). This is where the core business questions were answered.
* [walmart-10k-sales-datasets.zip](https://www.kaggle.com/najir0123/walmart-10k-sales-datasets): The original, compressed raw dataset downloaded from Kaggle.
* [Walmart.csv](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/Walmart.csv): The cleaned and processed dataset, which is the output of the ETL.ipynb notebook.

---

## Project Step

### 1. Download Dataset 
- **Data Source**: Use the Kaggle API to download the Walmart sales datasets from Kaggle.
- **Dataset**: Walmart Sales Dataset

### 2. Import Required Libraries and Load Data
   - **Libraries**: Install necessary Python libraries: **pandas, numpy, sqlalchemy, psycopg2**
   - **Loading Data**: Read the data into a Pandas DataFrame for initial analysis and transformations.

### 3. Explore the Data
   - **Goal**: Conduct an initial data exploration to understand data distribution, check column names, types, and identify potential issues.
   - **Analysis**: Use functions like `.info()`, `.describe()`, and `.head()` to get a quick overview of the data structure and statistics.

### 4. Data Cleaning
   - **Remove Duplicates**: Identify and remove duplicate entries to avoid skewed results.
   - **Handle Missing Values**: Drop rows or columns with missing values if they are insignificant; fill values where essential.
   - **Fix Data Types**: Ensure all columns have consistent data types (e.g., dates as `datetime`, prices as `float`).
   - **Currency Formatting**: Use `.replace()` to handle and format currency values for analysis.
   - **Validation**: Check for any remaining inconsistencies and verify the cleaned data.

### 5. Feature Engineering
   - **Create New Columns**: Calculate the `Total Amount` for each transaction by multiplying `unit_price` by `quantity` and adding this as a new column, etc.
   - **Enhance Dataset**: Adding this calculated field will streamline further SQL analysis and aggregation tasks.

### 6. Load Data into PostgreSQL
   - **Set Up Connections**: Connect to PostgreSQL using `sqlalchemy` and load the cleaned data into each database.
   - **Table Creation**: Set up tables in PostgreSQL using Python SQLAlchemy to automate table creation and data insertion.
   - **Verification**: Run initial SQL queries to confirm that the data has been loaded accurately.

### 7. SQL Analysis: Complex Queries and Business Problem Solving
   - **Business Problem-Solving**: Write and execute complex SQL queries to answer critical business questions (check out sql script for business questions)
         - Identify the top 5 revenue-generating branches.
         - Determine peak shopping hours and days to optimize staff scheduling.
         - Categorize products by popularity and profitability to inform pricing and marketing strategy.
         - Analyze customer ratings to identify branches requiring service improvements.
         - Explore product bundling opportunities through market basket analysis.
         - Track month-over-month revenue growth to assess business performance.
   - **Documentation**: Keep clear notes of each query's objective, approach, and results.

### 8. Load cleaned data to parquet and perform visual analysis
   - **Purpose:** To dig deeper into the data, I used Python's Matplotlib and Seaborn libraries to create visualizations that reveal key business trends and relationships. This visual approach helps translate raw numbers into actionable insights.
   - **Core Questions**:
      - Which product categories are the primary profit drivers? 
      - Is there a link between customer ratings and profitability? .
      - How do sales fluctuate over time?

### 8. Project Publishing and Documentation
   - **Documentation**: Maintain well-structured documentation of the entire process in Markdown or a Jupyter Notebook.
   - **Project Publishing**: The project is public on GitHub, including:
     - The `README.md` file.
     - Jupyter Notebooks: ETL.ipynb, Visualization.ipynb
     - SQL query scripts: sql_script_EDA.sql
     - Data files: Walmrt.csv

---

## Results and Insights

### Key Findings from Visual Analysis
**Profit Concentration**
* Profitability is heavily concentrated in two main areas. Fashion Accessories and Home & Lifestyle are the primary profit drivers, while the remaining three categories combined—Food & Beverages, Sports & Travel, and Health & Beauty—contribute less than 10% of the total profit. This presents a clear opportunity to focus marketing efforts on high-performing categories or to re-evaluate the strategy for underperforming ones.  

**Rating vs. Profitability Correlation** 
* The analysis reveals only a weak positive correlation between customer ratings and profit margins. While good service is important, a high rating on its own is not a strong predictor of a transaction's profitability. This indicates that product mix, pricing strategy, and cost of goods are the dominant factors driving profit margins.  

**Sales Cycle and Seasonality** 
* The business's sales trend has stabilized, showing a pattern of predictable seasonal peaks. This suggests that revenue is driven by periodic, high-impact sales events rather than steady, incremental growth. Future strategy could focus on maximizing these peak periods while exploring promotions to lift sales during off-peak times.urs.  


### Key Findings from SQL Analysis
**Operational Efficiency**
- Peak Hours Identified: The busiest shopping period is between 3 PM and 8 PM. This insight is crucial for optimizing staff schedules to improve customer service and manage queues effectively during high-traffic times.  
- Weekly Traffic Patterns: By identifying the busiest and quietest days of the week, the business can align staffing, plan promotions for slower days to drive traffic, and schedule restocking during lulls to minimize disruption.  
- Branch Performance Monitoring: The analysis of average customer ratings per branch acts as a health check. Branches with consistently lower ratings can be flagged for investigation into potential issues like management, cleanliness, or product availability, while high-performing branches can serve as models for success.

**Product & Marketing Strategy**
- Strategic Product Management: The framework for comparing product popularity (quantity sold) against profitability (profit margin) is a key strategic insight. It allows the business to:
   - Promote low-popularity, high-profit "hidden gems."
   - Bundle high-popularity, low-profit items with more profitable products.
   - Prioritize stock for items that are both popular and profitable.

- Untapped Cross-Sell Opportunity: The most significant marketing insight is that customers rarely purchase items from multiple categories in a single transaction. This reveals a major opportunity to increase the average transaction value through product bundling, strategic store layout changes, or targeted promotions designed to encourage cross-category shopping.

**Business Performance & Customer Behavior**
- High-Value Cash Customers: While used less frequently, cash payments are associated with a higher average transaction value. This suggests that cash-paying customers are a valuable segment, and ensuring their convenience (e.g., having ATMs) could be beneficial.
- Customer Segmentation: By segmenting customers into spending tiers (e.g., top, middle, bottom), the business can develop targeted strategies. This includes creating loyalty programs for top-tier customers or launching campaigns to increase the spending of lower-tier segments.
- Overall Business Health: The month-over-month (MoM) revenue growth calculation serves as a vital indicator of the business's trajectory. It helps in identifying seasonal trends, measuring the impact of marketing campaigns, and spotting potential downturns early.

---

## Challenges, Solutions and Lessions learned
