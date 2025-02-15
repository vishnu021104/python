from flask import Flask, flash, redirect, render_template, request, url_for

app=Flask(__name__)
app.secret_key='your_secret_key'

USERNAME='vishnu'
PASSWORD='2114'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form.get('username') 
        password=request.form.get('password')


        if username==USERNAME and password==PASSWORD:
            flash('login sucessfully','success')
        else:
            flash('Invalid username or password','error')

        return redirect(url_for('login'))
    
    return render_template('message.html')

if __name__=='__main__':
    app.run(debug=True)        