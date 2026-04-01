###############
# CSV manager
# manage csv readin, data readin
###############
import csv

###############


def CSV_import(csv_path, table_name, cursor):
    # csv_file: The csv path user wants to import
    # table_name: user defined new table name
    # cursor: sqlite db cursor object (a connection to current db)
###############
    # add path check(or let other part check path availability)
    # add table name check (avoid same name or accidentally overwriting)
###############
    with open(csv_path, 'r', encoding='utf-8') as f:    # get header
        reader = csv.reader(f)
        header = next(reader)
        
        columns_sql = f"{header[0]} INTEGER PRIMARY KEY"
        for col_name in header[1:]:
            columns_sql += f", {col_name} TEXT"
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})"

        cursor.execute(create_table_sql)

        placeholders = ",".join(["?"] * len(header))
        insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.executemany(insert_sql, reader)


###############
