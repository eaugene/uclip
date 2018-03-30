import re, uuid
import requests
import json
import sqlite3
import subprocess

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def rcv():
    conn = sqlite3.connect('ky.db')
    x='n-o'
    eau = conn.execute('''select mky from ky;''')
    for t in eau:
        x = t[0]
    y = '\<some error\>'
    response = requests.get("https://univclip.herokuapp.com/down?key=" + str(x))
    j = json.loads(response.content)
    if j['code'] == '143':
        y = str(j['data'])
        setClipboardData(y.encode())
    else:
        print('DOWN data failed')
    conn.close()


def main():
    conn = sqlite3.connect('ky.db')
    cursor = conn.execute('''SELECT count(name) FROM sqlite_master WHERE name='ky' AND type='table';''')
    for x in cursor:
        pr = x[0]
    if pr > 0:
        conn.close()
        rcv()
    else:
        conn.close()
        print('NO key exists . Register and then try')


if __name__ == "__main__":
    main()