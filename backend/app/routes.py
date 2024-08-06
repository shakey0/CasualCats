from flask import Blueprint, render_template, jsonify, send_file, url_for
import os, base64

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/api/cats')
def cats():
  cats = os.environ.get('CATS').split(',')
  cats_dict = {cat: cat.replace('+', ' & ').title() for cat in cats}
  return jsonify(cats_dict)

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

@main.route('/api/<cat>')
def cat(cat):
  try:
    cats = os.environ.get('CATS').split(',')
    if cat in cats:
      photo_paths = [os.path.join('test_photos', 'sophie_on_bed.jpg'), os.path.join('test_photos', 'sophie_santa.jpg')]
      photos = []
      for photo_path in photo_paths:
        with open(photo_path, 'rb') as photo_file:
          photo_base64 = base64.b64encode(photo_file.read()).decode('utf-8')
          photos.append(photo_base64)
      return jsonify({
        'cat': "This is a cat",
        'desc': "This is a cat description",
        'photos': photos
      })
    else:
      return jsonify({'error': 'Cat not found'}), 404
  except Exception as e:
    return jsonify({'error': str(e)}), 500
