from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, PolicyInfoForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '56ca92a96c7a8dc6'


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('info'))
        else:
            flash("Username / Password is InValid")
    return render_template('l.html', title='Login', form=form)


@app.route('/info', methods=['GET', 'POST'])
def info():
    form = PolicyInfoForm()
    return render_template('infy.html', title='Info', form=form)


if __name__ == '__main__':
    app.run(debug=True)

