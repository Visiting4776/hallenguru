from typing import List
import requests
from datetime import datetime
from bs4 import BeautifulSoup

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