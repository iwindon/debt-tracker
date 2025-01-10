from flask import Flask, request, render_template

app = Flask(__name__)

cards = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)

