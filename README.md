# Student Performance Analysis (MySQL + Interface)

This is a beginner-friendly SQL mini project that analyzes student marks using two related tables and a simple dashboard UI:

- `students(student_id, name, city)`
- `marks(student_id, subject, marks)`

## What this project covers

- Table design with primary and foreign keys
- Sample data insertion (10 students, 3 subjects each)
- Core analysis queries:
  - Average marks per student
  - Class topper
  - Subject-wise highest marks
  - Failed students (`marks < 40`)
  - Grade assignment using `CASE`
- Streamlit dashboard for interviewer/demo presentation

## Project files

- `Student_Performance_Analysis.sql` -> schema, data, and analysis queries
- `app.py` -> Streamlit interface/dashboard
- `requirements.txt` -> Python dependencies

## How to run (SQL only)

1. Open MySQL.
2. Run the script:
   - `Student_Performance_Analysis.sql`
3. View the query outputs.

## How to run with interface (for interview demo)

1. Ensure MySQL server is running.
2. Import SQL script:
   - `Student_Performance_Analysis.sql`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Start dashboard:
   - `streamlit run app.py`
5. In sidebar, enter DB credentials and click **Connect & Load Analysis**.

## What to show in interview (quick flow)

1. Explain schema (`students` and `marks`) and relationship.
2. Show Average Per Student tab and Topper tab.
3. Show Subject-wise Highest and Failed Students tabs.
4. Show CASE-based grading logic in Grades tab.
5. Highlight that insights come directly from SQL queries.

## Resume-ready project explanation

Built a **Student Performance Analysis** project using **MySQL and Streamlit**, with normalized tables (`students`, `marks`) and SQL analytics (joins, aggregations, subqueries, and `CASE`-based grading). Developed an interactive dashboard to present student averages, class topper, subject-wise highest scores, failed students, and grade distribution for data-driven academic insights.
