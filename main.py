import pyodbc
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Football API is running"}


@app.get("/players")
def get_players():
    players = [
        {"name": "Yamal", "position": "Attack", "market_value": 200000000},
        {"name": "Haaland", "position": "Attack", "market_value": 200000000},
        {"name": "Musiala", "position": "Midfield", "market_value": 130000000}
    ]
    return players


def get_db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-QR3ON186;"
        "DATABASE=FootballDB;"
        "Trusted_Connection=yes;"
    )
    return conn


@app.get("/clubs")
def get_clubs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 name, domestic_competition_id FROM clubs")
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
        WHERE c.name = ?
        ORDER BY p.market_value_in_eur DESC
    """, club_name)
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "position": row[1], "market_value": row[2]} for row in rows]
