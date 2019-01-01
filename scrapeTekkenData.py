from bs4 import BeautifulSoup
import urllib.request as request
import pandas as pd
import json
soup = BeautifulSoup


all_characters = ['akuma', 'alisa', 'anna','armor-king','asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov', 'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie',
                  'katarina', 'kazumi', 'kazuya', 'king', 'kuma', 'lars','lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe','marduk', 'master-raven', 'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']

for char in all_characters:
    webPage = "http://rbnorway.org/" + char + "-t7-frames/"
    page = request.urlopen(webPage)
    soup = BeautifulSoup(page, 'html.parser')

    # special moves
    print("Scraping : ", char , " special moves")
    tables = soup.find_all('table')
    table = tables[0]
    rows = table.find_all('tr')
    first_row = rows[0].find_all('td')
    keys = [ele.text.strip() for ele in first_row]
    char_fdata = {}
    for key in keys:
        char_fdata[key] = []
    for row in rows[1:]:
        elements = row.find_all('td')
        for i in range(len(keys)):
            if( i >=len(elements)):
                char_fdata[keys[i]].append("")
            else:
                char_fdata[keys[i]].append(elements[i].text.strip())

    df = pd.DataFrame.from_dict(char_fdata)
    json_file = pd.DataFrame.to_json(df,orient='index')
    parsed = json.loads(json_file)
    with open('tekken7Data/'+char+'-special.json', 'w') as outfile:
        json.dump(parsed, outfile, indent = 4, sort_keys = False)


    # basic moves
    print("Scraping : ", char , " basic moves")
    if(len(tables) < 2):
        continue
    table = tables[1]
    rows = table.find_all('tr')
    first_row = rows[0].find_all('td')
    keys = [ele.text.strip() for ele in first_row]
    char_fdata = {}
    for key in keys:
        char_fdata[key] = []
    for row in rows[1:]:
        elements = row.find_all('td')
        for i in range(len(keys)):
            char_fdata[keys[i]].append(elements[i].text.strip())

    df = pd.DataFrame.from_dict(char_fdata)
    json_file = pd.DataFrame.to_json(df, orient='index')
    parsed = json.loads(json_file)
    with open('tekken7Data/'+char+'-basic.json', 'w') as outfile:
        json.dump(parsed, outfile, indent = 4, sort_keys = False)

