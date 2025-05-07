import requests
from datetime import datetime
from scripts.save_rates_to_postgres_local import save_rates_to_postgres_local


def fetch_historical_rates(start_date: str, end_date: str) -> list:
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&sort=exchangedate&order=desc&json"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Помилка запиту до API: {response.status_code}")

    data = response.json()
    formatted = []

    for entry in data:
        try:
            if not all(k in entry for k in ("r030", "cc", "txt", "rate", "exchangedate")):
                continue
            rate_val = entry.get("rate")
            if rate_val is None or not isinstance(rate_val, (int, float, str)):
                continue

            formatted.append({
                "r030": entry["r030"],
                "cc": entry["cc"],
                "txt": entry["txt"],
                "base_ccy": "UAH",
                "rate": float(rate_val),
                "exchangedate": datetime.strptime(entry["exchangedate"], "%d.%m.%Y").date().isoformat()
            })
        except Exception as e:
            print(f"[!] Помилка обробки елемента: {e}")
    return formatted


if __name__ == "__main__":
    # вкажи потрібні дати тут
    start_date = "20240101"
    end_date = "20250330"

    rates = fetch_historical_rates(start_date, end_date)
    print(f"Отримано записів: {len(rates)}")

    save_rates_to_postgres_local(rates)
    print("✅ Дані збережено в PostgreSQL")
