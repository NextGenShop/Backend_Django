# Backend_Django
 
Apis available:
 POST: http://127.0.0.1:8000/product/ 
 
 GET http://127.0.0.1:8000/product/ Available paramater: query=, retailer=, limit=

 GET http://127.0.0.1:8000/basket/{ShopperId}
 
 PUT http://127.0.0.1:8000/basket/{ShopperId} Info required in Json: {"items":[{"ProductId": example id, "quantity": example number}]}
 
 DELETE http://127.0.0.1:8000/basket/{ShopperId}

# How to run

    make build
    make run
    
    
# Command to add mock data to sqlite db

    python manage.py loaddata MockSupermarketDataset.json
