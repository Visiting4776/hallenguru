from typing import List
import requests
from datetime import datetime
from bs4 import BeautifulSoup

baths = {
1: "Stadtbad Mitte",
# 2: "Schwimmhalle Fischerinsel",
# 7: "Sommerbad Humboldthain",
# 9: "Kombibad Seestraße (Halle)",
# 11: "Schwimmhalle Thomas-Mann-Straße",
# 15: "Wellenbad am Spreewaldplatz",
# 17: "Sommerbad Kreuzberg",
# 18: "Stadtbad Schöneberg",
# 19: "Sport - und Lehrschwimmhalle Schöneberg",
# 21: "Stadtbad Charlottenburg \"Alte Halle\"",
# 24: "Sommerbad Olympiastadion",
# 26: "Stadtbad Spandau Nord",
# 27: "Sommerbad Staaken",
# 28: "Kombibad Spandau Süd (Halle)",
# 29: "Stadtbad Wilmersdorf 1",
# 30: "Stadtbad Wilmersdorf 2",
# 31: "Sommerbad Wilmersdorf",
# 34: "Schwimmhalle Hüttenweg",
# 38: "Stadtbad Märkisches Viertel",
# 42: "Stadtbad Lankwitz",
# 43: "Schwimmhalle Finckensteinallee",
# 45: "Sommerbad Insulaner",
# 46: "Stadtbad Tempelhof",
# 47: "Kombibad Mariendorf (Halle)",
# 48: "Sommerbad Mariendorf (Rixdorfer Straße)",
# 49: "Stadtbad Neukölln",
# 51: "Sommerbad Neukölln",
# 52: "Kombibad Gropiusstadt (Halle)",
# 54: "Schwimmhalle Baumschulenweg",
# 60: "Kleine Schwimmhalle Wuhlheide",
# 61: "Schwimmhalle Allendeviertel",
# 62: "Sommerbad Wuhlheide",
# 64: "Schwimmhalle Sewanstraße",
# 68: "Schwimmhalle Buch",
# 70: "Sommerbad Pankow",
# 71: "Schwimmhalle Helene-Weigel-Platz",
# 74: "Schwimmhalle Zingster Straße",
# 76: "Schwimmhalle Kaulsdorf",
# 79: "Schwimm- und Sprunghalle im Europasportpark",
# 81: "Schwimmhalle Kreuzberg",
}

def get_slot_info(bath_id: int, year: int, month: int) -> List:
    url = f'https://pretix.eu/Baeder/{bath_id}/?date={year}-{month:02}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    events = []
    for event in soup.find_all('a', class_='event'):
        state = event['class'][-1]

        if state == 'over': 
            continue
        
        time_obj = event.find('span', class_='event-time')
        date = datetime.fromisoformat(time_obj['data-time'])
        times = [t.text for t in time_obj.find_all('time')]
        from_date = (
            event.find('span', class_='event-status').text.strip().split()[-1] 
            if state == 'soon' else '' )
        
        events.append({
            'bath_id': bath_id,
            'date': date.date(), #only date
            'start_time': times[0],
            'end_time': times[1],
            'state': state,
            'from_date': from_date
        })
    return events