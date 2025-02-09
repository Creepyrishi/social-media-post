from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/templates')
@app.route('/')
def index():
    return render_template('index.html', current_year=datetime.now().year)

@app.route('/twitter_template')
def twitter_template():
    return render_template('twitter_template.html', current_year=datetime.now().year)

@app.route('/instagram_template')
def instagram_template():
    return render_template('instagram_template.html', current_year=datetime.now().year)

@app.route('/facebook_template')
def facebook_template():
    return render_template('facebook_template.html', current_year=datetime.now().year)

@app.route('/youtube_template')
def youtube_template():
    return render_template('youtube_template.html', current_year=datetime.now().year)

@app.route('/contact')
def contact():
    return render_template('contact.html', current_year=datetime.now().year)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', current_year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
