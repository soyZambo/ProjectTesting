from flask import jsonify

from model.follows import FollowsDao

class Fquery:

    def build_attF_dict(self, f_id, followed_user_id, following_user_id):
        result = {}
        result['f_id'] = f_id
        result['followed_user_id'] = followed_user_id
        result['following_user_id'] = following_user_id
        return result

    def build_mapF_dict(self, row):
        result = {}
        result['f_id'] = row[0]
        result['followed_user_id'] = row[1]
        result['following_user_id'] = row[2]

        return result

    def getFollowUser(self, following_user_id, json):
        dao = FollowsDao()
        followed_user_id = json['followed_user_id']
        f_id = dao.getFollowUser(followed_user_id, following_user_id, following_user_id)
        result = self.build_attF_dict(f_id, followed_user_id, following_user_id)
        return jsonify(result), 202

    def getFollowersby(self, following_user_id):
        dao = FollowsDao()
        user_tuple = dao.getFollowersby(following_user_id)
        result_list = []
        for row in user_tuple:
            obj = self.build_mapF_dict(row)
            result_list.append(obj)
            print(row)
        return jsonify(result_list)

    def getFollows(self, followed_user_id):
        dao = FollowsDao()
        user_tuple = dao.getFollows(followed_user_id)
        result_list = []
        for row in user_tuple:
            obj = self.build_mapF_dict(row)
            result_list.append(obj)
            print(row)
        return jsonify(result_list)

    def getunFollow(self, following_user_id, json):
        dao = FollowsDao()
        followed_user_id = json['followed_user_id']
        f_id = dao.getunFollow(following_user_id, followed_user_id)
        result = self.build_attF_dict(f_id, followed_user_id, following_user_id)
        return jsonify(result), 202