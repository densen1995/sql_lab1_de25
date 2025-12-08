---
title: Welcome to sakila database
---

<Details title='    Queries using duckdb sakila database in evidence dashboard'>

  This page can be found in your project at `/pages/sakila.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>






```sql long_movies
    FROM film
    SELECT title, length
    WHERE length > 180 
    ORDER BY length DESC;
```

```sql love_movies
 FROM film
    SELECT title,
        rating,
        length,
        description
    WHERE lower(title) LIKE '%love%'
    ORDER BY title;
```

```sql length_stat
FROM film
    SELECT
        MIN(length) AS shortest,
        AVG(length) AS average,
        MEDIAN(length) AS median,
        MAX(length) as longest
```

```sql most_exp_movies_per_day
FROM film
    SELECT
        film_id,
        title,
        rental_rate,
        rental_duration,
        rental_rate / rental_duration AS cost_per_day
    ORDER BY cost_per_day DESC
    LIMIT 10
```
```sql top_actor_counts
    SELECT a.actor_id, a.first_name || ' ' || a.last_name AS actor_name, 
    COUNT(fa.film_id) AS nr_movie_count
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    GROUP BY a.actor_id, actor_name
    ORDER BY nr_movie_count DESC 
    LIMIT 10
```
```sql top_renters
    SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer_name, 
    COUNT(r.rental_id) AS rentals
    FROM customer c
    JOIN rental r ON c.customer_id = r.customer_id
    GROUP BY c.customer_id, customer_name
    ORDER BY rentals DESC;
    LIMIT 12
```

```sql highest_replace_cost
    FROM film 
    SELECT title, replacement_cost
    ORDER BY replacement_cost DESC
    LIMIT 15
```

```sql most_country_customer
    SELECT 
        country,
        COUNT(*) AS customer_count
    FROM customer cu
    JOIN address a ON cu.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id 
    GROUP BY country
    ORDER BY customer_count DESC
    LIMIT 5
```

```sql top_rented_movies
    SELECT 
        f.title,
        COUNT(*) AS rental_count
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY f.title
    ORDER BY rental_count DESC;
    LIMIT 10
```

```sql revenue_per_category
    SELECT
        c.name AS category,
        SUM(p.amount) AS total_revenue
    FROM category c 
    JOIN film_category fc ON c.category_id = fc.category_id
    JOIN film f ON fc.film_id = f.film_id
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    JOIN payment p ON r.rental_id = p.rental_id
    GROUP BY category
    ORDER BY total_revenue DESC;

```

<BarChart
    data={ revenue_per_category}
    title="Revenue per film category"
    x=category
    y=total_revenue
/>

```sql top_cust_total_spend
    SELECT 
        cu.customer_id,
        cu.first_name || ' ' || cu.last_name AS customer_name,
        SUM(p.amount) AS total_spend
    
    FROM customer cu
    JOIN payment p ON cu.customer_id = p.customer_id
    GROUP BY cu.customer_id, customer_name
    ORDER BY total_spend DESC;
    LIMIT 5
```


<BarChart
    data={top_cust_total_spend}
    title="Top customer by spend"
    x=customer_name
    y=total_spend
/>

