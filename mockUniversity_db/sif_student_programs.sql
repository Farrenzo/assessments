CREATE TABLE student_programs (
    student_id     INTEGER REFERENCES students(student_id),
    program_id     INTEGER REFERENCES programs(program_id),
    start_date     DATE NOT NULL,
    end_date       DATE,
    PRIMARY KEY (student_id, program_id)
);