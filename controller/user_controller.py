from app import app
from model.user_model import user_model
from flask import request
obj=user_model()

#request handler
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route('/user/update', methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route('/user/batsman/next')
def get_next_batsman_controller():
    return obj.get_next_batsman()

@app.route('/user/bowler/next')
def get_next_bowler_controller():
    return obj.get_next_bowler()

@app.route('/user/allrounder/next')
def get_next_allrounder_controller():
    return obj.get_next_allrounder()
