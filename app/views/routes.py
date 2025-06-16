# app/views/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from app.services import record_service

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    data = record_service.get_all()
    return render_template('index.html', name="Inigo Abuel", records=data)

@bp.route('/save')
def save():
    filename = record_service.save_to_csv()
    flash(f"Data saved to {filename}")
    return redirect(url_for('routes.index'))