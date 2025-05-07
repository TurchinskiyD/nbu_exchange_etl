WITH avg_rates AS (
    SELECT
        ccy,
        CASE
            WHEN exchangedate >= CURRENT_DATE - INTERVAL '30 days' THEN 'last_30_days'
            WHEN exchangedate >= CURRENT_DATE - INTERVAL '60 days'
                 AND exchangedate < CURRENT_DATE - INTERVAL '30 days' THEN 'prev_30_days'
        END AS period,
        rate
    FROM exchange_rates
    WHERE ccy IN ('USD', 'EUR')
      AND exchangedate >= CURRENT_DATE - INTERVAL '60 days'
)
SELECT
    ccy,
    period,
    ROUND(AVG(rate), 4) AS avg_rate
FROM avg_rates
GROUP BY ccy, period
ORDER BY ccy, period;


ccy|period      |avg_rate|
---+------------+--------+
EUR|last_30_days| 47.1544|
EUR|prev_30_days| 44.9714|
USD|last_30_days| 41.5890|
USD|prev_30_days| 41.4848|
