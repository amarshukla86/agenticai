import os
import sqlite3
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

load_dotenv(override=True)

DB_PATH = os.path.join(os.path.dirname(__file__), "sales.db")


@function_tool
def run_sql(query: str) -> str:
    """Execute a read-only SQL query on the sales database."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    return str(rows)

agent = Agent(
    name="Sales Assistant",
    model="gpt-4o-mini",
    instructions="""
    You help users answer questions about the sales database.
    Use the run_sql tool whenever database information is needed.
    """,
    tools=[run_sql],
)

result = Runner.run_sync(
    agent,
    # "Which five products generated the highest revenue this year?"
    "Which products generated more than ₹200,000 in revenue?" 
)

print(result.final_output)