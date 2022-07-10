import sqlite3
import pandas as pd

class DataPipeline:

    def __init__(self, DB_CONNECTION_STRING: str, query: str) -> None:
        self.DB_CONNECTION_STRING = DB_CONNECTION_STRING
        self.query = query
        
    def db_conn(self, DB_CONNECTION_STRING: str):
        return sqlite3.connect(DB_CONNECTION_STRING)

    def table_all_info(self, conn):
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        return [t[0] for t in tables]

    def query_size(self, conn, query: str):
        query = query.split('FROM')[1]
        query = f"SELECT COUNT(*) FROM " + query
        cnt = conn.execute(query).fetchall()[0][0]
        print(cnt)
        return cnt

    def query_properties(self, conn, tbl_name):
        prop = conn.execute(f"PRAGMA table_info({tbl_name});").fetchall()
        return prop

    def column_list(self, prop):
        col = list()
        for i in prop:
            col.append(i[1])
        return col

    def query_data(self, conn, query: str, prop):
        chunk_size=10000
        tbl = pd.DataFrame()
        cnt = self.query_size(conn, query)
        col = self.column_list(prop)
        
        for ptr in range(0, cnt, chunk_size):
            query = query + f"  LIMIT {chunk_size} OFFSET {ptr};"
            op = conn.execute(query).fetchall()
            op = pd.DataFrame(op)
            tbl = tbl.append(op, ignore_index=True)

        print(col)
        print(len(tbl))
        tbl.columns = col
        return tbl

    def PK(self, prop):
        PK = None
        for i in prop:
            if i[-1] == 1:
                PK = i[1]
            break
        return PK
    
    def run_pipeline(self):
        conn = self.db_conn(self.DB_CONNECTION_STRING)
        table_name = self.query.split('FROM')[1].split('WHERE')[0].strip()
        prop = self.query_properties(conn, table_name)
        data = self.query_data(conn, self.query, prop)
        return data