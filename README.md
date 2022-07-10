# SQL2MongoDB

<br>

## DESCRIPTION

<br>
Idea is to create a Pipeline to transfer data from regular SQL datbases to MongoDB.
<br>

## Current Situtation

<br>
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
