GET-запрос от service1 для получения данных:
Invoke-WebRequest -Uri "http://localhost:5000/send-data" -Method POST

PUT-запрос для обновления данных:
Invoke-WebRequest -Uri "http://localhost:5000/items" -Method GET

Если тебе нужно добавить новый товар:
Invoke-WebRequest -Uri "http://localhost:5000/items" -Method POST -Body '{"name": "Example item"}' -Headers @{"Content-Type"="application/json"}

DELETE-запрос для удаления элемента:
Invoke-WebRequest -Uri "http://localhost:5000/items/0" -Method DELETE
