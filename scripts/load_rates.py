import requests
import json
from datetime import datetime


def fetch_nbu_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        formatted = []
        for entry in data:
            formatted.append({
                "r030": entry.get("r030"),
                "txt": entry.get("txt"),
                "cc": entry.get("cc"),
                "base_ccy": "UAH",
                "rate": entry.get("rate"),
                "exchangedate": datetime.strptime(entry.get("exchangedate"), "%d.%m.%Y").date().isoformat()
            })
        return formatted
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


if __name__ == "__main__":
    exchange_rates = fetch_nbu_exchange_rates()
    print(json.dumps(exchange_rates, indent=2, ensure_ascii=False))
