import requests
import boto3
from flask import Flask


def http_callout():
    print("Client Lambda - HTTP Callout Begin")
    x = requests.get('https://www.facebook.com/')
    # x = requests.put('https://httpbin.org/put', data={'key': 'value'})
    # x = requests.post('https://www.w3schools.com/python/demopage.php', data={'key': 'value'})
    # x = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
    print("Client Lambda - HTTP Callout End")


def first():
    print("Client Lambda - First Function")


def second():
    print("Client Lambda - Second Function")


def db_callout():
    print("Client Lambda - DB Callout Begin")
    client = boto3.client('dynamodb')
    print("client METHODS FOR THIS SESSION::", dir(client))
    data = client.scan(TableName='Person')
    item = {
        "id": {"N": "556"},
        "address": {"S": "United States"},
        "firstName": {"S": "John"},
        "lastName": {"S": "Doe"},
        "age": {"N": "30"}
    }
    response = client.put_item(TableName='Person', Item=item)
    print("Client Lambda - DB Call out Begin")


def flask_wsgi():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run(port=6063)