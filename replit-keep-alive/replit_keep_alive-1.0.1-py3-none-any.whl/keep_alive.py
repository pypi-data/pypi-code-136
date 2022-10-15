from flask import Flask
from threading import Thread

app = Flask('')

def start(message):
  if message == None:
    message = "Hello World!"
  @app.route('/')
  def home():
      return message #You can change this text
  
  def run():
    app.run(host='0.0.0.0',port=8080) #localhost doesn't work, thats why it is 0.0.0.0
  
  def keep_alive():  
      t = Thread(target=run)
      t.start()
  keep_alive()
# Keep alive using up.rdsl.ga!