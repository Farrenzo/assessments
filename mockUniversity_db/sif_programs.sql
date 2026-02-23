CREATE TABLE programs (
    program_id      SERIAL PRIMARY KEY,
    program_name    VARCHAR(100) NOT NULL,
    degree_level    VARCHAR(50) CHECK (degree_level IN ('Bachelors', 'Masters', 'PhD')),
    department      VARCHAR(100) NOT NULL
);