# Mock University Assignment

## File prefixes
- sif = SQL info file
- rdf = Raw data file

### Get students in a given program

```SQL
SELECT
    s.first_name,
    s.last_name,
    s.first_name || " " || s.last_name AS first_last
FROM
    students s
JOIN
    student_programs sp
ON  s.student_id = sp.student_id
JOIN
    programs p
ON  sp.program_id = p.program_id
WHERE
    p.program_name = 'BSc Computer Science';
```

### Get required modules for a program

```SQL
SELECT
    m.module_code,
    m.module_name
FROM
    modules m
JOIN
    program_modules pm
ON  m.module_id = pm.module_id
WHERE
    pm.program_id = 1
AND pm.is_required = TRUE;
```

### Get student transcript

```SQL
SELECT
    m.module_code,
    e.term,
    e.grade
FROM
    enrollments e
JOIN
    modules m
ON  e.module_id = m.module_id
WHERE
    e.student_id = 42;
```

