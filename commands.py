from flask.cli import AppGroup
from models_05 import db

#cli = AppGroup('init', help='Initialize database')

# @cli.command('db')
# def init_db():
#     db.create_all()
#     print('OK')



 #from flask.cli import AppGroup

cli = AppGroup('init')

@cli.command('init-db')
def init_db():
# Код для инициализации базы данных
    db.create_all()
    print('Database initialized.')

#```

# 3. В файле `app.py` или `__init__.py` вашего приложения Flask добавьте следующий код для регистрации команды `init-db`:

# ```python
# from commands import cli

# app.cli.add_command(cli)
   