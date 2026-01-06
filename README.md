![Project Overview](Project%20Overview.png)


# Customer Behavior Analysis — End-to-End Data Pipeline (Python, SQL, Power BI)

## Overview

This project implements a complete end-to-end data analytics pipeline to analyze customer shopping behavior. Raw transactional data is cleaned and transformed using Python, loaded into a PostgreSQL database, analyzed using SQL, and visualized through an interactive Power BI dashboard.

The project was enhanced by refactoring the data processing logic into an object-oriented Python pipeline. This design improves maintainability, scalability, and reusability compared to a procedural script, and more closely reflects real-world data engineering practices.

---

## Dataset

- Source: Public / Synthetic retail dataset  
- Format: CSV  
- Description: Customer transactions including purchase amounts, product categories, review ratings, age, and purchase frequency  

The dataset contains common real-world issues such as missing values, inconsistent formatting, and redundant columns.

---

## Tools & Technologies

- Python (Pandas, NumPy, SQLAlchemy)
- SQL (PostgreSQL)
- Power BI (Data modeling, DAX, interactive dashboards)
- Jupyter Notebook
- Git & GitHub

---

## Data Pipeline Architecture

- Raw CSV Data
- Python OOP Pipeline (Cleaning & Feature Engineering)
- PostgreSQL (Relational Storage)
- SQL (Analysis & Validation)
- Power BI (Visualization & Reporting)


---

## Object-Oriented Pipeline Design

To improve code quality and structure, the data pipeline was implemented using Object-Oriented Programming (OOP). All data processing steps are encapsulated within a dedicated pipeline class, with each transformation represented as a separate method.

### Why OOP Improves the Project

- Encapsulates all pipeline logic within a single reusable object  
- Improves maintainability by isolating individual transformation steps  
- Allows easy extension of the pipeline with new features  
- Reflects production-style ETL and data engineering workflows  

---

## Pipeline Responsibilities

The object-oriented pipeline performs the following tasks:

- Load raw CSV data  
- Fill missing review ratings using category-level medians  
- Standardize column names and formats  
- Engineer new features such as customer age groups  
- Convert purchase frequency categories into numerical day-based values  
- Remove redundant or low-value columns  
- Load cleaned data into PostgreSQL using SQLAlchemy  

---

## Project Workflow

### 1. Data Ingestion & Cleaning (Python)

- Loaded raw CSV data using Pandas  
- Cleaned and standardized data  
- Performed feature engineering to support analysis  

---

### 2. Database Loading & SQL Analysis

- Loaded cleaned data into PostgreSQL  
- Wrote SQL queries using joins, aggregations, and filters  
- Analyzed customer behavior and revenue trends  

SQL outputs were cross-validated against Python results to ensure accuracy.

---

### 3. Dashboard Development (Power BI)

- Connected Power BI directly to PostgreSQL  
- Built an interactive dashboard with KPIs, trends, and category breakdowns  
- Designed for non-technical stakeholders  

---

## Key Insights

- Identified purchasing trends and high-value customer segments  
- Highlighted top-performing product categories  
- Demonstrated how a structured data pipeline enables reliable data-driven decisions  

---

## Project Structure

---

## Skills Demonstrated

- End-to-end data pipeline development  
- Object-oriented programming for data pipelines  
- Data cleaning and feature engineering using Python  
- SQL-based analytical querying in PostgreSQL  
- Business intelligence dashboard design  

---

