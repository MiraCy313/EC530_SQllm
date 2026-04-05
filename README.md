# EC530_SQllm

EC530_SQllm is an interactive Python command-line tool for importing CSV data into SQLite, validating simple SQL queries, and generating SQL from natural language using an OpenAI-powered LLM.

## Features

- Import CSV files into a local SQLite database
- Automatically infer and create table schemas from CSV column types
- Validate and execute simple SQL queries of the form `SELECT ... FROM table_name`
- Generate SQL from natural language using OpenAI responses
- Minimal CLI interface with `csv`, `sql`, `llm`, and `exit` commands

## Project Structure

- `SQllm.py` - Main CLI entry point
- `util/csv_manager.py` - CSV import and validation utilities
- `util/schema_manager.py` - Schema detection and SQLite table management
- `util/sql_validator.py` - Simple SQL parsing and execution support
- `util/llm_agent.py` - OpenAI LLM integration for natural language to SQL
- `test/` - Sample data and helper test scripts

## Prerequisites

- Python 3.10+ installed
- `pandas` package
- `openai` package
- A valid OpenAI API key stored in the environment variable `OPENAI_API_KEY`

### Install packages

```powershell
pip install pandas openai
```

### Set API key

```powershell
$env:OPENAI_API_KEY = 'your_api_key_here'
```

## Usage

Run the CLI from the project root:

```powershell
python SQllm.py
```

Once started, use these commands:

- `csv -i <path>`
  - Import a CSV file into the SQLite database
  - Example: `csv -i test/test_data_small4.csv`
- `sql <SELECT statement>`
  - Execute a validated SQL query
  - Only simple queries of the form `SELECT ... FROM table_name` are supported
  - Example: `sql SELECT * FROM my_table`
- `llm <natural language request>`
  - Ask the LLM to generate SQL for a natural language query
  - The tool prints the generated SQL, explanation, and then runs it
  - Example: `llm show me all rows from sales`
- `exit`
  - Quit the CLI

## How it works

1. `csv -i` uses `util.csv_manager.CSV_reader` to load the CSV and `util.schema_manager.Schema_import` to match or create a table.
2. Imported rows are inserted into SQLite via `util.csv_manager.CSV_import`.
3. `sql` uses `util.sql_validator.sql_validator` to allow only simple `SELECT ... FROM` statements, then executes them.
4. `llm` sends the user query and current database schema to OpenAI via `util.llm_agent.llm_response`.

## Notes

- The SQL validator currently supports only basic `SELECT` queries without `WHERE`, `JOIN`, or nested clauses.
- The LLM response is expected to return strict JSON with `sql` and `explanation` keys.
- The working database file is `test/test.db` by default.

## Testing

The `test/` folder contains example data and manual test scripts, such as `csv_manager_test.py`.

Run a manual import test by executing:

```powershell
python test/csv_manager_test.py
```

## License

This project is provided as-is for educational use.
