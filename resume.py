from flask import (Flask, render_template, make_response, Response, flash,
                   url_for, request, redirect, session)
import json

import models

app = Flask(__name__)

# def save_data():
#     try:
#         data = json.loads(request.cookies.get('User'))
#     except TypeError:
#         data = {}
#     return data

app.secret_key = 'lq3j45lj*&(YKDH(*YDSH*&^DHKJHidya98y34ukh98**&6andfjka'


@app.route('/')
def home():
    return render_template('resume_setup_form.html')


@app.route('/save', methods=['POST'])
def save():
    dictionary = dict(request.form.items())
    print(dictionary)
    if dictionary.get('page') == 'resume_setup_form':
        dictionary.pop("page")
        models.User.create(**dictionary)
        username = dictionary.get('username')
        session['username'] = dictionary.get('username')

        return redirect(url_for('employment', username=username))

    elif dictionary.get('page') == 'employment_form':
        username = dictionary.pop('username')
        choice = dictionary.pop('choice')
        dictionary.pop('page')

        user = models.User.get(models.User.username == session['username'])
        models.Employment.create(user=user, **dictionary)

        if choice == "New Employment":
            return redirect(url_for('employment', username=username))

        elif choice == "Submit":
            return redirect(url_for('generator', username=username))

        return 'Employment (clicked Submit) > Generator'


@app.route('/add/employment/<string:username>')
def employment(username):
    return render_template('employment_form.html', username=username)


@app.route('/resume/<string:username>')
def generator(username):
    try:
        user_instance = models.User.get(models.User.username == username)
        jobs = user_instance.get_employment()


        return render_template('resume-file.html', user_instance=user_instance, jobs=jobs)
    except models.DoesNotExist:
        flash('Username does NOT exist!')
        return redirect(url_for('home'))


if __name__ == '__main__':
    models.initialize()

app.run(debug=True, host='0.0.0.0', port=8000)