from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        print (results)
        users = []
        for user_data in results:
            #user(user_data)
            # user = cls(user_data)
            users.append(cls(user_data))
        return users

    @classmethod
    def one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('user_schema').query_db(query,data)
        print(results)
        return cls(results[0])

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,created_at, updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(), NOW());"
        user_id = connectToMySQL('user_schema').query_db(query,data)
        return user_id
    @classmethod
    def show_user(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('user_schema').query_db(query,data)
        return cls(results[0])
    @classmethod
    def show_edit(cls,data):
        query = "UPDATE users SET first_name =%(first_name)s , last_name =%(last_name)s, email =%(email)s, updated_at =NOW() WHERE id= %(id)s;"
        results = connectToMySQL('user_schema').query_db(query,data)
        return results

    # def showedit_update(cls,data):
    #     results=
    @classmethod
    def delete_user(cls,data):
        query= "DELETE FROM users WHERE id=%(user_id)s;"
        results= connectToMySQL('user_schema').query_db(query,data)
        return "sucess"
