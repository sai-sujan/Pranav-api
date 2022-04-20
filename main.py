from flask import Flask, request
import pandas as pd
import os

app = Flask(__name__)


@app.route('/main', methods=['GET'])
def main():
    if request.method == 'GET':
        df = pd.read_csv("features_30_sec.csv")
        df = df.sample(frac=1).reset_index(drop=True)
        df = df.head(10)
        df = df['filename']
        print(df)

    return df.to_json()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

