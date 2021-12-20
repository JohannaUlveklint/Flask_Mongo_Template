# import os
from dotenv import load_dotenv
from flask import Flask, render_template


from app.persistance.db import init_db


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')
    init_db(_app)

    from app.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    from app.blueprints import bp_user
    _app.register_blueprint(bp_user, url_prefix='/user')

    from app.blueprints import bp_admin
    _app.register_blueprint(bp_admin, url_prefix='/admin')
    return _app
    # @_app.get('/')
    # from app.controller.user_controller import get_all_users
    # users = get_all_users()
    # return render_template('index.html', users=users)

# friends = ['Alice', 'Bob', 'Carl', 'Dina', 'Elise']
#
# # End points (routes) https://svt.se/ = main address, nyheter/lokalt = end point
#
#
# @app.get('/')  # '/' = main address but nothing more
# def index():  # Common name for the home page
#     # db_name = os.environ.get('DB_NAME')
#     name = 'Lena'
#     # raise ValueError
#     return render_template('index.html', user=name)  # '<h1>Main</h1><p>This is the coolest web site ever! </p>
#     # </p<And I am the best</p>'
#
#
# @app.get('/friends')
# def get_name():
#     return render_template('friends.html', friends_list=friends)  # 'This is the name route'


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run()

