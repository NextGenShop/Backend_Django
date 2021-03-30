# Backend_Django

Local URL: http://127.00.1

Default PORT: 8000

## APIs available:

POST **/product**

GET **/product** Available parameters: query=, retailer=, limit=

GET **/basket/{ShopperId}**

PUT **/basket/{ShopperId}** Info required in JSON: {"items":[{"ProductId": example id, "quantity": example number}]}

DELETE **/basket/{ShopperId}**

## IBM Watson Tokens:
GET /tokens/speech-to-text

GET /tokens/text-to-speech

# Setup

1. Rename .env-sample to .env
2. Enter the SECRET_KEY value inside the .env file

# How to run

    make build
    make run

# Command to add mock data to sqlite db

    python manage.py loaddata MockSupermarketDataset.json
