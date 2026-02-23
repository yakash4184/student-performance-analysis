# import os

# import pandas as pd
# import streamlit as st
# import mysql.connector
# from mysql.connector import Error


# st.set_page_config(page_title="Student Performance Analysis", page_icon="🎓", layout="wide")

# st.title("🎓 Student Performance Analysis Dashboard")
# st.caption("MySQL + SQL Analytics + Streamlit Interface")


# def get_connection(host: str, user: str, password: str, database: str, port: int):
#     return mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database,
#         port=port,
#     )


# def run_query(conn, query: str) -> pd.DataFrame:
#     return pd.read_sql(query, conn)


# with st.sidebar:
#     st.header("Database Connection")
#     host = st.text_input("Host", value=os.getenv("DB_HOST", "localhost"))
#     port = st.number_input("Port", value=int(os.getenv("DB_PORT", "3306")), step=1)
#     user = st.text_input("User", value=os.getenv("DB_USER", "root"))
#     password = st.text_input("Password", value=os.getenv("DB_PASSWORD", ""), type="password")
#     database = st.text_input("Database", value=os.getenv("DB_NAME", "student_performance_analysis"))
#     connect_btn = st.button("Connect & Load Analysis", type="primary")


# if not connect_btn:
#     st.info("Sidebar me database details fill karke **Connect & Load Analysis** click karein.")
#     st.stop()


# try:
#     conn = get_connection(host, user, password, database, int(port))
# except Error as e:
#     st.error(f"Database connection failed: {e}")
#     st.markdown(
#         """
#         **Setup quick checklist**
#         1. MySQL server start karein.
#         2. SQL script run karein: `Student_Performance_Analysis.sql`
#         3. Sidebar credentials verify karein.
#         """
#     )
#     st.stop()


# avg_query = """
# SELECT
#     s.student_id,
#     s.name,
#     s.city,
#     ROUND(AVG(m.marks), 2) AS average_marks
# FROM students s
# JOIN marks m ON s.student_id = m.student_id
# GROUP BY s.student_id, s.name, s.city
# ORDER BY average_marks DESC;
# """

# topper_query = """
# SELECT
#     s.student_id,
#     s.name,
#     s.city,
#     ROUND(AVG(m.marks), 2) AS average_marks
# FROM students s
# JOIN marks m ON s.student_id = m.student_id
# GROUP BY s.student_id, s.name, s.city
# ORDER BY average_marks DESC
# LIMIT 1;
# """

# subject_top_query = """
# SELECT
#     m.subject,
#     m.student_id,
#     s.name,
#     m.marks AS highest_marks
# FROM marks m
# JOIN students s ON m.student_id = s.student_id
# JOIN (
#     SELECT subject, MAX(marks) AS max_marks
#     FROM marks
#     GROUP BY subject
# ) mx ON m.subject = mx.subject AND m.marks = mx.max_marks
# ORDER BY m.subject, m.student_id;
# """

# failed_query = """
# SELECT DISTINCT
#     s.student_id,
#     s.name,
#     s.city
# FROM students s
# JOIN marks m ON s.student_id = m.student_id
# WHERE m.marks < 40
# ORDER BY s.student_id;
# """

# grades_query = """
# SELECT
#     s.student_id,
#     s.name,
#     ROUND(AVG(m.marks), 2) AS average_marks,
#     CASE
#         WHEN AVG(m.marks) >= 75 THEN 'A'
#         WHEN AVG(m.marks) >= 50 THEN 'B'
#         ELSE 'C'
#     END AS grade
# FROM students s
# JOIN marks m ON s.student_id = m.student_id
# GROUP BY s.student_id, s.name
# ORDER BY average_marks DESC;
# """

# raw_marks_query = """
# SELECT
#     s.student_id,
#     s.name,
#     m.subject,
#     m.marks
# FROM students s
# JOIN marks m ON s.student_id = m.student_id
# ORDER BY s.student_id, m.subject;
# """

# avg_df = run_query(conn, avg_query)
# topper_df = run_query(conn, topper_query)
# subject_top_df = run_query(conn, subject_top_query)
# failed_df = run_query(conn, failed_query)
# grade_df = run_query(conn, grades_query)
# raw_marks_df = run_query(conn, raw_marks_query)

# col1, col2, col3 = st.columns(3)
# col1.metric("Total Students", int(avg_df.shape[0]))
# col2.metric("Class Average", round(float(avg_df["average_marks"].mean()), 2))
# col3.metric("Topper", f"{topper_df.iloc[0]['name']} ({topper_df.iloc[0]['average_marks']})")

# tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
#     [
#         "Average Per Student",
#         "Class Topper",
#         "Subject-wise Highest",
#         "Failed Students",
#         "Grades (CASE)",
#         "Raw Data",
#     ]
# )

# with tab1:
#     st.subheader("Average Marks Per Student")
#     st.dataframe(avg_df, use_container_width=True)
#     st.bar_chart(avg_df.set_index("name")["average_marks"], use_container_width=True)

# with tab2:
#     st.subheader("Topper of the Class")
#     st.dataframe(topper_df, use_container_width=True)

# with tab3:
#     st.subheader("Subject-wise Highest Marks")
#     st.dataframe(subject_top_df, use_container_width=True)

# with tab4:
#     st.subheader("Students Who Failed (marks < 40)")
#     if failed_df.empty:
#         st.success("No failed students found.")
#     else:
#         st.dataframe(failed_df, use_container_width=True)

# with tab5:
#     st.subheader("Grades Using CASE Statement")
#     st.dataframe(grade_df, use_container_width=True)
#     grade_counts = grade_df["grade"].value_counts().sort_index()
#     st.bar_chart(grade_counts, use_container_width=True)

# with tab6:
#     st.subheader("Raw Marks Table")
#     st.dataframe(raw_marks_df, use_container_width=True)

# conn.close()




import os
import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import Error

st.set_page_config(page_title="Student Performance Analysis", page_icon="🎓", layout="wide")

st.title("🎓 Student Performance Analysis Dashboard")
st.caption("MySQL + SQL Analytics + Streamlit Interface")

# -----------------------------
# Get DB credentials from Railway ENV variables
# -----------------------------

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
    )


def run_query(conn, query: str):
    return pd.read_sql(query, conn)


# -----------------------------
# Try connecting to Database
# -----------------------------

try:
    conn = get_connection()
except Exception as e:
    st.error("❌ Database connection failed.")
    st.code(str(e))
    st.stop()

# -----------------------------
# Queries
# -----------------------------

avg_query = """
SELECT
    s.student_id,
    s.name,
    s.city,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id, s.name, s.city
ORDER BY average_marks DESC;
"""

topper_query = """
SELECT
    s.student_id,
    s.name,
    s.city,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id, s.name, s.city
ORDER BY average_marks DESC
LIMIT 1;
"""

# -----------------------------
# Execute Queries
# -----------------------------

try:
    avg_df = run_query(conn, avg_query)
    topper_df = run_query(conn, topper_query)
except Exception as e:
    st.error("❌ Query execution failed.")
    st.code(str(e))
    st.stop()

# -----------------------------
# Dashboard
# -----------------------------

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", int(avg_df.shape[0]))
col2.metric("Class Average", round(float(avg_df["average_marks"].mean()), 2))
col3.metric("Topper", f"{topper_df.iloc[0]['name']} ({topper_df.iloc[0]['average_marks']})")

st.subheader("Average Marks Per Student")
st.dataframe(avg_df, use_container_width=True)
st.bar_chart(avg_df.set_index("name")["average_marks"], use_container_width=True)

conn.close()
