from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Milo2011'
debug = DebugToolbarExtension(app)



responses = []
ids = 0


@app.route('/')
def home_page():
    """ shows home page"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    questions = satisfaction_survey.questions
    return render_template('home.html', title = title, instructions = instructions, questions = questions)

@app.route('/questions/<int:ids>')
def questions(ids):
    """render questions"""
    if ids == 0:
        question = satisfaction_survey.questions[ids]
        ids+=1
    return render_template('questions.html', question = question, ids=ids)

@app.route('/thank-you')
def thanks():
    """ thank the surveyor"""
    return render_template('thank_you.html')

@app.route('/answers', methods=['POST', 'GET'])
def display_answers():
    """display answere"""

    return render_template('answers.html', responses = responses)

@app.route('/answers/new')
def collect_answers():
    """collect answers"""
    answer = request.form['answer']
    responses.append(answer)
    return render_template('/answers')


# @app.route('/questions0')
# def question1():
#     """render question 1"""
#     question = satisfaction_survey.questions[0]
#     return render_template('questions0.html', question = question)

# @app.route('/questions1')
# def question2():
#     """render question 2"""
#     question = satisfaction_survey.questions[1]
#     return render_template('questions1.html', question = question)

# @app.route('/questions2')
# def question3():
#     """render question 3"""
#     question = satisfaction_survey.questions[2]
#     return render_template('questions2.html', question = question)