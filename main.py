import requests

url = "https://www.maxjeune-tgvinoui.sncf/api/public/refdata/search-freeplaces-proposals"

params = {
    "destination": "FRMLT",
    "origin": "FRPLY",
    "departureDateTime": "2025-01-31T01:00:00.000Z"
}

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.maxjeune-tgvinoui.sncf"
})

response = session.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Données récupérées :")
    print(data)
else:
    print(f"Erreur : {response.status_code}")
    print(response.text)
    print(response.headers)