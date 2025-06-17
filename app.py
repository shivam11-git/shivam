from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>My first Flask page version via Webhooks</h1>
            <p>hello World from test FROM S2I 2nd time VERSION 3.2 LEARNING OPENSHIFT 4.14 new code</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
