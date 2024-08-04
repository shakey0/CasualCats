from flask import Flask, g, request, make_response, jsonify
from flask_wtf.csrf import CSRFProtect

def create_app():
  app = Flask(__name__)
  
  csrf = CSRFProtect()
  csrf.init_app(app)

  from .routes import main as main_blueprint

  app.register_blueprint(main_blueprint)

  @app.before_request
  def check_privacy_policy():
    g.show_privacy_policy = not request.cookies.get('privacy_policy_seen')

  @app.context_processor
  def inject_privacy_policy_flag():
    return dict(show_privacy_policy=g.show_privacy_policy)
  
  @app.route('/acknowledge_privacy_policy')
  def acknowledge_privacy_policy():
    response = make_response(jsonify(message="Privacy policy acknowledged"))
    response.set_cookie('privacy_policy_seen', 'yes', max_age=60*60*24*365*2) # Set cookie for 2 years
    return response

  return app
