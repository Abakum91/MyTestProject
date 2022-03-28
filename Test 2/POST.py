import requests

website = 'https://jsonplaceholder.typicode.com/posts'
respons = requests.post(website, json={

    "userId": 13,
    "tittle": "Shalom friends!!11",
    "body": "text TEXT TEXT BODY"

})
print(respons.text)