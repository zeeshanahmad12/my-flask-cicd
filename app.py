from flask import Flask

app = Flask(__name__)

BG_COLOR = "red"
VERSION = "V3"

@app.route('/')
def home():
    return f'''
    <html>
    <body style="background-color: {BG_COLOR}; 
                 text-align: center; 
                 padding: 50px;
                 color: white;
                 font-size: 40px;">
        <h1>Flask App - {VERSION}</h1>
        <p>Background: {BG_COLOR}</p>
        <p>OpenShift S2I + CI/CD Demo!</p>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
