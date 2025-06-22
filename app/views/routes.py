"""
routes.py
Handles web routes for displaying, adding, editing, and deleting records.
Author: Inigo Abuel
Course: CST8002 – Programming Language Research Project
"""

from flask import Blueprint, render_template, request, redirect
from app.models.record import Record
from app.services import record_service

bp = Blueprint("main", __name__)
CSV_FILE = "dataset/2013-14_coumarin_in_dried_beverage_mixes_breads_baking_mixes.csv"

@bp.route("/")
def index():
    records = record_service.get_all_records()
    return render_template("index.html", records=records)

@bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_record = Record(
            request.form["region"],
            request.form["function"],
            request.form["origin"],
            request.form["product"],
            request.form["date_sampled"],
            request.form["type_of_test"],
            request.form["component"],
            request.form["result"],
            request.form["unit"],
            request.form["plan_code"]
        )
        record_service.get_all_records().append(new_record)
        record_service.save_all_records(CSV_FILE)
        return redirect("/")
    return render_template("add.html")

@bp.route("/delete/<int:index>")
def delete(index):
    records = record_service.get_all_records()
    if 0 <= index < len(records):
        records.pop(index)
        record_service.save_all_records(CSV_FILE)
    return redirect("/")

@bp.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    records = record_service.get_all_records()
    if request.method == "POST":
        updated_record = Record(
            request.form["region"],
            request.form["function"],
            request.form["origin"],
            request.form["product"],
            request.form["date_sampled"],
            request.form["type_of_test"],
            request.form["component"],
            request.form["result"],
            request.form["unit"],
            request.form["plan_code"]
        )
        records[index] = updated_record
        record_service.save_all_records(CSV_FILE)
        return redirect("/")
    return render_template("edit.html", record=records[index], index=index)

@bp.route("/save")
def save():
    filename = record_service.save_to_csv()
    return render_template("save_success.html", filename=filename)
