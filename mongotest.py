from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost:27017')
db = client.girish

app = Flask(__name__)

@app.route("/questions", methods = ['GET'])
def questions():
    try:
        names = db.questions.find({},{"ques":1,"options":1,"_id":0,"quesid":1,"ans":1})
        return dumps(names)
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/answers", methods = ['POST'])
def answers():
    try:
        data = json.loads(request.data)
        quesid = data['quesid']
        yourans = data['yourans']
        if quesid and yourans:
            status = db.myanswers.insert_one({
                "quesid" : quesid,
                "yourans" : yourans
            })
        return dumps({'message' : 'SUCCESS'})
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/myanswers", methods = ['GET'])
def myanswers():
    try:
        answers = db.myanswers.find({},{"quesid":1,"yourans":1})
        return dumps(answers)
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/check/<id>", methods = ['GET','POST'])
def check(id):
    try:
        doc=db.questions.find({'quesid':float(id)})
        return dumps(doc)
    except Exception as e:
        return dumps({'error': str(e)})

@app.route('/questionUI')
def showMachineList():
    return render_template('QuesionList.htm')


"""
@app.route("/myquestion/<id>", methods = ['GET'])
def myquestionbyid(id):
    try:
        answers = db.myquestions.find_one({},{"quesid": "%d","ques":1,"options":1,"_id":0  %float(id)})
        return dumps(answers)
    except Exception as e:
        return dumps({'error' : str(e)})


@app.route("/merge",methods = ['GET'])
def merge():
    try:
        main=db.myquestions.aggregate([
           {
              $lookup: {
                 from: "myanswers",
                 localField: "quesid",
                 foreignField: "quesid",
                 as: "fromItems"
              }
           },
           {
              $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$fromItems", 0 ] }, "$$ROOT" ] } }
           },
           { $project: { fromItems: 0 } }
        ])
"""
if __name__ == '__main__':
     app.run(host='localhost',port='5002',debug = True)
