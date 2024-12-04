# -*- coding: utf-8 -*-
import sqlite3

def setup_db():
    conn = sqlite3.connect('imc.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            altura REAL,
            peso REAL,
            imc REAL,
            classe TEXT
        );
    """)

    conn.close()
