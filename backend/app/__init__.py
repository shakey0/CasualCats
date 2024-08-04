from flask import Flask, g, request, make_response, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf
import os

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
  
  csrf = CSRFProtect()
  csrf.init_app(app)

  from .routes import main as main_blueprint

  app.register_blueprint(main_blueprint)

  @app.before_request
  def check_privacy_policy():
    g.show_privacy_policy = not request.cookies.get('privacy_policy_seen')

  @app.context_processor
  def inject_common_context():
    env = 'development' if app.debug else 'production'
    return {
      'show_privacy_policy': g.show_privacy_policy,
      'csrf_token': generate_csrf(),
      'env': env
    }
  
  @app.route('/acknowledge_privacy_policy')
  def acknowledge_privacy_policy():
    response = make_response(jsonify(message="Privacy policy acknowledged"))
    response.set_cookie('privacy_policy_seen', 'yes', max_age=60*60*24*365*2) # Set cookie for 2 years
    return response

  return app
