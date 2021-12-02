from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        #database
        firstName = details['fnames']
        lastName = details['lnames']
        employee = details['uid']
        company = details['company']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Mydatas(FirstName, LastName, UID , CompanyName, Email) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, employee, company, email))
        mysql.connection.commit()
        cur.close()
        return render_template('second.html', nid=firstName, lid=lastName, uid=employee, cid=company, eid=email)
    return render_template('first.html')

@app.route('/second')
def sec():
    return render_template('second.html')


if __name__ == '__main__':
    app.run()