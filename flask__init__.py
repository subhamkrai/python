#!/usr/bin/python3
from  flask import  Flask
import  subprocess
#  creating  application name  
app=Flask(__name__)

#  web page 
page='''
        <h1>  Hello world  </h1>
        <h2>  python is awesome </h2>
'''
# defining routes  

@app.route('/')
#  defining function ob behalf of  /test
def  hello():
        return  page

# defining routes 
@app.route('/sec')
def  imp():
	return  "GOogle"

@app.route('/cmd',methods=['POST'])
def  command():
	out=subprocess.getoutput('date')
	return  out



#    running  app data

if  __name__  ==  "__main__"  :

        app.run(host='0.0.0.0',port=80)







