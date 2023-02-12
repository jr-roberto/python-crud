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

    def novo_usuario( values:list ):
        nome_usuario = values[0]
        senha = values[1]
        tipo_usuario = values[2]

        SQL = f"INSERT INTO tbl_usuarios (nome_usuario,senha,tipo_usuario) VALUES ('{nome_usuario}','{senha}','{tipo_usuario}')"
        banco.cur.execute(SQL)
        banco.conn.commit()
        return 

if len( banco.consulta_tabelas() ) == 0:
    # COnfigurando tabela usuario
    columns = ['nome_usuario','senha','tipo_usuario']
    banco.nova_tabela('usuarios',columns=columns)
    banco.novo_usuario( values=['roberto','banco123!','admin'] )
    # {'table_name': 'tbl_usuarios', 'columns': ['id', 'nome_usuario', 'senha', 'tipo_usuario']}

tabelas = banco.consulta_tabelas()
print(tabelas)
