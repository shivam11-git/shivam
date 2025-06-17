from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>My first Flask page version via Webhooks</h1>
    hello World from test FROM S2I 2nd time VERSION 3.2 LEARNING OPENSHIFT 4.14 new code
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

