from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_questions():
    questions = read_questions()

    return render_template('questions.html', questions=questions)



if __name__ == '__main__':
    app.secret_key = "topsecr3et"
    app.run(debug=True, host='0.0.0.0', port=5000)