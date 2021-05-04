from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "ChatBotFlaskKey"


@app.route('/', methods=['GET', 'POST'])
def login():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='chatbot'
    )
    cursor = mydb.cursor()
    if request.method == 'POST':
        details = request.form
        username = details['uname']
        passwd = details['pwd']
        cursor.execute("SELECT * FROM user_login WHERE user_name='"+username+"' AND password='"+passwd+"'")
        all = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            return redirect(url_for('info'))
        else:
            return render_template('l.html')
        mydb.commit()
        cursor.close()
    return render_template('l.html')


@app.route('/info')
def info():
    return render_template('policyinfo.html')


if __name__ == '__main__':
    app.run(debug=True)
