from django.shortcuts import render
from datetime import datetime
import os


# Create your views here.


def hello(request):
    return render(request, "hello.html")


def msgproc(request):
    datalist = []
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fname = cwd + "/cloudMessage/templates/" + "msgdata.txt"
    print("fname =", fname)
    if request.method == 'POST':
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open(fname, 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA,
                                                msg, time.strftime('%Y-%m-%d %H:%M:%S')))
    if request.method == 'GET':
        userC = request.GET.get("userC", None)
        if userC != None:
            with open(fname, 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split("--")
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "msg.html", {"data": datalist})
