from config.dbconfig import pg_config
import psycopg2

class FollowsDao:

    def getFollowUser(self, f_id, followed_user_id, following_user_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO follower(followed_user_id, following_user_id) VALUES(%s, %s) returning f_id;"
        cursor.execute(query, (followed_user_id, following_user_id))
        f_id = cursor.fetchone()[0]
        self.conn.commit()
        return f_id

    def getFollowersby(self, followed_user_id):
        cursor = self.conn.cursor()
        query = "SELECT f_id,followed_user_id, following_user_id from follower where following_user_id=%s;"
        cursor.execute(query, (followed_user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getunFollow(self, following_user_id, followed_user_id):
        cursor = self.conn.cursor()
        query = "delete from follower where following_user_id=%s and followed_user_id=%s;"
        cursor.execute(query, (following_user_id, followed_user_id))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0