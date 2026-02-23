CREATE TABLE program_modules (
    program_id  INTEGER REFERENCES programs(program_id),
    module_id   INTEGER REFERENCES modules(module_id),
    is_required BOOLEAN NOT NULL,
    PRIMARY KEY (program_id, module_id)
);