# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:09:43 2015

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
    businfo = json.loads(request.read(request))
    busesdata = businfo["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    print "Bus Line :  %s" % (str(sys.argv[2]))
    print "Numbers of Active Buses: %s" % (str(len(busesdata)))
    for buses  in busesdata:
        longitude_bus = buses["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        latitude_bus = buses["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        print "Bus %s is at %s latitude and %s longitude" % (str(buscount), str(latitude_bus), str(longitude_bus))
        buscount += 1

