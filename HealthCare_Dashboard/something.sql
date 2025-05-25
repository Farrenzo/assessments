/* CREATE THE TABLE */
CREATE TABLE dash_data.healthcare_data (
    patient_name VARCHAR (30),
    patient_age INTEGER,
    gender VARCHAR (10),
    blood_type VARCHAR (5),
    medical_condition VARCHAR (15),
    date_of_admission DATETIME,
    doctor VARCHAR (20),
    hospital VARCHAR (30),
    insurance_provider VARCHAR (16),
    billing_amount NUMERIC (15, 0),
    room_number INTEGER,
    admission_type VARCHAR (10),
    discharge_date DATETIME,
    medication VARCHAR (15),
    test_results VARCHAR (15)
) ON [PRIMARY]
GO

EXEC sys.sp_addextendedproperty
    @name=N'TableDescription',
    @value=N'Healthcare data for patients',
    @level0type=N'SCHEMA',
    @level0name=N'dash_data',
    @level1type=N'TABLE',
    @level1name=N'healthcare_data';

EXEC sys.sp_addextendedproperty
    @name=N'SourceDescription',
    @value=N'Source: Healthcare data from somewhere important enough.',
    @level0type=N'SCHEMA',
    @level0name=N'dash_data',
    @level1type=N'TABLE',
    @level1name=N'healthcare_data';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The patient''s full name',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'patient_name';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The patient''s age',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'patient_age';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The patient''s gender.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'gender';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The patient''s blood type.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'blood_type';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The patient''s medical condition.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'medical_condition';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The date the patient was admitted to the hospital.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'date_of_admission';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The name of the doctor in charge of the patient.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'doctor';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The name of the hospital.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'hospital';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The name of the insurance provider.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'insurance_provider';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The total billing amount.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'billing_amount';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The room number assigned to the patient.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'room_number';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The type of admission (e.g., emergency, elective).',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'admission_type';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The date the patient was discharged from the hospital.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'discharge_date';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The medication prescribed to the patient.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'medication';

EXECUTE sp_addextendedproperty
    @name = 'MS_Description',
    @value = 'The results of any tests conducted on the patient.',
    @level0type = 'SCHEMA',
    @level0name = N'dash_data',
    @level1type = N'TABLE',
    @level1name = N'healthcare_data',
    @level2type = N'COLUMN',
    @level2name = N'test_results';


