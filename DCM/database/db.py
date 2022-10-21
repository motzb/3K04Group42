from time import sleep
from PyQt5 import QtSql
from database.user import User


# Utility class to handle communications with sqlite3 database
class Database:
    def __init__(self):
        self.DB_PATH = r"database/app.db"
        self.db = None

    # to connect to the database
    def connect(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.DB_PATH)
        if not self.db.open():
            print("Unable to establish a database connection")
            return False
        else:
            self.create_table()
        return True

    # create table for the first time, if not present
    def create_table(self):
        query = QtSql.QSqlQuery()
        customer_table_query = "CREATE table users " \
                               "(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                               "username varchar(30) UNIQUE, " \
                               "password varchar(30))"

        user_table = query.exec(customer_table_query)
        print("Table Created", user_table)
        print("Table already exists, no need to create again!")

    # read all users registered in the database
    def read_all_users(self):
        all_users = list()
        self.db.transaction()
        query = QtSql.QSqlQuery()
        sql = "select id, username, password from users";
        query.exec(sql)
        while query.next():
            user = User()
            user.username = query.value(1)
            user.password = query.value(2)
            all_users.append(user)
            print(all_users[0].username)
        return all_users

    # add a new user upon registration
    def add_user(self, user):
        self.db.transaction()
        query = QtSql.QSqlQuery()
        sql = "insert into users (username, password) values('%s','%s')" % tuple(user.get_list())
        status = query.exec(sql)
        self.db.commit()
        print("User Added", status)
        sleep(0.5)
        return status

    # to delete a user already registered
    def delete_user(self, username):
        self.db.transaction()
        sql = "delete from users where username = '%s';" % (username)
        status = QtSql.QSqlQuery(sql)
        self.db.commit()
        print("user deleted")
        return status

    # login with user credentials
    def login(self, username, password):
        self.db.transaction()
        user = None
        query1 = QtSql.QSqlQuery()
        sql_user = "select id,username, password from 'users' where username = '%s' AND password = '%s' ;" % \
                   (username, password)
        result = query1.exec(sql_user)
        if (result and query1.last()):
            user = User(query1.value(1), query1.value(2))
        return user

    # check if user with specified username exists in the database or not
    def is_user_exists(self, username):
        self.db.transaction()
        user_exists = False
        query1 = QtSql.QSqlQuery()
        sql_user = "select id,username, password from 'users' where username = '%s';" % \
                   (username)
        result = query1.exec(sql_user)
        if (result and query1.last()):
            user_exists = True
        return user_exists

    # check if the user limit exceeds than 10 users
    def user_limit_exceeds(self):
        users = self.read_all_users()
        if len(users) >= 10:
            return True
        return False

# testing db functions
# db = Database()
# db.connect()
# db.create_table()
# db.add_user(User("user1", "user1"))
# print(db.is_user_exists("user1"))
