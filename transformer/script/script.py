import requests
import sys
import json

$

if __name__ == "__main__":
    data = sys.argv[1]
    data = json.loads(data)
    res = main(data)
    requests.post("http://127.0.0.1:6121/callback", json={"id": ">", "data": res})
