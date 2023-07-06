import requests
from datetime import datetime
import jwt
from flask import Flask, request, jsonify
import config
import uuid
import time


app = Flask(__name__)
request_counter = 0
start_time = time.time()


@app.before_request
def number_of_request():
    global request_counter
    request_counter += 1


@app.route("/proxy", methods=["POST"])
async def proxy_request():
    """Proxy view function. Takes a Post request from client and makes a Post request to upstream
    server(dummy website).

    Returns:
        response: Returns an HTTP Response (Here a dummy response)
    """
    data = await get_request_data()
    jwt_token = create_jwt_token(data)
    headers = {"x-my-jwt": jwt_token, "Content-Type": "application/json"}
    response = send_request(config.url, data=data, headers=headers)
    response = config.sample_response
    return jsonify(response)


@app.route("/status")
def status():
    """View function to provide the number of requests processed and time from start.

    Returns:
        Returns an HTTP Response with number_of_requests and elapsed_time
    """
    number_of_requests = request_counter
    elapsed_time = time.time() - start_time
    response = {
        "number_of_requests_processed": number_of_requests,
        "time_from_start": elapsed_time,
    }
    return jsonify(response)


async def get_request_data():
    """Gets the Client's request data.

    Returns:
        Returns the request data.
    """
    request_data = request.get_json()
    return request_data


def create_jwt_token(data):
    """Creates a jwt signed token

    Args:
        data (json/dict): Takes the request data coming from the client.

    Returns:
        Returns the encoded jwt token.
    """
    current_time = datetime.now()
    today_date = current_time.date()
    payload = {
        "username": data["username"],
        "date": str(today_date),
        "iat": str(current_time.timestamp),
        "jti": str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, config.secret_key, algorithm="HS512")
    return jwt_token


def send_request(url, data, headers):
    """Sends Post request to the upstream server.

    Args:
        url (str): Url of the upstream server
        data (json): Data coming from the client
        headers (dict): Request Headers

    Returns:
        Returns the HTTP Response.
    """
    response = requests.post(url, json=data, headers=headers)
    return response


if __name__ == "__main__":
    app.run()
