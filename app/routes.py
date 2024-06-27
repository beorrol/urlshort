from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import URL
import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    link = URL.query.filter_by(short_url=short_url).first()

    if link:
        return generate_short_url()
    
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        existing_url = URL.query.filter_by(original_url=original_url).first()

        if existing_url:
            return render_template('shortened.html', short_url=existing_url.short_url)

        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        return render_template('shortened.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url_entry = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url_entry.original_url)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
