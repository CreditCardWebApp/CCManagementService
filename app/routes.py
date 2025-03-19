from flask import render_template
from .models import CreditCardData
from . import app

import random

generated_numbers = set()

def generate_unique_number(n):
    while True:
        # Generate a random 16-digit number
        number = str(random.randint(10**(n-1), 10**n - 1))
        if number not in generated_numbers:
            generated_numbers.add(number)
            return number


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route('/admin/view_cards')
def view_cards():
    cards = CreditCardData.query.all()
    return render_template('view_cards.html', cards=cards)
