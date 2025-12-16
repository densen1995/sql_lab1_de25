---
title: Welcome to sakila database(Insights from a DVD rental data)
---

<Details title='    SOL Queries using duckdb sakila database in evidence dashboard'>

  This page can be found in your project at `/pages/sakila.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>







---
Title: "Sakila  Long  Movies Statistics"
Description: "An overview of the Long movie from the Sakila database"
---

# Long Movies Statistics

Below, we calculate and visualize the movies length greater than 180 minutes  from the Sakila database

```sql long_movies
    FROM film
    SELECT title, length
    WHERE length > 180 
    ORDER BY length DESC;
```

<BarChart
    data={long_movies}
    title="Long movies"
    x= title
    y=length
    swapXY=true
   
/>


---
Title: "Sakila Love Statistics"
Description: "An overview of the love movie from the Sakila database"
---

# Movie with word "love" Statistics

Below, we visualize the  movies with the word "love" from the Sakila database.

```sql love_movies
 FROM film
    SELECT title,
        rating,
        length,
        description
    WHERE regexp_matches(lower(title), '\\blove\\b')
    ORDER BY title;
```

<BarChart
    data={ love_movies}
    title="Movies with 'love in it "
    x=title
    y=length
   
/>

---
Title: "Sakila Movie Length Statistics"
Description: "An overview of the movie length statistics from the Sakila database"
---

# Movie Length Statistics

Below, we calculate and visualize the **shortest**, **average**, **median**, and **longest** movie lengths from the Sakila database.

```sql length_stat

    SELECT
        'Shortest' AS label, MIN(length) AS value
FROM film
UNION
SELECT
        'Average' AS label, AVG(length) AS value
FROM film
UNION
SELECT
        'Median' AS label, MEDIAN(length) AS value
FROM film
UNION
SELECT
        'Longest' AS label, MAX(length) AS value
FROM film

```

<BarChart
    data={length_stat}
    title="Movie length statistics"
    x= label
    y=value
/>


---
Title: "Sakila Most expensive movies per day Statistics"
Description: "An overview of the Most expensive movies rental per day from the Sakila database"
---

# Most expensive movies per day Statistics

Below, we calculate and visualize the most expensive movies per day from the Sakila database.

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

<BarChart
    data={most_exp_movies_per_day}
    title="Most expensive movies per day"
    x=title
    y=cost_per_day
/>


---
Title: "Sakila Top actor counts Statistics"
Description: "An overview of the  actors with the most movies from the Sakila database"
---

# Top actor counts Statistics

Below, we calculate and visualize the actors with the most movies from the Sakila database.

```sql top_actor_counts
    SELECT a.actor_id, a.first_name || ' ' || a.last_name AS actor_name, 
    COUNT(fa.film_id) AS nr_movie_count
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    GROUP BY a.actor_id, actor_name
    ORDER BY nr_movie_count DESC 
    LIMIT 10
```

<BarChart
    data={top_actor_counts}
    title="Top actor counts"
    x=actor_name
    y=nr_movie_count
/>


---
Title: "Sakila Top renters Statistics"
Description: "An overview of the  customers with the most movie rentals from the Sakila database"
---

# Top renters Statistics

Below, we calculate and visualize the customers with the most movie rentals from the Sakila database.

```sql top_renters
    SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer_name, 
    COUNT(r.rental_id) AS rentals
    FROM customer c
    JOIN rental r ON c.customer_id = r.customer_id
    GROUP BY c.customer_id, customer_name
    ORDER BY rentals DESC;
    LIMIT 12
```

<BarChart
    data={top_renters}
    title="Top renters"
    x=customer_name
    y=rentals
/>


---
Title: "Highest replace cost"
Description: "An overview of the movies with the highest replace cost from the Sakila database"
---

# Highest replace cost Statistics

Below, we calculate and visualize the movies with the highest replace cost from the Sakila database.

```sql highest_replace_cost
    FROM film 
    SELECT title, replacement_cost
    ORDER BY replacement_cost DESC
    LIMIT 15
```

<BarChart
    data={ highest_replace_cost}
    title="Highest replace cost"
    x=title
    y=replacement_cost
    swapXY = true
/>



---
Title: "Most country customers"
Description: "An overview of the countries with the most customers from the Sakila database"
---

# Most country customers Statistics

Below, we calculate and visualiz the countries with the most customers from the Sakila database.

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

<BarChart
    data={ most_country_customer}
    title="Most country customers"
    x=country
    y=customer_count
/>

---
Title: "Top rented movies"
Description: "An overview of the movies with the highest number of rentals from the Sakila database"
---

# Top rented movies Statistics

Below, we calculate and visualize the movies with the highest number of rentals from the Sakila database.

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

<BarChart
    data={ top_rented_movies}
    title="Top rented movies"
    x=title
    y=rental_count
/>

---
Title: "Revenue per film category"
Description: "An overview of movie categories and their respective revenues from the Sakila database"
---

# Revenue per film category Statistics

Below, we calculate and visualize  movie categories and their respective revenues from the Sakila database.

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
    swapXY = true
/>

---
Title: "Top customer by spend"
Description: "An overview of top customers based on their total expenditure from the Sakila database"
---

# Top customer by spend Statistics

Below, we calculate and visualize top customers based on their total expenditure from the Sakila database.

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

