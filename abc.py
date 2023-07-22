import requests
import json
import time


def get_numbers(urls):
    num = []
    for url in urls:
        response = requests.get(url, timeout=500)
        if response.status_code == 200:
            num.extend(json.loads(response.content)["numbers"])
        else:
            print("Skipping {url} because of status code {response.status_code}")
    return sorted(list(set(num)))


def main():
    urls = ["http://20.244.56.144/numibers/primes", "http://abc.com/fibo", "http://20.244.56.144/numbers/odd"]
    st_time = time.time()
    num = get_numbers(urls)
    print(json.dumps({"numbers": num}, indent=4))
    print(f"Time taken: {time.time() - st_time} seconds")


if __name__ == "__main__":
    main()
