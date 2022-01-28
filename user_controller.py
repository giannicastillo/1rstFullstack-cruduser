from flask_app import app
from flask import Flask, render_template,redirect,session, request

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.all_users()

    print(users)
    for user in users:
        print(user.first_name)
    return render_template('read.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template ('create.html')


@app.route('/process_new_user',methods= ['POST'])
def process_user():
    data={
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            }
    uid = User.add_user(data)
    return redirect (f'/users/{uid}')


@app.route('/<int:user_id>')
def one_user(user_id):

    data={
        "user_id": user_id
    }
    user = User.one_user(data)
    return render_template('create.html', user=user)

@app.route('/users/<int:id>')
def display_user(id):

    data={
        "id": id
    }
    print(data)

    return render_template('show.html', user= User.show_user(data))


@app.route('/edit/<int:id>')
def edit_page(id):
    data = {
        "id": id
    }
    return render_template('edit.html', user=User.show_user(data))


@app.route('/process_edit/<int:user_id>', methods =["POST"])
def update_user(user_id):

    data={
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "id": user_id
    }
    print(data)
    User.show_edit(data)
    return redirect( f'/users/{user_id}')

    # route to take new user info to show.html
# @app.route('/<int:user:id/update')
# def newuser_display(user_id):
#     data ={
#         "user_id": user_id
#     }
#     print(data)
#     return redirect('/users/<int:user_id>')

        # NEED HELP ABOVE - TRANSFERING BACK TO SHOW.HTML AFTER UPDATE. 

@app.route('/delete/<int:user_id>')
def remove_user(user_id):
    data={
        "user_id": user_id
    }
    User.delete_user(data)
    return redirect('/')




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'