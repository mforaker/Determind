from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        login_user(user)
        flask.flash('Logged in successfully')
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)
        return flask.redirect(next or flask.url_for('index'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():

    #register_form = RegisterForm(request.form)
    #if register.method == 'POST':
        #if register_form.validate():
            #username = request.form.get('username')
            #type = request.form.get('type')
            #name = request.form.get('name')
            #password = request.form.get('password')
            #registered_user = User.query.filter_by(username=username).first()
            #if registered_user is None:
                #user = User(username=username,
                            #type=type,
                            #name=name,
                            #password=generate_password_hash(password, method='sha256'))
                #db.session.add
    return render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user/<username>')
def username(username=""):
    return

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/results')
def results():
    return render_template('results.html')

@app.route('learningstyles/<styles>')
def learningstyle(styles=""):
    return
