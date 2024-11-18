#!/bin/bash

awk -F’,’ '{ if ($1 == "") $1 = "NA"; print $0 }' OFS=‘,’ AB_NYC_2019.csv > AB_NYC_2019_1.csv
awk -F, '{ for (i = 1; i <= NF; i++) if ($i == "") next; print $0 }' AB_NYC_2019_1.csv > AB_NYC_2019.csv

sort -t’,’ -k1 AB_NYC_2019.csv | uniq > AB_NYC_2019_1.csv 

mean_value=$(awk -F',' '{sum += $11; count++} END {print sum/count}' AB_NYC_2019_1.csv)
awk -F',' -v mean="$mean_value" '{ if ($11 < mean * 1.75 && $11 > mean * 0.25) print $0 }' OFS=',' AB_NYC_2019_1.csv > AB_NYC_2019.csv


rm AB_NYC_2019_1.csv


