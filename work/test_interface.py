import requests


def test_requests():
    r = requests.get("https://ceshiren.com/categories.json")
    print(r.status_code)
    print(r.text)
    assert r.status_code == 200


if __name__ == '__main__':
    test_requests()
