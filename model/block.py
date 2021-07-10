from config.dbconfig import pg_config
import psycopg2

class BlockDao:

    def getunBlock(self, user_id, blocked_user_id):
        cursor = self.conn.cursor()
        query = "delete from blocked where user_id=%s and blocked_user_id=%s;"
        cursor.execute(query, (user_id, blocked_user_id))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0

    def blockUser(self, blocked_id, user_id, blocked_user_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO blocked(user_id, blocked_user_id) VALUES(%s, %s) returning blocked_id;"
        cursor.execute(query, (user_id, blocked_user_id))
        blocked_id = cursor.fetchone()[0]
        self.conn.commit()
        return blocked_id

    def blockedBy(self, user_id):
        cursor = self.conn.cursor()
        query = "SELECT * from blocked where user_id = %s;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def blockingUser(self, blocked_user_id):
        cursor = self.conn.cursor()
        query = "SELECT blocked_id,user_id, blocked_user_id from blocked where blocked_user_id=%s;"
        cursor.execute(query, (blocked_user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result