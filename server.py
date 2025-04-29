from flask import Flask, render_template, abort, request, redirect
from os import listdir
import csv
import pprint
import pdb

app = Flask(__name__)
#print(__name__)

@app.route("/")
@app.route("/<path>")
def path_func(path=None):
    pages = [p for p in listdir('./templates')]
    if path == "" or path == None:
        return render_template('index.html')
    else:
        if path in pages:
            return render_template(path)
        else:
            abort(404)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #print(data)
        db_io('r',data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'

def db_io(mode,input):
    #pdb.set_trace()
    output = []
    keys = ['email', 'subject', 'message']
    if mode == 'r':
        with open('./database.txt', mode='r', newline="") as my_db:
            try:
                my_csv = csv.DictReader(my_db, fieldnames=keys)
                for r in my_csv:
                    output.append(r)
                pprint.pprint(output)
                return output
            except Exception as e:
                print(e)
    else:
        with open('./database.txt', mode='a', newline="") as my_db:
            try:
                my_csv = csv.DictWriter(my_db, input.keys())
                my_csv.writerow(input)
                return output
            except Exception as e:
                print(e)


# @app.route("/")
# def my_home():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('index.html')

# @app.route("/index.html")
# def index():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('works.html')

# @app.route("/work.html")
# def work():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('work.html')

# @app.route("/contact.html")
# def contact():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     #return "<p>Hello, Kurt!</p>"
#     return render_template('components.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/<username>/<int:pnum>")
# def test(username=None, pnum=None):
#     return render_template('about.html', name=username, num=pnum)