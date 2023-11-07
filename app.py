# файл app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy()

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')   
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #posts = db.relationship('Post', backref='author', lazy=True)  # добавление
    def __repr__(self):
        return f'User({self.username}, {self.email})'  #вывод инфы о  пользователе
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     def __repr__(self):
#         return f'Post({self.title}, {self.content})'
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     def __repr__(self):
#         return f'Comment({self.content})'      
if __name__ == "__main__":
    app.run(debug=True)

    Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask\__main__.py", line 3, in <module>
    main()
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask\cli.py", line 1064, in main
    cli.main()
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\decorators.py", line 33, in new_func
    return f(get_current_context(), *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask\cli.py", line 358, in decorator
    return __ctx.invoke(f, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\click\core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\app.py", line 13, in init_db
    db.create_all()
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
    engine = self.engines[key]
             ^^^^^^^^^^^^
  File "D:\GB\TASKS\flask1-1\venv\Lib\site-packages\flask_sqlalchemy\extension.py", line 690, in engines
    raise RuntimeError(
RuntimeError: The current Flask app is not registered with this 'SQLAlchemy' instance. Did you forget to call 'init_app', or did you create multiple 'SQLAlchemy' instances?