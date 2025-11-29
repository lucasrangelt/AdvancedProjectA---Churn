-- Churn Values
SELECT
    CASE
        WHEN churn = TRUE THEN 'True values'
        WHEN churn = FALSE THEN 'False values'
        ELSE 'Null values'
    END AS title,
    COUNT(churn) AS totalvalues,
    SUM(totalcharges) AS sumvalues
FROM
    churntable
GROUP BY
    title

-- Customer Churn Rate
SELECT
    AVG(CASE WHEN churn = TRUE THEN 1.0 ELSE 0.0 END) AS churn_rate
FROM
    churntable