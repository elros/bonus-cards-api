# python-mongo-api

## Installation

1. Install package requirements

    pip install -r requirements.txt

2. Install and run a MongoDB instance (or just use [a Docker container](https://hub.docker.com/_/mongo/) as show below)

    docker run -d -p 27017:27017 mongo

## Bonuses API

### Authorization

The Bonuses app uses [JWT](https://jwt.io) authorization. To access the API you'll need to get an authorization token. First send a JSON object with username and password to the auth URI (see example below).

Request example:

    POST /api/v1/auth
    Content-Type: application/json
    Content-Length: 49

    {"username": "alice", "password": "alice_secret"}

Response example:

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 226

    {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTE5NzA3NTUsImlhdCI6MTUwOTM3ODc1NSwibmJmIjoxNTA5Mzc4NzU1LCJpZGVudGl0eSI6IjU5ZjYyZDM1YmE0ZDEyOTlhZDI3YWM0NCJ9.56e2PCGjBbZBoqcltD94Ump7awhqsaSJPumyEsWYkvA'}

You should use the provided JWT token in subsequent requests like this:

    GET /api/v1/client/profile
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTE5NzA3NTUsImlhdCI6MTUwOTM3ODc1NSwibmJmIjoxNTA5Mzc4NzU1LCJpZGVudGl0eSI6IjU5ZjYyZDM1YmE0ZDEyOTlhZDI3YWM0NCJ9.56e2PCGjBbZBoqcltD94Ump7awhqsaSJPumyEsWYkvA

### API for clients

1. User profile

Request example:

    GET /api/v1/client/profile
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTE5NzA3NTUsImlhdCI6MTUwOTM3ODc1NSwibmJmIjoxNTA5Mzc4NzU1LCJpZGVudGl0eSI6IjU5ZjYyZDM1YmE0ZDEyOTlhZDI3YWM0NCJ9.56e2PCGjBbZBoqcltD94Ump7awhqsaSJPumyEsWYkvA

Response example:

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 81

    {"bonus_card_id": "000001", "email": "alice@localhost", "full_name": "Alice Doe"}

2. Bonus transactions list

Use `page` parameter for pagination.

Request example:

    GET /api/v1/client/bonus-transactions/
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTE5NzA3NTUsImlhdCI6MTUwOTM3ODc1NSwibmJmIjoxNTA5Mzc4NzU1LCJpZGVudGl0eSI6IjU5ZjYyZDM1YmE0ZDEyOTlhZDI3YWM0NCJ9.56e2PCGjBbZBoqcltD94Ump7awhqsaSJPumyEsWYkvA

Response example:

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 290

    {"transactions": [{"bonus_card_id": "000001", "flight_date": "2017-10-06 22:34:13.704000+00:00", "flight_from": "KRR", "flight_to": "KRR", "points": 74}, {"bonus_card_id": "000001", "flight_date": "2017-10-20 22:34:13.705000+00:00", "flight_from": "LED", "flight_to": "SVO", "points": 37}]}

### API for third-party apps

1. Create bonus transaction

Request example:

    POST /api/v1/third-party/bonus-transactions/
    Content-Type: application/json
    Content-Length: 81
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTE5NzA3NTUsImlhdCI6MTUwOTM3ODc1NSwibmJmIjoxNTA5Mzc4NzU1LCJpZGVudGl0eSI6IjU5ZjYyZDM1YmE0ZDEyOTlhZDI3YWM0NCJ9.56e2PCGjBbZBoqcltD94Ump7awhqsaSJPumyEsWYkvA

    {"bonus_card_id": "000001", "email": "alice@localhost", "full_name": "Alice Doe"}

Response example:

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 51

    {"id": "59f74e9eba4d12a1db5ac671", "success": True}

## Unit testing
To run unit tests you'll need a local MongoDB instance (e.g. [a Docker container](https://hub.docker.com/_/mongo/)). Its connection parameters should be specified in `tests/settings.py`.
