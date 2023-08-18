import requests

def get_latest_bitcoin_rate():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "bitcoin" in data and "usd" in data["bitcoin"]:
        return data["bitcoin"]["usd"]
    else:
        return None

latest_bitcoin_rate = get_latest_bitcoin_rate()

if latest_bitcoin_rate is not None:
    print(f"Latest Bitcoin rate: ${latest_bitcoin_rate:.2f}")
else:
    print("Failed to retrieve the latest Bitcoin rate.")

