from flask import Flask, jsonify,request

app=Flask(__name__)

tasks=[
    {
        'id':1,
        'title':u'"buyGroceries',
        'description':u"Milk,apples,grapes",
        'done':False
    },
        {
        'id':2,
        'title':u'"learn python',
        'description':u"Need To find a good python tutorial online",
        'done':False
    }
]
@app.route('/add-data',methods=['POST'])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide Data",
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task Added Successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks

    })

if __name__ == "__main__":
    app.run(debug=True)