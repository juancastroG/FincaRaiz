from flask import Flask, render_template
application = Flask(__name__)

#a flask application with a render template
@application.route('/')

def index():
  return 'holaaa'
  
if __name__ == '__main__':
    application.run(debug=True)
    application.run(host='0.0.0.0', port=81)
