from datetime import timedelta
import redis
# mongodb

MONGODB_SERVER = "192.168.1.39"
MONGODB_PORT = 27017
MONGODB_DB= "dqt22222x"
MONGODB_COL_f = "2222"

# mysql
DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'pymysql' # 连接数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD ='123456'  # 密码
HOST = 'localhost'  # 服务器
PORT ='3306' # 端口
DATABASE = 'web' # 数据库名


# SQLALCHEMY settings
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# app配置

BABEL_DEFAULT_LOCALE = 'zh_hans_CN'
Debuge = True
SEND_FILE_MAX_AGE_DEFAULT=timedelta(seconds=2)
SECRET_KEY = "cc"
SESSION_TYPE = 'redis' # session类型为redis
SESSION_PERMANENT = False # 如果设置为True，则关闭浏览器session就失效。
SESSION_USE_SIGNER= True # 是否对发送到浏览器上session的cookie值进行加密
SESSION_KEY_PREFIX = 'blog:' # 保存到session中的值的前缀
SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379') # 用于连接redis的配置
PERMANENT_SESSION_LIFETIME = 3000

