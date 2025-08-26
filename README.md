# Walmart Data Analysis

## Project Overview
This project is an end-to-end data analysis solution designed to extract critical business insights from any sales data. Utilizing Python for data processing, visualizating  and analysis, SQL for advanced querying, and structured problem-solving techniques to solve key business questions. The project is stimulated real-world tasks of data analysts.

As a Data Science student, my goal was to move beyond theory and tackle a practical, end-to-end data analysis project. I chose to analyze this sales dataset to solve common business challenges, such as identifying top-performing products and pinpointing opportunities for growth. This project serves as a demonstration of my skills in data manipulation (Python), advanced querying (SQL), and extracting actionable insights that can drive business decisions. 


## Project Step

### 1. Download Dataset 
- **Data Source**: Use the Kaggle API to download the Walmart sales datasets from Kaggle.
- **Dataset Link**: [Walmart Sales Dataset](https://www.kaggle.com/najir0123/walmart-10k-sales-datasets)

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
     - The `README.md` fil.
     - Jupyter Notebooks.
     - SQL query scripts.
     - Data files.

---

## Results and Insights

This section will include your analysis findings:
- **Sales Insights**: Key categories, branches with highest sales, and preferred payment methods.
- **Profitability**: Insights into the most profitable product categories and locations.
- **Customer Behavior**: Trends in ratings, payment preferences, and peak shopping hours.


---

