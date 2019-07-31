import os
from flask import Flask,render_template,send_file,session,redirect,request
from flask_github import GitHub
from flask_simple_geoip import SimpleGeoIP
from github import Github as gh
from webhooks.recieve_hook import receive_hook
app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET'] = os.getenv('GITHUB_CLIENT_SECRET')
if os.getenv('ENV') == 'PRODUCTION':
    app.secret_key = os.getenv('FLASK_SECRET')
else:
    app.secret_key = 'change-me'
github = GitHub(app)
scope = "read:org write:repo_hook"
sgip = SimpleGeoIP(app)
@app.route('/')
def login():
    return github.authorize(scope=scope)


@app.route('/oauth')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        return render_template('error.html',errors=["Error authenticating, please try again or contact Zeke for "
                                                    "assistance"])
    else:
        try:
            gh(oauth_token)
        except Exception as e:
            return render_template('error.html',errors=["Unknown error with authentication token ({})".format(e)])
        session['token'] = oauth_token
        return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect('/')
    g = gh(session['token'])
    return render_template('dashboard.html',github=g)


@app.route('/gh-hook/<id>',methods=['POST'])
def hook(id):
    event = receive_hook(request)
    print(event)
    return "Ok"


@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicons/favicon.ico')


app.run(host='0.0.0.0',port='5000')