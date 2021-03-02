#!/usr/bin/python
import webbrowser


phrase=input("Key phrase:")
filepath = "urls.txt"
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}:{}".format(cnt,line.strip()))
        webbrowser.open('https://tinyurl.com/create.php?source=indexpage&url={}&alias={}{}'.format(line,phrase,cnt))
        line = fp.readline()
        cnt+=1
