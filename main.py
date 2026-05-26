import psycopg2
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "postgresql://postgres:FjwnbBWUzdrUxlWyjrIBpAnqxNBtrJZJ@postgres.railway.internal:5432/railway"


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


@app.get("/")
def home():
    return {"message": "Football API is running"}


@app.get("/players")
def get_players():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, position, market_value_in_eur FROM players LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "position": row[1], "market_value": row[2]} for row in rows]


@app.get("/clubs")
def get_clubs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, domestic_competition_id FROM clubs LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "competition": row[1]} for row in rows]


@app.get("/clubs/{club_name}/players")
def get_club_players(club_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name, p.position, p.market_value_in_eur
        FROM players p
        JOIN clubs c ON p.current_club_id = c.club_id
        WHERE c.name = %s
        ORDER BY p.market_value_in_eur DESC NULLS LAST
    """, (club_name,))
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "position": row[1], "market_value": row[2]} for row in rows]
