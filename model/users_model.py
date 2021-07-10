from config.dbconfig import pg_config
import psycopg2

class UsersDao:

    def insertUser(self, username, password, email):
        cursor = self.conn.cursor()
        query = "insert into users (username, password, email) values (%s, %s, %s ) returning user_id;"
        cursor.execute(query, (username, password, email,))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select user_id, username, password,email from users"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
            print(row)
        return result
