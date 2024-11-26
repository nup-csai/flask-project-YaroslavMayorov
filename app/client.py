import requests


def check_root_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Запрос успешен, код 200.")
            print(response)
            print(response.json())
        else:
            print(response.status_code)
            exit(-1)
    except requests.RequestException as e:
        exit(-1)


check_root_url("http://localhost:8080/")
check_root_url("http://localhost:8080/k")