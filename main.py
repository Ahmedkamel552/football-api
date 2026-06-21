from typing import Optional
from pydantic import BaseModel, Field
import os
from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()
DATABASE_URL = os.environ.get("DATABASE_URL")

# ... get_db_connection and all existing endpoints ...

# Add these at the bottom


class PlayerFilter(BaseModel):
    position: Optional[str] = None
    min_value: Optional[int] = Field(default=0, ge=0)
    max_value: Optional[int] = Field(default=1000000000, ge=0)
    limit: int = Field(default=20, ge=1, le=100)


@app.post("/players/filter")
def filter_players(filters: PlayerFilter):
    # ... rest of the code
