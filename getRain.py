import requests, json
import pandas as pd
import urllib

years = [2018]#, 2016, 2017, 2018]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

weather = {}

for y in years:
    year = str(y)
    weather[year] = {}

    for m in months:
        month = '0'+str(m) if len(str(m)) == 1 else str(m)
        weather[year][month] = {}

        for d in days:
            day = '0'+str(d) if len(str(d)) == 1 else str(d)
            weather[year][month][day] = {}

            params = {  'n': 'spain/barcelona',
                        'mode': 'historic',
                        'hd': str(y)+month+day,
                        'month': month,
                        'year': y,
                        'json': 1  }
            # r = requests.get('https://www.timeanddate.com/scripts/cityajax.php', params=params)
            # print(r.url)

            urlPage = 'https://www.timeanddate.com/scripts/cityajax.php?n=spain/barcelona&mode=historic&hd=20180101&month=01&year=2018&json=1'
            # r = urllib.request.urlopen(urlPage)
            # r = urllib.request.urlopen(
                # 'https://www.timeanddate.com/scripts/cityajax.php?n=spain/barcelona&mode=historic&hd=' + str(y)+month+day + '&month=' + month
                # + '&year=' + year + '&json=1')
            # dataFrame = pd.DataFrame.from_dict(r.text, orient='columns')
            
            with urllib.request.urlopen(urlPage) as url:
                data = json.loads(url.read().decode())
                print(data)

            break

            if r.status_code == 200:
                for t in r.json():
                    if len(t['c'][0]['h']) > 5:
                        hour = t['c'][0]['h'][0:3]
                    else:
                        hour = t['c'][0]['h']
                    
                    tiempo = t['c'][3]['h']
                    weather[year][month][day][hour] = (tiempo.lower.find('rain') != -1 or tiempo.lower.find('thunder') != -1 or tiempo.lower.find('shower') != -1) 
                        
            else:
                print('Error on ' + day + '/' + month + '/' + year)

with open('rainData.json', 'w') as outFile:
    json.dump(weather, outFile)
