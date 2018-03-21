from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/request-counter')
def list_questions():
    pass



if __name__ == '__main__':
    app.secret_key = "topsecr3et"
    app.run(debug=True, host='0.0.0.0', port=5000)