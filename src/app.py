from flask import redirect, render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

from daos.reference_dao import ReferenceDao
from config import app, db

reference_dao = ReferenceDao(db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():
    return render_template("/new_reference.html")
 
@app.route("/references", methods=["GET"])
def references():
    refs = reference_dao.get_references()   # Fetch references from the repository
    return render_template("reference_list.html", references=refs)



@app.route("/references", methods=["POST"])
def create_new_reference():
    datafields = ["name","author","title","journal","year",\
                  "volume","number","pages","month","note",\
                    "publisher","editor"]
    data = {}
    for field in datafields:
        input = None if request.form.get(field) == '' else request.form.get(field)
        data[field] = input

    reference_dao.create_reference(data)
    return redirect("/")
