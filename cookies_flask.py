from flask import Flask, make_response, request
app=Flask(__name__)

@app.route('/set')
def setcookie():
    Response=make_response("setting cookie")
    Response.set_cookie('framework','flask')
    return Response

@app.route('/get')
def getcookie():
    Framework=request.cookies.get('framework')
    return "the framework is "+Framework


if __name__=='__main__':
    app.run(debug=True)