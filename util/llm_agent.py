###############
# LLM agent
# manage Natural Language requests
###############
import os
from openai import OpenAI
import json
import util.schema_manager as schm

def llm_response(cursor, user_input):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    instr='You are an AI assistant tasked with converting user queries into SQL statements. \
        You must return output in strict JSON format.\
        Rules:\
        1. Output must be valid JSON.\
        2. Do not include markdown code fences.\
        3. Do not include any extra text before or after the JSON.\
        4. The JSON must contain exactly two keys:\
        - "sql": the SQL statement only\
        - "explanation": a short explanation of what the SQL does\
        5. "sql" must contain only one SQL statement.\
        6. Use only the provided schema.\
           '
    user_input += "The database uses SQLite and contains the following tables:"
    tables = schm.Schema_getTables(cursor)
    for tb in tables:
        cols = schm.Schema_getColumns(cursor,tb)
        user_input += f'"{tb}"({",".join(cols)}) '
    response = client.responses.create(
        model="gpt-5.2",
        instructions=instr,
        input=user_input,
    )
    #print(response.output_text)
    raw = response.output_text.strip()
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        return False, f"Invalid JSON returned by model: {raw}"
    return True, result

