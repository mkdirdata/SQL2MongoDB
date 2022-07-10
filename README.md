# SQL2MongoDB

<br>

## DESCRIPTION

Idea is to create a Pipeline to transfer data from regular SQL databases to MongoDB.
<br>

## Current Situtation

Currently only handles SQLite.<br>
However there's some redundant, or lets say unnecesary code, will remove in future.<br>
(some sections of Datapipline, as this can be handeled through pd.read_sql_table, pd.read_sql_query, pd.read_sql)
<br>

## Pipeline

```mermaid
graph TD
  A[Create DB Conn]-->B[Load SQL Data]
  B-->C[Process Data]
  C-->D[Insert into MongoDB]
  E[Create MongoDB Conn]-->D[Insert into MongoDB]
```
<br>

## FUTURE WORK

- Exception handling
- Code rework (Majorly OOP's)
- Implement/replicate relations b/w tables (if possible)
- More to come...
<br>

## Lib versions

- Python 3.10.5
- pip 22.1.2
- pandas 1.4.3
- pymongo 4.1.1
