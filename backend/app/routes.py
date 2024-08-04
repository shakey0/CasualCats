from flask import Blueprint, render_template, jsonify
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/api/cats')
def cats():
  cats = os.environ.get('CATS').replace('+', ' & ').title().split(',')
  return jsonify(cats)

@main.route('/<cat>')
def profile(cat):
  try:
    cats = os.environ.get('CATS').split(',')
    if cat in cats:
      return render_template(f'index.html', cat=cat)
    else:
      return render_template('404.html')
  except:
    return render_template('404.html')
