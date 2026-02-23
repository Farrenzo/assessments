CREATE TABLE modules (
    module_id       SERIAL PRIMARY KEY,
    module_code     VARCHAR(20) UNIQUE NOT NULL,
    module_name     VARCHAR(100) NOT NULL,
    credit_value    INTEGER CHECK (credit_value > 0)
);