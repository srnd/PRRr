import os
from flask import Flask,render_template,send_file,session,redirect
from flask_github import GitHub
from github import Github as gh
app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET'] = os.getenv('GITHUB_CLIENT_SECRET')
if os.getenv('ENV') == 'PRODUCTION':
    app.secret_key = os.getenv('FLASK_SECRET')
else:
    app.secret_key = 'change-me'
github = GitHub(app)
@app.route('/')
def login():
    return github.authorize()


@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        return render_template('error.html',errors=["Error authenticating, please try again or contact Zeke for "
                                                    "assistance"])
    else:
        try:
            gh(oauth_token)
        except Exception as e:
            return render_template('error.html',errors=["Unkown error with authentication token ({})".format(e)])
        session['token'] = oauth_token
        return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect('/')
    g = gh(session['token'])
    return render_template('dashboard.html',github=g)


@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicons/favicon.ico')


app.run(host='0.0.0.0',port='5000')