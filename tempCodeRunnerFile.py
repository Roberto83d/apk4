from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Upewnij się, że nazwa pliku szablonu jest poprawna

if __name__ == '__main__':
    app.run(debug=True)
