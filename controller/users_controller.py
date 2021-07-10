from flask import jsonify

from model.users_model import UsersDao


class Basequery:


    def build_attr_dict(self, user_id, username, password, email):
        result = {}
        result['user_id'] = user_id
        result['username'] = username
        result['password'] = password
        result['email'] = email
        return result

    def build_map_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['username'] = row[1]
        result['password'] = row[2]
        result['email'] = row[3]
        return result


    def addNewUser(self, json):
        username = json['username']
        password = json['password']
        email = json['email']
        dao = UsersDao()
        user_id = dao.insertUser(username, password, email)
        result = self.build_attr_dict(user_id, username, password, email)
        return jsonify(result), 201



    def getAllUsers(self):
        dao = UsersDao()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
            print(row)
        return jsonify(result_list)