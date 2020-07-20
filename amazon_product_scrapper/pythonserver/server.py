from flask import Flask, render_template ,request , jsonify ,make_response
from selenium import webdriver
from time import sleep
import main
app = Flask(__name__)

@app.route('/pass_val',methods=['POST'])
def pass_val():
    website=request.args.get('value')
    main.get_details(website)
    return website

if __name__ == '__main__':
  app.run(debug=True)