from flask import Flask ,render_template,jsonify,request


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def docker():
    return 'To check the docker images'


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=800)