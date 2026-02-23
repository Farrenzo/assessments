CREATE TABLE students (
    student_id      SERIAL PRIMARY KEY,
    first_name      VARCHAR(50) NOT NULL,
    last_name       VARCHAR(50) NOT NULL,
    email           VARCHAR(255) UNIQUE NOT NULL,
    date_of_birth   DATE NOT NULL,
    enrollment_date DATE NOT NULL,
    status          VARCHAR(20) CHECK (status IN ('active', 'graduated', 'withdrawn'))
);