from flask import Blueprint, render_template, redirect, request, make_response, jsonify, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')