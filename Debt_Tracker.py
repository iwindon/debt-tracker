from flask import Flask, request, render_template_string

app = Flask(__name__)

cards = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_name = request.form['card_name']
        apr = request.form['apr']
        balance = request.form['balance']
        cards.append({
            'card_name': card_name,
            'apr': apr,
            'balance': balance
        })
    return render_template_string('''
        <form method="POST">
            Card Name: <input type="text" name="card_name"><br>
            APR: <input type="text" name="apr"><br>
            Balance: <input type="text" name="balance"><br>
            <input type="submit" value="Add Card">
        </form>
        <h2>Card List:</h2>
        <ul>
            {% for card in cards %}
            <li>{{ card.card_name }} - APR: {{ card.apr }} - Balance: {{ card.balance }}</li>
            {% endfor %}
        </ul>
    ''', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
