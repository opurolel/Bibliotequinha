from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    teste = "Funcionou"
    return render_template('index.html', teste2=teste)

if __name__ == '__main__':
    app.run(debug=True)