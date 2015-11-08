import sqlite3
from bottle import route, run, template

@route('/todo')
@route('/my_todo_list')
def todo_list():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

run(host='localhost', port=8090, debug=True, reload=True)