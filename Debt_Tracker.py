import logging
from flask import Flask, request, render_template

app = Flask(__name__)

cards = []

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            card_name = request.form['card_name']
            apr = request.form['apr']
            balance = request.form['balance']
            card_type = request.form['card_type']
            cards.append({
                'card_name': card_name,
                'apr': apr,
                'balance': balance,
                'card_type': card_type
            })
            logging.info(f"Added card: {card_name}, APR: {apr}, Balance: {balance}, Card Type: {card_type}")
        except Exception as e:
            logging.error(f"Error processing form data: {e}")
            return "Bad Request", 400
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)



