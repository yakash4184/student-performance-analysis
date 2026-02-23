-- ============================================================
-- Project: Student Performance Analysis
-- Database: MySQL
-- ============================================================

-- Reset and create a fresh database for this project.
DROP DATABASE IF EXISTS student_performance_analysis;
CREATE DATABASE student_performance_analysis;
USE student_performance_analysis;

-- ------------------------------------------------------------
-- 1) Create tables
-- ------------------------------------------------------------

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE marks (
    student_id INT NOT NULL,
    subject VARCHAR(50) NOT NULL,
    marks INT NOT NULL,
    PRIMARY KEY (student_id, subject),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- ------------------------------------------------------------
-- 2) Insert sample data
--    10 students and 3 subjects each (Math, Science, English)
-- ------------------------------------------------------------

INSERT INTO students (student_id, name, city) VALUES
    (1,  'Aarav Sharma',  'Delhi'),
    (2,  'Diya Patel',    'Mumbai'),
    (3,  'Rohan Verma',   'Pune'),
    (4,  'Anaya Singh',   'Jaipur'),
    (5,  'Kabir Mehta',   'Ahmedabad'),
    (6,  'Isha Nair',     'Kochi'),
    (7,  'Vivaan Gupta',  'Lucknow'),
    (8,  'Sara Khan',     'Hyderabad'),
    (9,  'Arjun Das',     'Kolkata'),
    (10, 'Meera Joshi',   'Bhopal');

INSERT INTO marks (student_id, subject, marks) VALUES
    (1,  'Math',    88), (1,  'Science', 92), (1,  'English', 90),
    (2,  'Math',    72), (2,  'Science', 68), (2,  'English', 75),
    (3,  'Math',    55), (3,  'Science', 49), (3,  'English', 61),
    (4,  'Math',    39), (4,  'Science', 45), (4,  'English', 52),
    (5,  'Math',    91), (5,  'Science', 95), (5,  'English', 87),
    (6,  'Math',    64), (6,  'Science', 58), (6,  'English', 62),
    (7,  'Math',    47), (7,  'Science', 36), (7,  'English', 41),
    (8,  'Math',    76), (8,  'Science', 81), (8,  'English', 73),
    (9,  'Math',    33), (9,  'Science', 38), (9,  'English', 44),
    (10, 'Math',    59), (10, 'Science', 66), (10, 'English', 54);

-- ------------------------------------------------------------
-- 3) Analysis queries
-- ------------------------------------------------------------

-- Q1: Calculate average marks per student.
SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students AS s
JOIN marks AS m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC;

-- Q2: Find the topper of the class (highest average marks).
SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students AS s
JOIN marks AS m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC
LIMIT 1;

-- Q3: Find subject-wise highest marks (handles ties if any).
SELECT
    m.subject,
    m.student_id,
    s.name,
    m.marks AS highest_marks
FROM marks AS m
JOIN students AS s
    ON m.student_id = s.student_id
JOIN (
    SELECT
        subject,
        MAX(marks) AS max_marks
    FROM marks
    GROUP BY subject
) AS max_per_subject
    ON m.subject = max_per_subject.subject
   AND m.marks = max_per_subject.max_marks
ORDER BY m.subject, m.student_id;

-- Q4: Identify students who failed in at least one subject (marks < 40).
SELECT DISTINCT
    s.student_id,
    s.name,
    s.city
FROM students AS s
JOIN marks AS m
    ON s.student_id = m.student_id
WHERE m.marks < 40
ORDER BY s.student_id;

-- Optional detail view for failed records (subject + marks).
SELECT
    s.student_id,
    s.name,
    m.subject,
    m.marks
FROM students AS s
JOIN marks AS m
    ON s.student_id = m.student_id
WHERE m.marks < 40
ORDER BY s.student_id, m.subject;

-- Q5: Assign grades using CASE based on average marks.
-- A: >= 75, B: 50-74, C: < 50
SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks,
    CASE
        WHEN AVG(m.marks) >= 75 THEN 'A'
        WHEN AVG(m.marks) >= 50 THEN 'B'
        ELSE 'C'
    END AS grade
FROM students AS s
JOIN marks AS m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC;
