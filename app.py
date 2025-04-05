from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ap_biology.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    unit = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    topics = Topic.query.order_by(Topic.unit).all()
    return render_template('index.html', topics=topics)

@app.route('/topic/<int:topic_id>')
def topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    return render_template('topic.html', topic=topic)

@app.route('/unit/<int:unit_number>')
def unit(unit_number):
    topics = Topic.query.filter_by(unit=unit_number).all()
    return render_template('unit.html', topics=topics, unit_number=unit_number)

@app.route('/test_images')
def test_images():
    return send_from_directory('static', 'test_images.html')

@app.route('/svg_test')
def svg_test():
    return send_from_directory('static', 'svg_test.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5004) 