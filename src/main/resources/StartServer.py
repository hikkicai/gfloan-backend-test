from flask import Flask
from flask import render_template
from flask import request
import pymysql

app = Flask(__name__, template_folder='./')
db = pymysql.connect("localhost", "root", "root", "calculator_data")
sql_insert = "INSERT INTO add_data  (user_ip,times,sum) values (%s,1,%s)"
sql_query = "SELECT times,sum FROM add_data WHERE user_ip=%s"
sql_update = "UPDATE add_data SET times=%s,sum=%s WHERE user_ip=%s"


def update_db(ip, total):
    with db.cursor() as cur:
        cur.execute(sql_query, ip)
        result = cur.fetchone()
        if not result:
            cur.execute(sql_insert, (ip, total))
        else:
            cur.execute(sql_update, (result[0] + 1, result[1] + total, ip))

        db.commit()


def query_db():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    msg = total = ''
    if request.method == "POST":
        x = request.form['num1'].strip()
        y = request.form['num2'].strip()

        try:
            total = float(x) + float(y)
        except ValueError as e:
            msg = str.format("Invalid data was given: ", e)
        except Exception as e:
            msg = str.format("Oops, something went wrong! ", e)
        else:
            update_db(request.remote_addr, total)

        return render_template('add.html', RESULT=str(total), MSG=msg)
    return render_template('add.html')


if __name__ == "__main__":
    app.run()

