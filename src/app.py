from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():
   return 'Hi there!'

if __name__ == '__main__':
   app.run()