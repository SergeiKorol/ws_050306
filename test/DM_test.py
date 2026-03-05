import requests

def test_dm():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed":True }
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    x = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    response_body = x.json()
    assert response_body['completed'] == True