import os
import requests
import time

AREAS = [
    '18VR22',
    '18VR31',
    '18VR32',
    '18VR42',
    '18VR52',
    '18VR53',
    '18VR62',
    '18VR63',
]

URL = 'http://www.butterfly.ontarioinsects.org/ontbutterflyatlas/SQL.php?starting=1333&type=recordsAll&sp=all&area=squares&order=date&spIndex=0&areaID=%s&areaName='

try:
    os.mkdir('data')
except:
    pass

for area in AREAS:
    print('Fetching data for area: %s' % area)
    r = requests.get(URL % area)
    if r.status_code != 200:
        print('error: status code: %s' % r.status_code)
        break
    with open(os.path.join('data', '%s.html' % area), 'wb') as f:
        f.write(r.text.encode('utf-8'))
        time.sleep(10)
