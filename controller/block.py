from flask import jsonify

from model.block import BlockDao


class Blockquery:

    def build_mapdic_unblock(self, blocked_id, user_id, blocked_user_id):
        result = {}
        result['blocked_id'] = blocked_id
        result['user_id'] = user_id
        result['blocked_id'] = blocked_user_id

    def build_mapB_dict(self, row):
        result = {}
        result['blocked_id'] = row[0]
        result['user_id'] = row[1]
        result['blocked_user_id'] = row[2]

        return result

    def getunBlock(self, user_id, json):
        dao = BlockDao()
        blocked_user_id = json['blocked_user_id']
        blocked_id = dao.getunBlock(user_id, blocked_user_id)
        result = self.build_mapdic_unblock(blocked_id, user_id, blocked_user_id)
        return jsonify(result), 203

    def blockUser(self, blocked_user_id, json):
        user_id = json['user_id']
        dao = BlockDao()
        blk_id = dao.blockUser(user_id, blocked_user_id, blocked_user_id)
        result = self.build_mapdic_unblock(blk_id, user_id, blocked_user_id)
        return jsonify(result), 201

    def blockedBy(self, user_id):
        dao = BlockDao()
        user_tuple = dao.blockedBy(user_id)
        result_list = []
        if not user_tuple:
            return jsonify("Not Found"), 404
        else:
            for row in user_tuple:
                obj = self.build_mapB_dict(row)
                result_list.append(obj)
                print(row)
            return jsonify(result_list)

    def blockingUser(self, blocekd_user_id):
        dao = BlockDao()
        user_tuple = dao.blockingUser(blocekd_user_id)
        result_list = []
        if not user_tuple:
            return jsonify("Not Found"), 404
        else:
            for row in user_tuple:
                obj = self.build_mapB_dict(row)
                result_list.append(obj)
                print(row)
            return jsonify(result_list)