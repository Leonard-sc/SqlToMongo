from flask import Blueprint,render_template,make_response,request,jsonify,current_app
import os
from werkzeug import secure_filename

bp = Blueprint('base',__name__)
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route("/trans/",methods=['GET','POST'])
def solve_trans():
    req_type = request.form["type"]
    if req_type=="text" :
        res = request.form["data"]
        # write handle sql text here
        pass
    elif req_type=="file":
        # this is a get and print result example
        file = request.files["data"]
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
        file.save(file_path)

        # write handle sql file here 
        # and save the mongodb result file 
        # and 

        file = open(file_path)
        mongo_res = file.read()
        res = mongo_res
        pass
    
    data = jsonify({"result":res,"error":"","type":req_type})
    response = make_response(data,200)
    return response