import http.client
import json
import winsound
import time
from datetime import datetime

print("-------------------Start---------------------------")
while True :
    start_t = datetime.now()
    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = ''
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Origin': 'https://www.cowin.gov.in',
      'DNT': '1',
      'Connection': 'keep-alive',
      'Referer': 'https://www.cowin.gov.in/',
      'TE': 'Trailers'
    }
    conn.request("GET", "/api/v2/appointment/sessions/public/calendarByDistrict?district_id=371&date=07-05-2021", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("**** HTTP status code: "+ str(res.status) + "  **********************"+  str(start_t))
    decoded = data.decode("utf-8")
    #print(decoded)
    jsonData = json.loads(decoded)
    centers = jsonData["centers"]
    #print("---------------------------------------------------")
    for center in centers:
        pin = center['pincode']
        sessions = center['sessions']
        for session in sessions:
            age_l = session['min_age_limit']
            cap = session['available_capacity']
            if age_l > 15 and age_l < 44 and pin < 416100 and pin > 416000 and cap > 0 :
                print(".....................................................")
                print("address: "+ center['address'])
                print(pin)
                print(session)
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
                winsound.PlaySound("*", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                winsound.Beep(1000,500)
    conn.close()
    time.sleep(10)
    end_t = datetime.now()
    print("************ End Time "+str(end_t) + "  time taken:" + str(end_t-start_t))
    print()
print("--------------------End----------------------------")


#curl "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=371&date=08-05-2021"
