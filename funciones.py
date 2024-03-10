
import pandas as pd


def json_to_dataframe(data_entrada):
    elements = data_entrada['elements']
    places = {'lat': [], 'lon': [], 'name': [], 'address': []}

    for i in elements:
        lalitude = i['lat']
        longitude = i['lon']
        name = i['tags'].get('name')
        street = i['tags'].get('addr:street', 'Sin calle')
        number = i['tags'].get('addr:housenumber', 0)
        
        places['lat'].append(lalitude)
        places['lon'].append(longitude)
        places['name'].append(name)
        places['address'].append(str(street) + ' ' + str(number))

    df = pd.DataFrame(places)
    return df

def correlacion(df1,df2):

    
    return df1.corrwith(df2)