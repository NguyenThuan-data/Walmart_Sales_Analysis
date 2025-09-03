# Walmart Data Analysis

## Table of Contents
- [Project Goal and Motivation](#Project-Goal-and-Motivation)
- [Tech Stack](#Tech-Stack)
- [Files Structure](#Files-Structure)
- [Project Workflow & ETL Pipeline](#Project-Workflow-&-ETL-Pipeline)
- [Key Findings and Visualizations](#Key-Findings-and-Visualizations)
- [Actionable Insights](#Actionable-Insights)
- [Lessons Learned Through Project](#Lessons-Learned-Through-Project)

---

## Executive Summary and Business Opportunity
As a Data Science student, my goal was to move beyond theory and tackle a practical, end-to-end data analysis project. I chose to analyze this sales dataset to solve common business challenges, such as identifying top-performing products and pinpointing opportunities for growth. This project serves as a demonstration of my skills in ETL process, data manipulation, cleansing, visualizing (Python), advanced querying (SQL), and extracting actionable insights that can drive business decisions.  

This project performs an end-to-end analysis of the Walmart sales dataset to uncover key insights into branch performance, customer behavior, and product trends. The primary goal was to leverage data to answer critical business questions and provide data-driven recommendations for optimizing staffing, improving customer ratings, and increasing overall profitability. By transforming raw CSV data into a clean, queryable database and creating insightful visualizations, this analysis serves as a blueprint for strategic decision-making.

---

## Tech Stack:
- **Data Ingestion & Transformation:** Python (Pandas, NumPy)  
- **Database Management:** PostgreSQL  
- **Data Loading:** SQLAlchemy, Psycopg2  
- **Data Visualization:** Python (Matplotlib, Seaborn)  
- **Environment:** Jupyter Notebook, PgAdmin4

---

## Files Structure:
* README.md: You are here! This file provides a comprehensive overview of the project.
* [ETL.ipynb](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/ETL.ipynb): A Jupyter Notebook that handles the Extract, Transform, Load (ETL) process. It reads the raw data, performs all necessary cleaning and feature engineering, and loads the final dataset into the PostgreSQL database.
* [Visualization.ipynb](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/Visualization.ipynb): This notebook contains all the Python code used for the visual analysis, generating the charts and graphs discussed in the insights section.
* [sql_script_EDA.sql](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/sql_script_EDA.sql): The SQL script containing all queries used for the Exploratory Data Analysis (EDA). This is where the core business questions were answered.
* [walmart-10k-sales-datasets.zip](https://www.kaggle.com/najir0123/walmart-10k-sales-datasets): The original, compressed raw dataset downloaded from Kaggle.
* [Walmart.csv](https://github.com/NguyenThuan-data/Walmart_Sales_Analysis/blob/master/Walmart.csv): The cleaned and processed dataset, which is the output of the ETL.ipynb notebook.

---

## Project Workflow & ETL Pipeline

### 1. Data Extraction and Exploration
This process is to get and analyze the raw data, to come up with cleaning strategies and potential investigation.

- The raw **Walmart.csv** dataset was loaded into a Pandas DataFrame.
  [insert loading code pics)
- The first analysis step inlude using functions like `.info()`, `.describe()`, and `.head()` to get a quick overview of the data structure and statistics.

[insert .info pic]  
- This dataset contains 6435 rows(observations) and 8 columns(attributes). In unit_price, there is '$' which is very hard to do any calculation needed and it is classified as 'object', which is not correct. There also 10020 record, indicating that there might some missing data.
[insert duplicate, and missing value identify pics]
- In `unit_price` and `quantity`, there are 31 missing values was indicate by `NaN`.
- There are 102 duplicated rows

### 2. Data Cleaning
   - Remove **Duplicates entries** to ensure data accuracy.
   - **Handle Missing Values**: Drop rows  with missing values, 31 is not a significant number over more than 10000 records, won't affect overall perspective. To avoid making any bias if refilling.
   - **Fix Data Types**: Standardizing data types, converting `date` columns to `datetime` objects 
   - **Currency Formatting**: Use `.replace()` to remove **$** of `unit_price` columns and covert to `float`

 - New dataset shape after perform cleaning.

### 3. Feature Engineering
   - **Create New Columns**: Calculate the `Total Amount` for each transaction by multiplying `unit_price` by `quantity` and adding this as a new column, etc.
   - **Enhance Dataset**: Adding this calculated field will streamline further SQL analysis and aggregation tasks.

### 4. Data Loading
   -  Connect to PostgreSQL using `sqlalchemy` and load the cleaned data into each database.
   - The cleaned and transformed DataFrame was efficiently loaded into a SQL table, automating the table creation process and ensuring a reliable data warehouse for analysis.
   - Initial validation queries were run to confirm a successful and accurate data load.
   - [insert pic]

### 5. Business Intelligence & SQL Analysis
   - **Business Problem-Solving**: Write and execute SQL queries to answer critical business questions (check out sql script for all business questions)
   - **Key Business Questions Answered:**
         - Identify the top 5 revenue-generating branches.  
         - Determine peak shopping hours and days to optimize staff scheduling.  
         - Categorize products by popularity and profitability to inform pricing and marketing strategy.  
         - Analyze customer ratings to identify branches requiring service improvements.  
         - Explore product bundling opportunities through market basket analysis.  
         - Track month-over-month revenue growth to assess business performance.  
   - **Example Query: Identify the top 5 revenue-generating branches**

### 6. Project Publishing and Documentation
   - **Documentation**: Maintain well-structured documentation of the entire process in Markdown or a Jupyter Notebook.
   - **Project Publishing**: The project is public on GitHub, including:
     - The `README.md` file.
     - Jupyter Notebooks: ETL.ipynb, Visualization.ipynb
     - SQL query scripts: sql_script_EDA.sql
     - Data files: Walmrt.csv

---

## Key Findings and Visualizations

### "Health and beauty" is a Primary Profit Driver
* Profitability is heavily concentrated in two main areas. Fashion Accessories and Home & Lifestyle are the primary profit drivers, while the remaining three categories combined—Food & Beverages, Sports & Travel, and Health & Beauty—contribute less than 10% of the total profit. This presents a clear opportunity to focus marketing efforts on high-performing categories or to re-evaluate the strategy for underperforming ones.  

### Rating is not affect significantly to Profitability.
* The analysis reveals only a weak positive correlation between customer ratings and profit margins. While good service is important, a high rating on its own is not a strong predictor of a transaction's profitability. This indicates that product mix, pricing strategy, and cost of goods are the dominant factors driving profit margins.  

### Sales based on seasons, peak at the end of the year and stable for the rest. 
* The business's sales trend has stabilized, showing a pattern of predictable seasonal peaks. This suggests that revenue is driven by periodic, high-impact sales events rather than steady, incremental growth. Future strategy could focus on maximizing these peak periods while exploring promotions to lift sales during off-peak times.urs.  

---

## Actionable Insights

Based on Key findings, below is the summary of challenges, solution and suggestion for next steps.

### On Profit Concentration
- **Challenge:** The business is over-reliant on just two product categories (Fashion, Home), creating significant risk.  
- **Solution:** Protect your star categories while using targeted bundles and promotions to lift the underperforming ones.  
- **Next Step:** Conduct a SKU-level profitability analysis to identify and fix the specific products that are loss leaders.

### On Customer Ratings vs. Profitability
- **Challenge:** Efforts to boost ratings may not be driving profit, suggesting a potential misallocation of resources.  
- **Solution:** Treat customer ratings as an operational tool to flag issues (e.g., long queues, low stock), not as a direct profit metric.
- **Next Step:** Analyze the text comments behind low ratings to pinpoint and resolve specific operational failures.

### On Sales Peaks
- **Challenge:** Misaligned staffing and inventory lead to wasted labor costs during lulls and lost sales during peak hours (3 PM - 8 PM).  
- **Solution:** Implement dynamic staffing schedules that match customer traffic patterns. Schedule restocking for quiet morning hours.  
- **Next Step:** Build a demand forecasting model to proactively manage staff and inventory weeks in advance.

### On Cross-Sell Opportunity
- **Challenge:** Customers shop in silos, rarely buying from multiple categories. This is a major missed opportunity to increase the average transaction value.  
- **Solution:** Actively encourage cross-category sales through product bundles, strategic store layouts, and point-of-sale suggestions.  
- **Next Step:** Perform a Market Basket Analysis to discover the most natural product pairings and create data-driven promotions.

---

## Lessons Learned Through Project
### 1. A good Write-up is very important
- **Lesson:** the final output isn't just the code or the charts, but the clear communication of its value.
- **The Takeaway:** The most sophisticated analysis is ineffective if it can't be easily understood. Investing 20% of the project time in crafting a clear, compelling narrative in the README delivers 80% of the project's perceived value and impact. Great work that is poorly explained is invisible work.

### 2 An Analyst's Job Is to Be a Storyteller
- **Lesson:** The goal is not just to answer "what happened?" , but to answer "so what?" and "what now?".
- **The Takeaway:** Not just conduct the Key Findings, but also what can we do from that Key fidings to imrove the business
