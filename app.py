from flask import Flask, render_template, request, redirect
from flask_cors import CORS
#import database_handle
import databasehandle


import webbrowser


app = Flask(__name__)
CORS(app)
app.secret_key = '!@#$%^^7'


@app.route('/', methods=[ 'GET'])
def index_page_with_session():
    return render_template('add_to_do.html')
    

@app.route('/insert_item', methods=['POST', 'GET'])
def save_todo():
    try:
        task_name = request.form['todo_name']
        date = request.form['date']
        description = request.form['desc']
   
        data = [task_name, date, description]
        databasehandle.add_todo(data)
    except:
        pass

    
@app.route('/view_todolist/<order_id>')
def view_todolist(order_id):
      task = databasehandle.Read_todo(order_id)
      return render_template('mytodolist.html', users=task)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=2241)
