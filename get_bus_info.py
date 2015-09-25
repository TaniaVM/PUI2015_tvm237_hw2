# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:46:36 2015

@author: tania
"""

__author__ = 'tvm'
import csv
import json
import sys
import urllib2

if __name__=='__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (str(sys.argv[1]), str(sys.argv[2]))
    buscount=0
    request = urllib2.urlopen(url)
    busdata = json.loads(request.read(request))
    busesdata = busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    with open(str(sys.argv[3]), 'wb') as fileb:
           wtr = csv.writer(fileb)
           wtr.writerow(["Latitude","Longitude","Stop Name", "Stop status"])
           for buses  in busesdata:
                latitude_bus = buses["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
                longitude_bus = buses["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
                stopstatus = "N/A"
                stopname = "N/A"
                for Stopinfo in buses["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]:
                    stopstatus = Stopinfo["Extensions"]["Distances"]["PresentableDistance"]
                    stopname = Stopinfo["StopPointName"] 
                    if stopstatus == "approaching" or stopstatus == "1 stop away" or stopstatus == "< 1 stop away" or stopstatus == "at stop":
                        wtr.writerow([latitude_bus,longitude_bus,stopname,stopstatus])
                if len(buses["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]) == 0:
                    wtr.writerow([latitude_bus,longitude_bus,stopname,stopstatus])
                buscount += 1

   

