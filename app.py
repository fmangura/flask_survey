from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_siurvey

# responses = []
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

@app.route('/question-session/<int:number>')
def first_question(number):

    if len(session['response']) != len(questions):
        return render_template('question.html', question=questions[number])
    
    if len(session['response']) != number:
        flash("You are trying to access an invalid questions")
        return redirect(f"/question/{len(session['response'])}")
    
    if len(session['response']) == len(questions):
        return redirect('/complete')
    

@app.route('/question/answer', methods=['POST'])
def answer_question():
    answer = request.form['answer']
    print(answer)
    response = session['response']
    print(response)
    response.append(answer)
    print(response)
    session['response'] = response
    print(len(session['response']))
    print(session['response'])
    return redirect(f"/question-session/{len(session['response'])}")

@app.route('/complete')
def complete():
   return render_template('complete.html')

@app.route('/question-session', methods=['POST'])
def start_session():
    session["response"] = []
    print(len(session['response']))
    return redirect('/question-session/0')

