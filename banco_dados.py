import sqlite3 as db

class banco:
    conn = db.connect('python-crud.db')
    cur = conn.cursor()

    def nova_tabela( table_name:str , columns:list ):
        SQL = f"CREATE TABLE tbl_{table_name} ( id int primary key , { ','.join(columns) } )"
        return banco.cur.execute(SQL)
    
    def consulta_tabelas():
        SQL = "SELECT name FROM sqlite_master"

        # Retorna tupla com todas as tabelas
        query_tables = banco.cur.execute( SQL ).fetchall()

        # Reservando espaço para armazenar
        tables = []
        for table in query_tables:
            if 'sqlite_autoindex' not in table[0]:
                table_name = table[0]

                SQL = f"SELECT * FROM { table_name }"
                table_description =  banco.cur.execute( SQL ).description

                cols = []
                for columns in table_description:
                    cols.append(columns[0])
                
                table = {"table_name":table_name,"columns":cols}
                tables.append(table)
        
        return tables

tables = banco.consulta_tabelas()

for tab in tables:
    print(tab)
    
