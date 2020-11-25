from flask import Flask,jsonify,request

# CREATE AN APP
app = Flask(__name__)

# CREATE THE DATA

contacts = [
    {
        "id":1,
        "name":"aditya",
        "done":False,
        "number":8817268423
    },
    {
        "id":2,
        "name":'nihal',
        "done":False,
        "number":9875676700
    },
    {
        "id":3,
        "name":'daksh',
        "done":False,
        "number":9700004188
    }
]

# CREATE THE ROUTE
@app.route("/add-data",methods = ["POST"])

# CREATE A FUNCTION FOR ADDING THE DATA

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        "name": request.json['name'],
        'number': request.json.get('number'),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

# GET THE DATA FROM API

@app.route("/get-data")

def get_data():
    return jsonify({
        "data":contacts

    })


if(__name__ == "__main__"):
    app.run(debug = True)
