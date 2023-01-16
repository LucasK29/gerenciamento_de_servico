import sqlite3

def connect_db():
    conn = sqlite3.connect('./data_base/belux.db',check_same_thread=False)
    return conn

def create_table(table_name, conn):
    conn.execute('CREATE TABLE {0} (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, funcao TEXT)'
    .format(table_name))

def insert_data(table_name, data_list:dict,conn):
    keys = ''
    values = ''
    for item in data_list.items():
        keys += item[0] + ', '
        if type(item[1]) != str:
            values += str(item[1]) + ', '
        else: values += "'" + item[1] + "', "
    keys = keys[:-2]
    values = values[:-2]
    conn.execute("INSERT INTO {0} ({1}) VALUES ({2})"
    .format(table_name, keys, values))
    conn.commit()

def delete_data(table_name,key,val,conn):
    conn.execute(f"DELETE from {table_name} where {key} = {val}")
    conn.commit()

def update_row(table_name,col,val1,key,val2,conn):
    #UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
    conn.execute(f"UPDATE {table_name} SET {col} = '{val1}' WHERE {key} = {val2}")
    conn.commit()

