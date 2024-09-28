#!/usr/bin/python3
import sqlite3

from flask import Flask

DB_PATH = '/home/ent1r/study/bd/DB/test.s3db'

app = Flask(__name__) # Создаем экземпляр класса Flask и указываем ему имя модуля откуда брать настройки

@app.route('/') # Декоратор - обработчик определенных запросов/событий
def main_page():
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    cur.execute('Select * FROM t1')
  return  str(cur.fetchall())

if __name__ == '__main__':
  app.run(port=5010, debug=True) # Запускаем на нужном порте с отладочной инфой