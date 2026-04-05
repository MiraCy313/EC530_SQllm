import sqlite3
import pandas as pd
import cmd
################
import util.schema_manager as schm
import util.csv_manager as csvm
import util.sql_validator as sqlv
import util.llm_agent as llma
###### Check cmd to make the CLI, kinda handy
class SQllm(cmd.Cmd):
    prompt = "<SQllm> "
    #intro = "输入 help 查看可用命令"

    def do_csv(self, arg):
        tok = arg.split()
        if len(tok)>=1:
            match tok[0]:
                case "-i": 
                    try:
                        csv_file = csvm.CSV_reader(tok[1])
                        tb_name = schm.Schema_import(csv_file, cursor)
                        csvm.CSV_import(csv_file, tb_name, cursor)
                        conn.commit()
                        conn.close
                    except ValueError as e:
                        print(e)
                case _:
                    print("Unknown option!")
    
    def do_sql(self, arg):
        if sqlv.sql_validator(arg)[0] == False:
            print(sqlv.sql_validator(arg)[1])
        else:
            info = sqlv.sql_validator(arg)[1]
            if sqlv.sql_runner(info["table"], info["columns"], cursor)[0] == False:
                print(sqlv.sql_runner(info["table"], info["columns"], cursor)[1])
            else:
                print(sqlv.sql_runner(info["table"], info["columns"], cursor)[1])

    def do_llm(self, arg):
        result = llma.llm_response(cursor, arg)
        if result[0]==False:
            print(result[1])
        else:
            print(f"SQL: {result[1]["sql"]}")
            print(f"Explanation: {result[1]["explanation"]}")
            print("Running generated SQL code...")
            self.do_sql(result[1]["sql"])

    def emptyline(self):
        pass

    def do_exit(self, arg):
        return True

if __name__ == "__main__":
    db_path = "test/test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    SQllm().cmdloop()



