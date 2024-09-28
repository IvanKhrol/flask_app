#!/usr/bin/python3

from flask import Flask

app = Flask(__name__) # Создаем экземпляр класса Flask и указываем ему имя модуля откуда брать настройки

@app.route('/') # Декоратор - обработчик определенных запросов/событий
def main_page():
  return  'Hello world'

if __name__ == '__main__':
  app.run(port=5010, debug=True) # Запускаем на нужном порте с отладочной инфой