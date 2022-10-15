from flask import Flask
from threading import Thread

app = Flask('')

def start(message=None):
  if message == None:
    message = '<html><head><style>*{font-family:system-ui;}</style></head><body><h1>You are using <b>replit keep alive from PyPi</b>.<br>Head over to a site like <a href="https://up.rdsl.ga/">up.rdsl.ga</a> to keep your repl alive with this webserver.</h1><p>Thanks for using me!</p></body></html>'
  @app.route('/')
  def home():
      return message 
  
  def run():
    print("[Replit keep alive] server is running on port 8080")
    app.run(host='0.0.0.0',port=8080) #localhost doesn't work, thats why it is 0.0.0.0
    
  
  def keep_alive():  
      t = Thread(target=run)
      t.start()
  keep_alive()
# Keep alive using up.rdsl.ga!


def WaitressStart(message=None):
  if message == None:
    message = '<html><head><style>*{font-family:system-ui;}</style></head><body><h1>You are using <b>replit keep alive from PyPi</b>.<br>Head over to a site like <a href="https://up.rdsl.ga/">up.rdsl.ga</a> to keep your repl alive with this webserver.</h1><p>Thanks for using me! - waitress version</p></body></html>'
  @app.route('/')
  def home():
      return message 
    
  def run():
    print("[Replit keep alive] waitress is serving at port 8080")
    import waitress
    waitress.serve(app, host='0.0.0.0', port=8080) #localhost doesn't work, thats why it is 0.0.0.0
    

  
  def keep_alive():  
    
      t = Thread(target=run)
      
      t.start()
  keep_alive()
# Keep alive using up.rdsl.ga!