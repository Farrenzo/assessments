# University & Data Engineering Assessments

This repository contains showcase and demo projects demonstrating database design, SQL development, ETL practices, and data visualization.

## Projects Included

### 1. **HealthCare Dashboard**

A healthcare analytics dashboard built from a real-world dataset.  
- Raw data was sourced from a public healthcare dataset on Kaggle.  
- A Python script performs baseline data cleaning and transformation as a foundation for SQL ingestion and dashboarding.  
- The dashboard visualizes transformed data to highlight key trends and insights.  
- **Skills Highlighted:**  
  - Python for ETL and data cleaning  
  - SQL-ready dataset design  
  - Data visualization principles

> See the full documentation inside `HealthCare_Dashboard/README.md`.

---

### 2. **Mock University Database (SQL Server)**

A fully designed sample database intended to showcase relational modeling skills for a university environment.  
This project includes:

- Normalized tables for students, programs, modules, enrollments, and relationships
- MS-SQL Server DDL scripts for table creation
- Example data loads to illustrate relationships and querying

**Conceptual Highlights**
- Entity-relationship modeling and normalization
- Many-to-many join tables (e.g., student enrolments and program modules)
- Use of primary keys, foreign keys, and constraints
- Tooling for schema development in SQL Server

This project is ideal for demonstrating your ability to **build from scratch**, write robust SQL DDL, and model real-world data domains.

---

## Repository Structure

```text
assessments/
│
├── HealthCare_Dashboard/ ← Healthcare analytics dashboard and ETL
│ ├── RawData.png
│ ├── TransformedData.png
│ ├── pd_data_cleaner.py
│ └── README.md
│
├── mockUniversity_db/ ← SQL Server database design and scripts
│ └── (SQL scripts + examples)
│
├── .gitignore
└── README.md
```


---

## Core Skills Demonstrated

Below are some technical skills explicitly showcased in this repository:

### ✔ Database Design

- Logical and physical schema design
- Normalization of relational data
- Clear representation of entities and relationships

### ✔ SQL Server Fundamentals

- Table creation with keys and constraints
- Join logic for analytics and reporting
- Data loading and management scripts

### ✔ ETL & Data Pipeline Awareness

- Data cleaning and transformation using Python
- Preparing data for SQL ingestion
- Understanding of real-world messy datasets

### ✔ Presentation Readiness

- Clean markdown documentation
- Logical project structure for review
- Visual artifacts to support narrative

---

## How to Use

1. Clone this repository.
2. For the university schema:
   - Load SQL scripts into SQL Server Management Studio (SSMS)
   - Execute DDL to create sample database
   - Use provided sample queries to validate relationships
3. For the dashboard:
   - Review the dashboard folder and ETL script.
   - Customize or extend the visualizations to suit your analytical goals.

---

## Feedback & Contributions

This repository is maintained by Dan Farrenzo as a personal showcase of database and data engineering skills.  
Feel free to fork, improve, or reference it for your own demonstrations.

---

## License

This project is released under the MIT License.
