#!/bin/bash

if ! [ -d parsed_data ]; then
    mkdir parsed_data
fi

for track in raw_data/gpsdata/*.gpx; do
    out=`basename "$track"`
    python3 parse_gps_track.py "$track" "parsed_data/$out.csv"
done