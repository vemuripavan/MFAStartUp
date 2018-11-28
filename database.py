import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["girish"]
mycol = mydb["questions"]

mylist = [
 {

        "ques" : "what is test?",
        "options" : [
                {
                        "op1" : "test",
                        "op2" : "test",
                        "op3" : "test"
                }
        ],
        "quesid" : 1,
        "ans" : 1
},
{

        "ques" : "what is test2?",
        "options" : [
                {
                        "op1" : "test",
                        "op2" : "test",
                        "op3" : "test"
                }
        ],
        "quesid" : 2,
        "ans" : 1
},
{

        "ques" : "what is test3?",
        "options" : [
                {
                        "op1" : "test",
                        "op2" : "test",
                        "op3" : "test"
                }
        ],
        "quesid" : 3,
        "ans" : 1
},
{

        "ques" : "what is test4?",
        "options" : [
                {
                        "op1" : "test",
                        "op2" : "test",
                        "op3" : "test"
                }
        ],
        "quesid" : 4,
        "ans" : 1
},
{

        "ques" : "what is test5?",
        "options" : [
                {
                        "op1" : "test",
                        "op2" : "test",
                        "op3" : "test"
                }
        ],
        "quesid" : 5,
        "ans" : 1
},
]

x = mycol.insert_many(mylist)
