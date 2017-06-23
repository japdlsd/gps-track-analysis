#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET
import logging
from pprint import pprint, pformat
import datetime
import re

def parseGpx2Csv(gpx_filename, csv_filename):
    logging.debug("gpx_filename: {}".format(gpx_filename))
    tree = ET.parse(gpx_filename)
    root = tree.getroot()

    out_file = open(csv_filename, "w")
    print("lat,lon,ele,t,timestamp,tracknum", file=out_file)

    timeregex = re.compile("(\d*)-(\d*)-(\d*)T(\d*):(\d*):(\d*)Z")

    for num, track in enumerate(root):
        if track.tag.find("trk") == -1: continue
        trkseg = track[1]
        for point in trkseg:
            lat = point.attrib["lat"]
            lon = point.attrib["lon"]
            ele = point[0].text
            ts = point[1].text
            # 2008 - 10 - 09 T 16 : 15 : 24 Z
            # 0123 4 56 7 89 0 12 3 45 6 78 9
            t = datetime.datetime(*[int(x) for x in timeregex.match(ts).group(*range(1,7))])
            print(",".join([lat,lon,ele,str(t.timestamp()),ts,str(num)]), file=out_file)
    out_file.close()

def main():
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) != 3:
        logging.error("WRONG ARGUMENT COUNT")
        exit(1)

    gpx_filename, csv_filename = sys.argv[1:]

    parseGpx2Csv(gpx_filename, csv_filename)
    

if __name__ == "__main__":
    main()