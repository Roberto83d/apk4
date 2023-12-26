from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True)
    
    from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def check_data_integrity():
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        cursor.execute('SELECT SUM(balance) FROM account')
        total_balance = cursor.fetchone()[0]

        cursor.execute('SELECT SUM(quantity) FROM inventory')
        total_quantity = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(id) FROM transaction_history')
        total_transactions = cursor.fetchone()[0]

        conn.close()

        return {
            'total_balance': total_balance,
            'total_quantity': total_quantity,
            'total_transactions': total_transactions
        }
    except sqlite3.Error as e:
        return {'error': str(e)}

# Endpoint do uruchamiania sprawdzenia integralności danych
@app.route('/check_integrity')
def run_check_integrity():
    data = check_data_integrity()
    return render_template('integrity_results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
