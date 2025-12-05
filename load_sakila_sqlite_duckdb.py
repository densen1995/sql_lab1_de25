import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path


DATA_PATH = Path.cwd() / "data"  ##reusable parent
SQLITE_PATH = DATA_PATH / "sqlite-sakila.db" ##source path
DUCKDB_PATH = DATA_PATH / "sakila.duckdb"  ##destination path

DATA_PATH.mkdir(exist_ok=True) ##to ensure the folder exists

source = sql_database(credentials=f"sqlite:///{SQLITE_PATH}", schema="main")

pipeline = dlt.pipeline(
    pipeline_name = "sakila_sqlite_duckdb",
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)),
    dataset_name="staging",   
)

load_info = pipeline.run(source, write_disposition = "replace")

print(load_info)
                        

