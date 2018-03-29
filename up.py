import re, uuid
import requests
import json
import sqlite3
import subprocess


def getClipboardData():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def snd():
    conn = sqlite3.connect('ky.db')
    x='n-o'
    eau = conn.execute('''select mky from ky;''')
    for t in eau:
        x = t[0]
    y = '\<some error\>'
    y = getClipboardData()
    response = requests.get("https://univclip.herokuapp.com/up?key=" + str(x)+ "&data=" + str(y))
    j = json.loads(response.content)
    if j['code'] == '143':
        print('UP data successfull')
    else:
        print('UP data failed')
    conn.close()


def main():
    conn = sqlite3.connect('ky.db')
    cursor = conn.execute('''SELECT count(name) FROM sqlite_master WHERE name='ky' AND type='table';''')
    for x in cursor:
        pr = x[0]
    if pr > 0:
        conn.close()
        snd()
    else:
        conn.close()
        print('NO key exists . Register and then try')


if __name__ == "__main__":
    main()
