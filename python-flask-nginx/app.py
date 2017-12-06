from flask import Flask
from extensions import db
from api import registerApi, signApi, serviceApi


def create_app():

    '''
    This is the application factory which returns the flask app object.
    The config_name directs a runtime configuration load.
    '''
    #config_object = ".".join(('config',config_name))
    app = Flask(__name__)
    #app.config.from_object(config_object)
    app.config.from_object('config.settings.TestConfig')
    #app.config.from_pyfile('settings.py', silent=True)

    '''
    initialize the db and register the modularized services to the app.
    '''
    db.init_app(app)
    #init_db(app)
    
    app.register_blueprint(registerApi)    
    app.register_blueprint(signApi)
    app.register_blueprint(serviceApi)

    return app


def init_db(current_app):
    with current_app.app_context():
        db.create_all()



'''
if __name__=='__main__':    
    app = create_app('DevelopmentConfig')  # os.environ['ENV_SETTINGS']; export ENV_SETTINGS='DevelopmentConfig'
    
    app.run(debug=True)'''
