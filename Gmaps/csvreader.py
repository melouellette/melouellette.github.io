import csv

fo = open("C:/GEOM99/Week1_2/melouellette.github.io/Gmaps/data/ProvincalParksSmall.csv", 'r')
freader = csv.reader(fo)
next(freader)
#append each line to the proper list
for row in freader:
    line = row.split(",")
    lat = float(line[1])
    lon = float(line[2])
    print("{ lat:", lat, ", lng:", lon, "},")
fo.close()
