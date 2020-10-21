import requests


def query_presidents():
    url_ddg = "https://api.duckduckgo.com"

    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")

    rsp_data = resp.json()

    return str(rsp_data)


def main():
    print(query_presidents())


if __name__ == "__main__":
    main()
