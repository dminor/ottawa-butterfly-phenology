from bs4 import BeautifulSoup
import glob
import os
import re

MONTHS = [
    '_', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

with open(os.path.join('data', 'butterflies.txt'), 'wb') as o:
    for fname in glob.glob(os.path.join('data', '*.html')):
        print('Extracting butterflies from: %s' % fname)
        with open(fname, encoding='ISO-8859-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            record = []
            for td in soup.find_all('td'):
                record.append(td.text.strip())
                m = re.match('(\d\d\d\d)(\d\d)(\d\d)', td.text)
                if m:
                    y, m, d = map(int, m.groups())
                    if y > 1700 and m <= 12 and d <= 31:
                        month = MONTHS[m]
                        for i, r in enumerate(record):
                            if r == month:
                                o.write('|'.join(record[i:]).encode('utf-8'))
                                o.write('\n'.encode('utf-8'))
                        record = []
