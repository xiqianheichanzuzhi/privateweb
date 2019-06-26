from flask_admin import BaseView, expose



@expose('/admin')
def index(self):
    return self.render('index.html')


