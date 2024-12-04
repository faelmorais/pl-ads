# -*- coding: utf-8 -*-
import sqlite3

class IMCRepository:
    def __init__(self):
        self.print_all()

    def _open_connection(self):
        self.conn = sqlite3.connect('imc.db')
        self.cursor = self.conn.cursor()

    def _close_connection(self):
        self.cursor.close()
        self.conn.close()

    def add_registro(self, nome, endereco, altura, peso, imc, classe):
        sql = 'INSERT INTO imc (nome, endereco, altura, peso, imc, classe) VALUES (?, ?, ?, ?, ?, ?)'
        data = (nome, endereco, altura, peso, imc, classe)
        self._open_connection()
        self.cursor.execute(sql, data)
        self.conn.commit()
        self._close_connection()

    def print_all(self):
        self._open_connection()
        self.cursor.execute('SELECT * FROM imc')
        registros = self.cursor.fetchall()
        print("Registros salvos no banco de dados:")
        for rec in registros:
            print(rec)
        self._close_connection()

imc_repository = IMCRepository()
