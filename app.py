from flask import Flask, render_template,request,redirect
from model import db, Card, Item
from uuid import uuid4

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home_page():
    return render_template('index.html')

@app.route('/card/new', methods=["POST"])
def add_card():
    name = request.form.get('cardName')
    card_id = str(uuid4())
    
    Card.create(id=card_id, name=name).save()
    return redirect('/')

if __name__ == '__main__':
    db.connect()
    db.create_tables([Card,Item])
    app.run('0.0.0.0',port=5000)