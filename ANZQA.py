#encoding: utf-8

from flask import Flask,render_template,request,g,redirect, url_for, session
import config
from models import User, Question, Answer
from exts import db
from decorators import login_required
from datetime import datetime
from sqlalchemy import or_
from avatar_generator import Avatar


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    # context = {
    #     'questions':Question.query.order_by('-create_timestamp').all()
    # }
    # return render_template('index.html',**context)
    all_questions = Question.query.order_by('-create_timestamp').all()
    return render_template('index.html',questions=all_questions)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form.get('userid')
        password = request.form.get('password')
        user = User.query.filter(User.userid == userid).first()
        if user and user.check_password(password):
            session['user_id'] = user.userid
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return 'user id or password is incorrect'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        userid = request.form.get('userid')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.userid == userid).first()
        if user:
            return 'the user id has been registered'
        else:
            if password1 != password2:
                return 'the passwords inputted are different'
            else:
                user = User(userid = userid, password = password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/raisequestion/', methods=['GET', 'POST'])
@login_required
def raisequestion():
    if request.method == 'GET':
        return render_template('raisequestion.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title = title, content = content)
        user_id = session.get('user_id')
        user = User.query.filter(User.userid == user_id).first()
        question.creator_id = user.id
        db.session.add(question)
        db.session.commit()
        avatar = Avatar.generate(128, question.creator.userid)
        return redirect(url_for('index'))

@app.route('/question_detail/<question_id>')
def questiondetail(question_id):
    question = Question.query.filter(Question.id == question_id).first()
    current_time = datetime.now()
    return render_template('questiondetail.html',question = question,current_time=current_time)


@app.route('/add_answer/', methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')
    answer = Answer(content=content, question_id=question_id)
    user_id = session['user_id']
    user = User.query.filter(User.userid == user_id).first()
    answer.answer_creator_id = user.id
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('questiondetail',question_id=question_id))

@app.route('/search/')
def search():
    q = request.args.get('q')
    search_result = Question.query.filter(or_(Question.title.contains(q),Question.content.contains(q))).order_by('-create_timestamp')
    return render_template('index.html', questions=search_result)


@app.context_processor
def userlogin_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.userid == user_id).first()
        if user:
            return {'user':user}
    return {}

if __name__ == '__main__':
    app.run()


