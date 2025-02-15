from flask import Flask, redirect, url_for, request, render_template_string

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        return render_template_string('''
            <form method="post">
                Name: <input type="text" name="nm">
                <input type="submit" value="Submit">
            </form>
        ''')

if __name__ == '__main__':
    app.run(debug=True)

