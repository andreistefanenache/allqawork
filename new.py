from flask import Flask,request
app = Flask(__name__)

@app.route('/get_record/<id>',methods=['GET'])
def get(id):
    return id

@app.route('/get_all_records',methods=['GET'])
def get_all():
    return 'all the records'

@app.route('/create_record/<name>',methods=['POST'])
def name(name):
    return name

@app.route('/delete_record/<id>',methods=['DELETE'])
def put(id):
	return id

@app.route('/update_record/<id>',methods=['UPDATE'])
def deletion(id):
	return id+str(request.json)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
