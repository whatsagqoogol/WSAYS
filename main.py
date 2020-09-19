from flask import Flask, render_template
import requests

app = Flask(__name__)

# most recent year in this database is 2018
url = 'https://educationdata.urban.org/api/v1/schools/ccd/directory/2018/'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
