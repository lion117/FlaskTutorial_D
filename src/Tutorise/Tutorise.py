from flask import Flask
from flask import redirect,url_for,request , make_response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return redirect(url_for('hello_world'))

@app.route('/int/<int:tdata>')
def varPathInt(tdata):
    return  'variant int : %d' % tdata

@app.route('/float/<float:tfloat>')
def varPathfloat(tfloat):
    return  'variant float : %f'%tfloat

@app.route('/string/<path:tstring>')
def varPathpath(tstring):
    return  'variant string : %s'%tstring

@app.route('/var/<tvar>')
def var(tvar):
    return  'variant string : %d'%tvar


@app.route('/tget',methods=['get'])
def test_get():
    iMap ={}
    for itor in request.args:
        iMap[itor] = request.args[itor]

    return  json.dumps(iMap)
    # return unicode(type(request.args))

@app.route('/tpost',methods=['post'])
def test_form():
    iMap = {}
    for itor in request.form:
        iMap[itor] = request.form[itor]
    return json.dumps(iMap)


@app.route('/tpdata',methods=['post'])
def test_raw():
    return  unicode(request.values)

@app.route('/cookie')
def test_cookie():
    iCookie = request.cookies
    iResult = "cookies: "
    iCounts = 0
    for itor in iCookie:
        iCounts +=1
        print unicode(itor) + " : " + iCookie[itor]+  "---" + unicode(iCounts)
    iResp = make_response(iResult)
    iResp.set_cookie("name","leo")
    return  iResp

if __name__ == '__main__':
    app.run(debug=True)
