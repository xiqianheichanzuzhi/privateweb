from flask_script import Manager
from App import create_app
# 初始化,__name__代表主模块名或者包

app = create_app()  # 从APP.__init__文件导入create_app
app.app_context().push()
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
