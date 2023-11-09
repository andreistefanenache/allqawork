from flask import Flask,request
from werkzeug.routing import Rule
class Every:
	def __contains__(self,t):
		return True
class Evil(str):
	def __eq__(self,o):
		return True


app = Flask(__name__)
app.url_rule_class = lambda rule, **kwargs: Rule(rule, **{**kwargs, 'methods': None})
localvars="POST"

@app.route('/',methods=['GET'])
def hello_internet():
    return "Hello Internet!"

@app.route('/post',methods=['POST'])
def name():
    return localvars

@app.route('/put',methods=['PUT'])
def put():
	return 'PUT'

@app.route('/delete',methods=['DELETE'])
def deletion():
	return 'DELETE'
@app.route('/everything',methods=[Evil()])
def wow(methods=Every()):
	return request.method
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
