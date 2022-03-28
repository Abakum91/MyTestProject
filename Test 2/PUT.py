import requests

website = 'https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(website).json())

respons = requests.put(website, json={

    "userId": 13,
    "tittle": "Shalom friends!!11",
    "body": "text TEXT TEXT BODY"

})
print(respons.json())