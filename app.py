from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_siurvey

responses = []
questions = [ 
    'Question1',
    'Question2',
    'Question3',
    ]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dope'
app.debug = True

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def root_page():
    return render_template('homepage.html')

@app.route('/question/<int:number>')
def first_question(number):
    if len(responses) != len(questions):
        return render_template('question.html', question=questions[number])
    
    if len(responses) != number:
        flash("You are trying to access an invalid questions")
        return redirect(f'/question/{len(responses)}')
    
    if len(responses) == len(questions):
        return redirect('/complete')
    

@app.route('/question/answer', methods=['POST'])
def answer_question():
    answer = request.form['answer']
    responses.append(answer)
    return redirect(f'/question/{len(responses)}')

@app.route('/complete')
def complete():
   return render_template('complete.html', question=questions, response=responses)