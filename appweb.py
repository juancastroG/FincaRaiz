from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
  return "holaaa shelsylinda"
  
if __name__ == '__main__':
    application.run(debug=True)
    application.run(host='0.0.0.0', port=80)
