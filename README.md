# sql_lab1_de25

**SQL -> DuckDB -> Evidence Dashboard Project**
- Sql lab on querying  a database using SQL in duckdb from database source: Sakila database(DVD rental database) using  EDA(Exploiratory Data Analysis) ,Pandas and matplotlib for graphical representations.
- Also creating an evidence dashboard for visualisation of the data from the sakila database.


**Entity Relational Diagram(Sakila Database)**

<img src = 'SQLite3 Sakila Sample Database ERD.png' width=500>

**SQL -> DuckDB -> Evidence Dashboard Project**

**This project demonstrates a complete modern data workflow:**
- Python virtual environment setup
- Extracting data from SQLite
- Loading data into DuckDB using dlt
- Querying DuckDB with SQL
- Building an interactive Evidence dashboard
- Creating data visualizations

**Structure**
- SQLite = Source database
- dlt = Data loading tool
- DuckDB = Analytics database
- Evidence = Dashboard framework
- Node.js (via nvm) = Frontend environment

**Pyhton Enviroment Setup(venv)**
- uv venv
- activate by venv\Scripts\activate for windows /source venv/bin/activate for mac
- Install required packages: pip install dlt duckdb pandas

**Load Data from SQLite to DuckDb usind dlt**
- Import the libraries dlt Path and sql_database for this 
- Run in the terminal pyhton file/script name (load_sakila_sqlite_duckdb.py) to succesfully load into duck and create a sakila.duckdb 

**Query duckdb**
- Import duckdb and now connect  SQL to duckdb with con to read the sakila file already loaded into duckdb
- Use pandas df to get some decsription or insight of the database for further exploration 

- 
with duckdb.connect("data/sakila.duckdb") as conn:

    description = conn.sql("DESC;").df()

description #description of the sakila database after connection to duckdb"""


**Setup Node.js using nvm (Windows)**
- Download and install nvm-windows
- After installations, run node -v and npm -v in the terminal to check status

**Create Evidence Dashboard**
- Run npm install, npm run sources
- npm run dev which opens up the local host:--- for the dashboard

**Evidence Project structure**
dashboard/
│
├── pages/
│     └── sakila.md (for SQL queries)
│
├── sources/
│     ├── connection.yaml
│     ├── country.sql
│     ├── film_actor.sql
│     └── payment.sql
│
├── static/
└── package.json

**Connect Evidence to DuckDB**
- 
name: sakila
type: duckdb
options:
  filename: sakila.duckdb

**Example SQL Queries and creating graphs in Evidence inside pages/sakila.md**
- 
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
    swapXY= true
    
   
   
/>

**Start Evidence**
- cd dashboard(change directory to dashboard folder in order to run the command and start the evidence dashboard)
- npm install
- npm run dev

**Finally the evidence dashboard appears in your local host which shows the BI Report of the database based on requirements**
**Note: The evidence dashboard updates automatically when changes are made in the queries in pages/sakila.md**
=======
Sql lab on different queries using duckdb from Sakila database(DVD rental database) using  EDA in python and matplotlib for plotting and graphical representations.
Also making a BI report using an evidence dashboard for visualisation of the queries from the sakila database.