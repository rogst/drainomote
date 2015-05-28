import requests
import xml.etree.ElementTree as ET
from django.conf import settings


class Kemp():
    def __init__(self, loadbalancer="default"):
        url_format = "{protocol}://{username}:{password}@{hostname}:{port}"
        kemp = settings.KEMPLM[loadbalancer]
        self.username = kemp["USER"]
        self.password = kemp["PASSWORD"]
        self.protocol = kemp["PROTO"]
        self.hostname = kemp["HOST"]
        self.port = kemp["PORT"]
        self.service_uri = \
            url_format.format(protocol=self.protocol,
                              username=self.username,
                              password=self.password,
                              hostname=self.hostname,
                              port=self.port)

    def get_realservers(self):
        r = requests.get("{0}/access/stats".format(self.service_uri),
                         verify=False)
        xml_root = ET.fromstring(r.text)

        realservers = {}
        for rs in xml_root[0][0].iter('Rs'):
            addr = rs.find("Addr").text
            enabled = rs.find("Enable").text
            activeconns = rs.find("ActivConns").text
            persist = rs.find("Persist").text
            connspersec = rs.find("ConnsPerSec").text

            if addr in realservers.keys():
                if realservers[addr]["status"] == "enabled" or enabled == "1":
                    realservers[addr]["status"] = "enabled"
                else:
                    realservers[addr]["status"] = "disabled"

                realservers[addr]["activeconns"] = \
                    int(realservers[addr]["activeconns"]) + int(activeconns)
                realservers[addr]["persist"] = \
                    int(realservers[addr]["persist"]) + int(persist)
                realservers[addr]["connspersec"] = \
                    int(realservers[addr]["connspersec"]) + int(connspersec)
            else:
                realservers[addr] = {}
                realservers[addr]["status"] = \
                    "enabled" if enabled == "1" else "disabled"
                realservers[addr]["activeconns"] = activeconns
                realservers[addr]["persist"] = persist
                realservers[addr]["connspersec"] = connspersec

        return realservers

    def disable_realserver(self, rs_ip):
        r = requests.get("{0}/access/disablers?rs={1}".format(
            self.service_uri,
            rs_ip), verify=False)
        print(r.text)

    def enable_realserver(self, rs_ip):
        r = requests.get("{0}/access/enablers?rs={1}".format(
            self.service_uri,
            rs_ip), verify=False)
        print(r.text)
