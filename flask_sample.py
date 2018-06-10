#!/usr/bin/python3

from  flask import Flask,render_template,request

# defining app 
app=Flask(__name__)

# start route
@app.route('/',methods=['GET','POST'])

def webpage():
	if request.method ==  'GET' :
		return  render_template('adhoc.html')
	else :
		return  render_template('hello.html')
		
		


#  running  app 
if __name__  ==  "__main__" :
	app.run(debug=True,host='0.0.0.0',port=80)


