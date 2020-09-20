from flask import Flask, render_template, jsonify
import requests
import pandas as pd

app = Flask(__name__)

# most recent year in this database is 2018
url = 'https://educationdata.urban.org/api/v1/schools/ccd/directory/2018/'
response = requests.get(url)

df = pd.DataFrame(response.json())
print(df.head())


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_case')
def report_case(data=df):
  data = data.jsonify()
  return data
  # return render_template('report_case.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
