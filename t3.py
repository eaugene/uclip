import subprocess

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()


def main():
    x=getClipboardData()
    print(x)
    x=raw_input('enter data : ')
    setClipboardData(x.encode())
    x = getClipboardData()
    print(x)

if __name__== "__main__":
  main()