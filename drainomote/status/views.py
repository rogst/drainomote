from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time
from .kemp import KempLB
from .models import Realserver, Realserver_Group_Permissions
# Create your views here.


@login_required
def index(request):
    user = request.user
    groups = user.groups.all()

    lb = KempLB("https", "drainomote", "bXDizv1SfERUcILsF7ko", "10.0.16.20")
    realserver_info = lb.get_realservers()

    realservers = []
    for group in groups:
        rows = Realserver_Group_Permissions.objects.filter(group=group)
        for row in rows:
            rs = {}
            rs["ip"] = row.realserver.ip
            rs["name"] = row.realserver.name
            rs["status"] = realserver_info[row.realserver.ip]["status"]
            rs["activeconns"] = \
                realserver_info[row.realserver.ip]["activeconns"]
            rs["persist"] = realserver_info[row.realserver.ip]["persist"]
            rs["connspersec"] = \
                realserver_info[row.realserver.ip]["connspersec"]
            realservers.append(rs)

    return render(request, "status/index.html", {"realservers": realservers})


@login_required
def me(request):
    user = request.user
    groups = user.groups.all()
    realservers = []
    for group in groups:
        rows = Realserver_Group_Permissions.objects.filter(group=group)
        for row in rows:
            realservers.append(row.realserver.name)

    return render(request, "status/me.html",
                  {"groups": groups, "realservers": realservers})


@login_required
def disable(request, rs_ip):
    user = request.user
    groups = user.groups.all()
    realservers = []
    for group in groups:
        rows = Realserver_Group_Permissions.objects.filter(group=group)
        for row in rows:
            realservers.append(row.realserver.ip)

    if rs_ip in realservers:
        lb = KempLB("https",
                    "drainomote",
                    "bXDizv1SfERUcILsF7ko",
                    "10.0.16.20")
        lb.disable_realserver(rs_ip)

    time.sleep(3)
    return redirect("status:index")


@login_required
def enable(request, rs_ip):
    user = request.user
    groups = user.groups.all()
    realservers = []
    for group in groups:
        rows = Realserver_Group_Permissions.objects.filter(group=group)
        for row in rows:
            realservers.append(row.realserver.ip)

    if rs_ip in realservers:
        lb = KempLB("https",
                    "drainomote",
                    "bXDizv1SfERUcILsF7ko",
                    "10.0.16.20")
        lb.enable_realserver(rs_ip)

    time.sleep(2)
    return redirect("status:index")
