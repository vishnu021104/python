from flask import Flask, session, redirect, url_for, request

app=Flask(__name__)
app.secret_key='your_secret_key'

@app.route('/set_session')
def set_session():
    session['username']='vishnu'
    return 'session set!'

@app.route('/get_session')
def get_session():
    username=session.get('username')
    return f'Hello,{username}!'

@app.route('/logout')
def logout():
    session.pop('username')
    return 'logged out !'

@app.route('/clear_session')
def clear_session():
    session.clear()
    return 'session cleared !'

if __name__=='__main__':
    app.run(debug=True)