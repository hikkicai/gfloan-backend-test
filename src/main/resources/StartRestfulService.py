from flask import Flask, jsonify, request, abort
import pymysql

app = Flask(__name__)

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


@app.route('/')
def index():
    return 'Calculator is up and running!'


@app.route('/add-task/', methods=['POST'])
def add_task():
    if not request.json or 'num1' not in request.json or 'num2' not in request.json:
        abort(400)

    try:
        x = float(request.json['num1'])
        y = float(request.json['num2'])
        total = x + y
    except ValueError:
        abort(400)
    except Exception:
        abort(500)
    else:
        update_db(request.remote_addr, total)
        return jsonify({'result': total})


@app.route('/get-task/', methods=['GET'])
def get_task():
    with db.cursor() as cur:
        cur.execute(sql_query, request.remote_addr)
        result = cur.fetchone()

    if not result:
        return jsonify({'times': 0, 'sum': None})
    else:
        return jsonify({'times': result[0], 'sum': result[1]})


@app.route('/add-task-enhance/', methods=['POST'])
def add_task_enhance():
    if not request.json:
        abort(400)

    num_list = []
    for item in ['num1', 'num2', 'num3']:
        if item not in request.json:
            abort(400)

        try:
            num = request.json[item]
            assert type(num) == int
            assert 0 <= num <= 9
        except AssertionError:
            abort(400)
        except Exception:
            abort(500)
        else:
            num_list.append(num)

    op_list = []
    for item in ['operator1', 'operator2']:
        if item not in request.json:
            abort(400)

        try:
            op = request.json[item].strip()
            assert op in ['+', '-']
        except AssertionError:
            abort(400)
        except Exception:
            abort(500)
        else:
            op_list.append(op)

    total = None
    if len(num_list) == 3 and len(op_list) == 2:
        num_list[1] = num_list[1] if op_list[0] == "+" else 0 - num_list[1]
        num_list[2] = num_list[2] if op_list[1] == "+" else 0 - num_list[2]
        total = sum(num_list)
        update_db(request.remote_addr, total)

    return jsonify({'result': total})


if __name__ == '__main__':
    app.run()
