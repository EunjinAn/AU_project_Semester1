""" if we can install package, we write pip install package name.


2022. 09.05 Quiz
numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

do_sum =[]

for number in numbers:
    if type(number) == int:
        do_sum.append(number)
        result = sum(do_sum)
print("result:",result)""" 

import numpy as np

"""import numpy as np
x = np.random.randint(0, 10, size=(2, 3, 2))
print(x)
   
x = np.random.randint(10, size=(2, 3, 2))  # Three-dimensional array
print(x
a = np.random.randint(0, 9, size=10)
print(a)"""

import pandas as pd

# Read the file from remote
data = pd.read_json('https://admin.opendata.dk/dataset/44ecd686-5cb5-40f2-8e3f-b5e3607a55ef/resource/eeabb0f8-1b19-4c80-b059-5ba5c4c872d2/download/guidedenmarkaalborgenjson.json')
data['Address'][0]['GeoCoordinate']
[x['GeoCoordinate'] for x in data['Address']]
data['GeoCoordinate'] = [x['GeoCoordinate'] for x in data['Address']]
# drop, where no GeoCoordinate
data = data.dropna(subset=['GeoCoordinate'])

# Pull out the values
data['latitude'] = [x['Latitude'] for x in data['GeoCoordinate']]
data['longitude'] = [x['Longitude'] for x in data['GeoCoordinate']]
print(data['latitude'],data['longitude'])


        
        
        
    

