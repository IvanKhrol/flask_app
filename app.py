#!/usr/bin/python3
import sqlite3

from flask import Flask, render_template

DB_PATH = '/home/ent1r/study/bd/DB/test.s3db'

app = Flask(__name__) # Создаем экземпляр класса Flask и указываем ему имя модуля откуда брать настройки

@app.route('/') # Декоратор - обработчик определенных запросов/событий
def main_page():
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    cur.execute('Select * FROM t1')
  return  render_template(
    'main_page.html', 
    columns=[x[0] for x in cur.description],
    data=cur.fetchall())

if __name__ == '__main__':
  app.run(port=5010, debug=True) # Запускаем на нужном порте с отладочной инфой