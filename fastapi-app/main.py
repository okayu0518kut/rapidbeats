from fastapi import FastAPI
import sqlite3
from pathlib import Path

app = FastAPI()
DB_PATH = Path("db.sqlite3")

@app.on_event("startup")
async def startup():
    # データベースの接続を開く
    app.state.db = sqlite3.connect(DB_PATH)

@app.on_event("shutdown")
async def shutdown():
    # データベースの接続を閉じる
    app.state.db.close()

@app.get("/")
async def read_root():
    cursor = app.state.db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return {"tables": tables}

