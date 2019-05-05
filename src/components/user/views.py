from src import db
from flask import Blueprint, render_template, redirect, url_for, flash, request


user_blueprint = Blueprint('user', __name__, template_folder='templates/user')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('user/login.html')