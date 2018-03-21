from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

count = 0

@app.route('/')
@app.route('/request-counter')
def request_counter():
    return render_template("request.html")


if __name__ == '__main__':
    app.secret_key = "topsecr3et"
    app.run(debug=True, host='0.0.0.0', port=5000)