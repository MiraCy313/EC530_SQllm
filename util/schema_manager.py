###############
# Schema manager
# manage db table schema
# find existing tables
# decide between merge/create new table
###############

def Schema_import(csv_inst, cursor):
    ### check whether create new table or import into old one.
    ### create new if needed
    ### return a table name
    # csv_inst: pandas csv_reader instance from CSV_reader
##############
    csv_columns = []
    for col, dtype in zip(csv_inst.columns, csv_inst.dtypes):   # get data types
        if "int" in str(dtype):
            sql_type = "INTEGER"
        elif "float" in str(dtype):
            sql_type = "REAL"
        else:
            sql_type = "TEXT"
        csv_columns.append([col, sql_type])
    #print(csv_columns)

    tables = Schema_getTables(cursor)       # get existing tables
    for tb in tables:
        columns = Schema_getColumns(cursor, tb)
        if len(csv_columns) == len(columns)-1:    # check if columns number match
            for cols in csv_columns:      # check if name and dtype match
                #print(cols[0],cols[1])
                if (cols[0] in columns) and (columns[cols[0]] == cols[1]):
                    pass
                else:
                    break       # this will jump the current iter, start with new tb
            else:
                print(f"Schema matched! Table name: {tb}")
                return tb
        else:
            continue
    new_tb = input("No existing schema matched. Please name a new table:")
    csv_colsdef = []
    for cols in csv_columns:
        csv_colsdef.append(f'"{cols[0]}" {cols[1]}')
    create_sql = f'CREATE TABLE IF NOT EXISTS {new_tb} (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    {", ".join(csv_colsdef)});'
    cursor.execute(create_sql)
    return new_tb
        
    
def Schema_getTables(cursor):
    ### get all table names from db, return a tuple
##############
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = tuple(row[0] for row in cursor.fetchall())
    return tables
    

def Schema_getColumns(cursor, table_name):
    ### get columns and dtypes from a table, return a tuple/dict(to be decided)
##############
    cursor.execute(f"PRAGMA table_info({table_name});")
    info = cursor.fetchall()
    columns = {row[1]: row[2] for row in info}    # dict(cname: dtype)
    return columns

