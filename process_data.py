# process CSV file
# formatted lat,long,z

import csv, sys

output = open('data.js', 'w')

with open('test.csv', 'r') as csvfile:
    latitude = 0
    longitude = 0
    max_accel = 0
    count = 0
    reader = csv.reader(csvfile, delimiter=',')
    output.write('var latitude = []; var longitude = []; var accel = [];')
    for row in reader:
        print ', '.join(row)
        lat = row[0][:10]
        long = row[1][:10]
        if( lat == latitude and long == longitude ):
            if max_accel < row[2] and max_accel < 150:
                 max_accel = row[2]
        else:
            output.write('latitude[%s] = %s; longitude[%s] = %s; accel[%s] = %s;' % (count, lat, count, long, count, max_accel))
            count = count + 1
            latitude = lat
            longitude = long
            max_accel = row[2]

            
            
        
