import re, uuid
import requests
import json
import sqlite3


def nxt():
        conn = sqlite3.connect('ky.db')
        k = raw_input("Enter the key : ")
        print("you have entered : " + k)
        response = requests.get("https://univclip.herokuapp.com/verify?key=" + k)
        j = json.loads(response.content)
        if j['code'] == '143':
                frm="INSERT INTO ky (mky) VALUES ("+k+");"
                conn.execute(frm)
                eau = conn.execute('''select mky from ky;''')
                for t in eau:
                        print(str(t[0])+'ok')
                conn.commit()
        else:
                print('key verification failed')
                cursor = conn.execute('''SELECT count(name) FROM sqlite_master WHERE name='ky' AND type='table';''')
                for x in cursor:
                        pr = x[0]
                if pr > 0:
                        conn.execute('''DROP TABLE ky''')
        conn.close()


def main():
        conn = sqlite3.connect('ky.db')
        cursor=conn.execute('''SELECT count(name) FROM sqlite_master WHERE name='ky' AND type='table';''')
        for x in cursor:
                pr=x[0]
        if pr > 0:
                print('ALREADY KEY EXISTS , ENTER Y TO REMOVE THAT')
                op=raw_input('ENTER OPTION Y - REMOVE , N - NO : ')
                if op == 'Y' or op == 'y':
                        conn.execute('''DROP TABLE ky;''')
                        conn.execute('''CREATE TABLE ky (mky INT PRIMARY KEY NOT NULL);''');
                        conn.close()
                        nxt()
                else:
                        print('registration failed')
                        conn.close()
        else:
                conn.execute('''CREATE TABLE ky (mky INT PRIMARY KEY NOT NULL);''');
                conn.close()
                nxt()


if __name__== "__main__":
  main()


