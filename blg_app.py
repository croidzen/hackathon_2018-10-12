from flask import Flask, request, jsonify, abort
import csv, datetime, os, json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is the content'


def write_entry_to_file(entry):
    with open('database.csv', mode='a+', newline='') as file:
        file_writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # file_writer.writerow(['Success!'])
        file_writer.writerow([entry['timestamp'], entry['vehicle_id']]) #, entry['changed_state'], entry['new_state']])


@app.route('/', methods=['POST'])
def create_entry():
    # if not request.json in request.json:    #or not 'timestamp' or...
    #     abort(400)
    
    dt = datetime.datetime.now()
    ts = str(dt.year) + '-' + str(dt.month)+ '-' + str(dt.day)+ '_' + str(dt.hour)+ ':' + str(dt.minute)+ ':' + str(dt.second)

    entry = {
        'timestamp': ts,
        'vehicle_id': request.json['vehicle_id']
        # 'changed_state': request.json['changed_state'],
        # 'new_state': request.json['new_state']
    }
    write_entry_to_file(entry)
    return jsonify({'entry': entry}), 201
# curl -i -H "Content-Type: application/json" -X POST -d "{"""vehicle_id""": """12345"""}" http://localhost:5000/
# curl -i -H "Content-Type: application/json" -X POST -d "{"""vehicle_id""": """12345"""}" https://blg-challenge.herokuapp.com/


@app.route('/', methods=['GET'])
def get_database():
    if os.path.exists('database.csv'):
        # with open('database.csv') as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter='\t')
        #     for row in csv_reader:
        #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #         for each value in row:    
        #             print(f'Processed {line_count} lines.')

        entries = json.dumps(list(csv.reader(open('database.csv'))))
    return entries


@app.route('/', methods=['DELETE'])
def delete_database():
    if os.path.exists('database.csv'):
        os.remove('database.csv')
    return jsonify({'result': True})
# curl -i -H "Content-Type: application/json" -X DELETE -d "" http://localhost:5000/

if __name__ == '__main__':
    app.run(debug=True) 