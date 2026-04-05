###############
# SQL validator
# manage SQL requests
# forward valid, block invalid
###############
### What user can do:
# Check schema of a table
# Check what tables you have
# Check samples count
# Show the first n samples
###############
import re
import sqlite3
import util.schema_manager as schm

def sql_validator(sql):
    ### validate user input SQL(for now only SELECT are supported)
    # sql: user input
    if not sql or not sql.strip():
        return False, "Empty input!"

    sql = sql.strip().rstrip(";")
    pattern = re.compile(
        r"^select\s+(.+)\s+from\s+([A-Za-z_][A-Za-z0-9_]*)$",
        re.IGNORECASE
    )
    match = pattern.match(sql)
    if not match:
        return False, "Only simple 'SELECT ... FROM table_name' is supported."

    select_part = match.group(1).strip()
    table_name = match.group(2).strip()

    if select_part == "*":
        columns = ["*"]
    else:
        columns = [col.strip() for col in select_part.split(",")]
        if not columns or any(not col for col in columns):
            return False, "Invalid column list."
        for col in columns:
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", col):
                return False, f"Invalid column name: {col}"
    return True, {
        "table": table_name,
        "columns": columns
    }

def sql_runner(table, columns, cursor):
    tables = schm.Schema_getTables(cursor)
    if not table in tables:
        return False, f"Table {table} does not exist!"
    column_list = schm.Schema_getColumns(cursor, table)
    if columns[0] != '*' and any(col not in column_list for col in columns):
        return False, "Invalid columns selected!"
    cursor.execute(f'SELECT {",".join(columns)} FROM {table}')
    contents = cursor.fetchall()
    return True, contents
