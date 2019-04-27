import reverse_geocoder as rg
import mysql.connector as mysql

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

database = mysql.connect(user='root',
                         password='cornisgood',
                         host='192.168.1.11',
                         database='ufo_sightings')

cursor = database.cursor()

cursor.execute('SELECT * FROM origcsv')
results = cursor.fetchall()

sqlupdateUS = '''UPDATE origcsv SET sighting_city = %s, sighting_state = %s, sighting_country = %s WHERE sighting_id = %s'''
sqlupdateNONUS = '''UPDATE origcsv SET sighting_city = %s,sighting_state = '', sighting_country = %s WHERE sighting_id = %s'''

count = 0
for result in results:
    locationdata = rg.get(result[9:],mode=1)
    if locationdata['cc'] == 'US':
        data = (
            locationdata['name'],
            us_state_abbrev.get(locationdata['admin1']),
            locationdata['cc'],
            result[0])
        cursor.execute(sqlupdateUS,data)
        database.commit()
        print(count)
        count += 1
    else:
        data = (
            locationdata['name'],
            locationdata['cc'],
            result[0]
        )
        cursor.execute(sqlupdateNONUS, data)
        database.commit()
        print(count)
        count += 1

print(count)