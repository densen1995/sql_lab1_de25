SELECT 
    cu.customer_id,
    cu.first_name || ' ' || cu.last_name AS customer_name,
    SUM(p.amount) AS total_spend
    
FROM staging.customer cu
JOIN staging.payment p ON cu.customer_id = p.customer_id
GROUP BY cu.customer_id, customer_name
ORDER BY total_spend DESC
LIMIT 100;