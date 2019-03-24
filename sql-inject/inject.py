from flask import Flask, request, render_template_string, g
import sqlite3
app = Flask(__name__)


form_template = """
Find user info from name:
<form method="post">
<input type="text" name="query">
</form>
"""
resp = """
RESPONSE:
{{ response }}
"""

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('users.sqlite')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def injector():
    if request.method == 'POST':
        query = request.form['query']
        c = get_db().cursor()
        query_str = f"SELECT name, favorite_food FROM users WHERE name = '{query}';"
        for q in query_str.split(';'):
            if q != '':
                print(q + ';')
                c.execute(q + ';')
        response = c.fetchall()
        return render_template_string(resp, response=response)
    return form_template
