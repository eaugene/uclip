import re, uuid
import requests
import json
import sqlite3


def cls():
    conn = sqlite3.connect('ky.db')
    x='n-o'
    eau = conn.execute('''select mky from ky;''')
    for t in eau:
        x = t[0]
    f = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    response = requests.get("https://univclip.herokuapp.com/end?key=" + str(x) + "&mac=" + f)
    j = json.loads(response.content)
    if j['code'] == '143':
        conn.execute('''DROP TABLE ky''')
        print('session closed successfully')
    elif j['message'] == 'no data to delete':
        conn.execute('''DROP TABLE ky''')
        print('session closed successfuly')
    else:
        print(str(j['message']))
        print('end session failed')
    conn.close()


def main():
    conn = sqlite3.connect('ky.db')
    cursor = conn.execute('''SELECT count(name) FROM sqlite_master WHERE name='ky' AND type='table';''')
    for x in cursor:
        pr = x[0]
    if pr > 0:
        conn.close()
        cls()
    else:
        conn.close()
        print('NO key exists to end sharing session.')


if __name__ == "__main__":
    main()