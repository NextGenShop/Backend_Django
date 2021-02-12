# Backend_Django

Apis available:

POST: http://127.0.0.1:8000/product/

GET http://127.0.0.1:8000/product/ Available parameters: query=, retailer=, limit=

GET http://127.0.0.1:8000/basket/{ShopperId}

PUT http://127.0.0.1:8000/basket/{ShopperId} Info required in Json: {"items":[{"ProductId": example id, "quantity": example number}]}

DELETE http://127.0.0.1:8000/basket/{ShopperId}

IBM Watson Tokens:
GET http://127.0.0.1:8000/tokens/speech-to-text
GET http://127.0.0.1:8000/tokens/text-to-speech

# Setup

1. Rename .env-sample to .env
2. Enter the SECRET_KEY value inside the .env file

# How to run

    make build
    make run

# Command to add mock data to sqlite db

    python manage.py loaddata MockSupermarketDataset.json
