import requests
from datetime import datetime


def fetch_nbu_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        formatted = []
        for entry in data:
            try:
                rate = entry.get("rate")
                cc = entry.get("cc")
                txt = entry.get("txt")
                if not cc or not txt or rate is None or not isinstance(rate, (int, float)):
                    continue  # пропускаємо невалідні значення

                formatted.append({
                    "r030": entry.get("r030"),
                    "txt": entry.get("txt"),
                    "cc": entry.get("cc"),
                    "base_ccy": "UAH",
                    "rate": entry.get("rate"),
                    "exchangedate": datetime.strptime(entry.get("exchangedate"), "%d.%m.%Y").date().isoformat()
                })
            except Exception as e:
                print(f'Помилка при обробці елемента: {e}')
        return formatted
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


if __name__ == "__main__":
    exchange_rates = fetch_nbu_exchange_rates()
