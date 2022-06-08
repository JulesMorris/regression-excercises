import pandas as pd
import seaborn as sns
from env import get_db_url
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#acquire data, join on parcelid

def acquire_zillow(use_cache = True):
    if os.path.exists('zillow.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('zillow.csv')
    print('Acquring from SQL database')
    url = get_db_url('zillow')
    query = '''
            
    SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet,taxvaluedollarcnt, yearbuilt, taxamount, fips, 
    transactiondate, roomcnt, latitude, longitude, rawcensustractandblock, lotsizesquarefeet, propertylandusetypeid, regionidzip
    FROM properties_2017

    LEFT JOIN propertylandusetype USING(propertylandusetypeid)
    JOIN predictions_2017 USING (parcelid)

    WHERE propertylandusedesc IN ("Single Family Residential",                       
                              "Inferred Single Family Residential")'''

    #create df
    df = pd.read_sql(query, url)

    #create cached csv
    df.to_csv('zillow.csv', index = False)                          
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#function to reduce outliers

def discard_outliers(df, k, col_list):
    
    for col in col_list:
        #obtain quartiles
        q1, q3 = df[col].quantile([.25, .75]) 
        
        #obtain iqr range
        iqr = q3 - q1
        
        upper_bound = q3 + k * iqr
        lower_bound = q1 - k * iqr
        
        #return outlier - free df
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]

    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def prep_zillow(df):

    #rename df columns
    df = df.rename(columns = {'bedroomcnt': 'bedrooms',
                              'bathroomcnt': 'bathrooms',
                              'calculatedfinishedsquarefeet': 'area',
                              'taxvaluedollarcnt': 'tax_value',
                              'yearbuilt': 'year_built',
                              'taxamount': 'tax_amount',
                              'fips': 'county',
                              'transactiondate': 'transaction_date',
                              'roomcnt': 'room_count',
                              'rawcensustractandblock': 'census_tract',
                              'lotsizesquarefeet': 'lot_size',
                              'propertylandusetypeid': 'prop_land_id',
                              'regionidzip': 'zip_code'})


    #undo 10e6 that was applied to lat and long
    df[['latitude', 'longitude']] = (df[['latitude', 'longitude']]) / (10 ** 6)

    #undo 10e6 that was applied to census_tract
    df['census_tract'] = (df['census_tract']) / (10 ** 6)

    #create new column for bed/bath
    df['bed_and_bath'] = df['bedrooms'] + df['bathrooms']

    #create new column to bin year_built
    df['year_built_binned'] = pd.cut(x = df['year_built'], 
                                 bins = [1878, 1909, 1919, 1929, 1939, 1949, 1959, 1969, 1979, 1989, 1999, 2009, 2019], 
                                 labels=[1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])

    #create new column to bin tax value
    df['tax_value_binned'] =  pd.qcut(df['tax_value'], 3, labels = ['Low', 'Med', 'High'], precision = 2)


    #Get dummies for non-binary categorical variables
    dummy_df = pd.get_dummies(df[['county']], dummy_na = False, \
                              drop_first = True)

    #Concatenate dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis = 1)


    #eliminate values that did not occur in 2017
    df = df[(df.transaction_date <= '2017-12-31')]

    #eliminate lot_size elimination
    df = df[df.lot_size < 200000]

    #drop null values
    df = df.dropna()

    #encode tax_value after dropping nulls
    df['tax_value_encoded'] = df['tax_value_binned'].map({'Low': 0, 'Med': 1, 'High': 2}).astype(int)



    #use function to discard outliers
    df = discard_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'area', 'tax_value', 'tax_amount', 'lot_size'])
 
    #train, test, split
    train_validate, test = train_test_split(df, test_size = .2, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123)

    return train, validate, test

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#get scaled data

def scale_data(train, 
               validate, 
               test, 
               columns_to_scale = ['bedrooms', 'bathrooms', 'area', 'year_built', 'lot_size', 'latitude', 'longitude', 'bed_and_bath'],
               return_scaler = False):

    '''
    Scales the 3 data splits. 
    Takes in train, validate, and test data splits and returns their scaled counterparts.
    If return_scalar is True, the scaler object will be returned as well
    '''
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    scaler = MinMaxScaler()
    scaler.fit(train[columns_to_scale])
    
    train_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                  columns = train[columns_to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                  columns = validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns = test[columns_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def wrangled_zillow():
    
    train, validate, test = prep_zillow(acquire_zillow())

    return train, validate, test