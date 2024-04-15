import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

server.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
server.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
server.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')

@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return {'error': 'Invalid credentials', 'status': 401}
    
    # check db for user
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (auth.username, auth.password))
    user = cur.fetchone()
    cur.close()

    if res>0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email and auth.password != password:
            return {'error': 'Invalid credentials', 'status': 401}
        else:
            return createJWT(auth.username, os.environ.get('JWT_SECRET'), True)
    else:
        return {'error': 'Invalid credentials', 'status': 401}
        

def createJWT(username, secret, status):
    if status:
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, secret, algorithm='HS256')
        return {'token': token, 'status': 200}
    else:
        return {'error': 'Invalid credentials', 'status': 401}
    