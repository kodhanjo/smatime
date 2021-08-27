from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Server

from flask_migrate import Migrate,MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = create_app('development')




admin=Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))




manager= Manager(app)
manager.add_command('server',Server)

migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role=Role )

if __name__ == '__main__':
    manager.run()  
