from flask import Flask, request, jsonify, abort
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is the content'


def write_entry_to_file(entry):
    file = open('database.txt','w') 
    file.write('success!')
    # file.write(entry['timestamp'], '\t', entry['vehicle_id']) #, '\t', entry['changed_state'], '\t', entry['new_state'])
    file.close() 


@app.route('/', methods=['POST'])
def create_entry():
    # if not request.json in request.json:    #or not 'timestamp' or...
    #     abort(400)
    entry = {
        'timestamp': 'todo',
        'vehicle_id': request.json['vehicle_id']
        # 'changed_state': request.json['changed_state'],
        # 'new_state': request.json['new_state']
    }
    write_entry_to_file(entry)
    return jsonify({'entry': entry}), 201
# curl -i -H "Content-Type: application/json" -X POST -d "{"""vehicle_id""": """001"""}" http://localhost:5000/


if __name__ == '__main__':
    app.run(debug=True) 