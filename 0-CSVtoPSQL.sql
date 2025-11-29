-- 1: Create the database (Should be done inside PgAdmin)
CREATE DATABASE churntable;

-- 2: Create the table and columns
CREATE TABLE churntable (
    customerID VARCHAR(10),
    gender VARCHAR(16),
    seniorCitizen BOOLEAN,
    "partner" BOOLEAN,
    dependents BOOLEAN,
    tenure INT,
    phoneService BOOLEAN,
    multipleLines VARCHAR(20),
    internetService VARCHAR(16),
    onlineSecurity VARCHAR(20),
    onlineBackup VARCHAR(20),
    deviceProtection VARCHAR(20),
    techSupport VARCHAR(20),
    streamingTV VARCHAR(20),
    streamingMovies VARCHAR(20),
    "contract" VARCHAR(16),
    paperlessBilling BOOLEAN,
    paymentMethod VARCHAR(32),
    monthlyCharges FLOAT,
    totalCharges FLOAT,
    churn BOOLEAN
);

-- 3: Take data from CSV and insert into churntable (Should be done inside PgAdmin)
\copy churntable (customerID, gender, seniorCitizen, partner, dependents, tenure, phoneService, multipleLines, internetService, onlineSecurity, onlineBackup, deviceProtection, techSupport, streamingTV, streamingMovies, contract, paperlessBilling, paymentMethod, monthlyCharges, totalCharges, churn) FROM 'C:/Users/LUCAS/Downloads/Academico e Vida Profissional/Data Science/AdvancedProjectA/WA_Fn-UseC_-Telco-Customer-Churn.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8', NULL ' ');