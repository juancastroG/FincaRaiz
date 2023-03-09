from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

application = Flask(__name__)

@application.route('/')
def index():
  
  # Set path Selenium
  WINDOW_SIZE = "1920,1080"

  # Options
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
  chrome_options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

  # Get the response and print title
  driver.get("https://www.fincaraiz.com.co/finca-raiz/venta/chapinero/bogota")
  contenedor = driver.find_element_by_xpath('//*[@id="listingContainer"]')
  return contenedor.text

  driver.close()
  
  return "ShelsyHola"
if __name__ == '__main__':
    application.run(debug=True)
    application.run(host='0.0.0.0', port=80)
