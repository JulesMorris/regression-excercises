# Zillow Price Prediction
A project using regression to develop predictions to beat the Zestimate. 

## About the Project 

### Project Goals

My goals are to address identify the key features that impact home price in the Southern California market so that I can build a predictive model that accurately predicts single family home price and make recommendations to increase the accuracy of predictive power in future models for deployment.

### Project Description

This project looked at features impacting home prices in Ventura, LA, and Orange County. Accurately predicting home price is important for not only Zillow, but all customers interested in purchasing a home. The California market is notoriously prohibitive for price sensitive consumers, building an accurate predictive model based on attributes known to drive price and customizing that to California's unique landscape creates a more knowledgable customer base. 


### Initial Questions

1. Is area (in sqft) positively correlated with home price in the SoCal market?
2. Is there a relationship between pre-war homes, defined in this project as homes built before 1945 and homes built afterwards?
3. Is home price different across counties?
4. Does access to the beach and mountains play a role in home price?


### Data Dictionary


'airconditioningtypeid':	 Type of cooling system present in the home (if any)

'architecturalstyletypeid':	 Architectural style of the home (i.e. ranch, colonial, split-level, etc…)

'basementsqft':	 Finished living area below or partially below ground level

'bathroomcnt' (bathrooms):	 Number of bathrooms in home including fractional bathrooms

'bedroomcnt' (bedrooms):	 Number of bedrooms in home 

'buildingqualitytypeid':	 Overall assessment of condition of the building from best (lowest) to worst (highest)

'buildingclasstypeid':	The building framing type (steel frame, wood frame, concrete/brick) 

'calculatedbathnbr':	 Number of bathrooms in home including fractional bathroom

'decktypeid':	Type of deck (if any) present on parcel

'threequarterbathnbr':	Number of 3/4 bathrooms in house (shower + sink + toilet)

'finishedfloor1squarefeet':	 Size of the finished living area on the first (entry) floor of the home

'calculatedfinishedsquarefeet' (area):	 Calculated total finished living area of the home 

'finishedsquarefeet6':	Base unfinished and finished area

'finishedsquarefeet12':	Finished living area

'finishedsquarefeet13':	Perimeter  living area

'finishedsquarefeet15':	Total area

'finishedsquarefeet50':	 Size of the finished living area on the first (entry) floor of the home

'fips' (count):	 Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details

'fireplacecnt':	 Number of fireplaces in a home (if any)

'fireplaceflag':	 Is a fireplace present in this home 

'fullbathcnt':	 Number of full bathrooms (sink, shower + bathtub, and toilet) present in home

'garagecarcnt':	 Total number of garages on the lot including an attached garage

'garagetotalsqft':	 Total number of square feet of all garages on lot including an attached garage

'hashottuborspa': Does the home have a hot tub or spa

'heatingorsystemtypeid':	 Type of home heating system

'latitude':	Latitude of the middle of the parcel multiplied by 10e6

'longitude':	Longitude of the middle of the parcel multiplied by 10e6

'lotsizesquarefeet (lot_size)'	 Area of the lot in square feet

'numberofstories':	 Number of stories or levels the home has

'parcelid (parcel_id)'	 Unique identifier for parcels (lots) 

'poolcnt':	 Number of pools on the lot (if any)

'poolsizesum'	: Total square footage of all pools on property

'pooltypeid10':	 Spa or Hot Tub

'pooltypeid2':	 Pool with Spa/Hot Tub

'pooltypeid7': Pool without hot tub

'propertycountylandusecode':	 County land use code i.e. it's zoning at the county level

'propertylandusetypeid':	 Type of land use the property is zoned for

'propertyzoningdesc':	 Description of the allowed land uses (zoning) for that property

'rawcensustractandblock (census_tract)'	 Census tract and block ID combined - also contains blockgroup assignment by extension

'censustractandblock':	 Census tract and block ID combined - also contains blockgroup assignment by extension

'regionidcounty':	County in which the property is located

'regionidcity':	 City in which the property is located (if any)

'regionidzip(zip_code)':	 Zip code in which the property is located

'regionidneighborhood':	Neighborhood in which the property is located

'roomcnt (room_count)':	 Total number of rooms in the principal residence

'storytypeid':	 Type of floors in a multi-story house (i.e. basement and main level, split-level, attic, etc.).  See tab for details.

'typeconstructiontypeid':	 What type of construction material was used to construct the home

'unitcnt':	Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)

'yardbuildingsqft17':	Patio in  yard

'yardbuildingsqft26':	Storage shed/building in yard

'yearbuilt (year_built)':	 The Year the principal residence was built 

'taxvaluedollarcnt (tax_value)':	The total tax assessed value of the parcel

'structuretaxvaluedollarcnt':	The assessed value of the built structure on the parcel

'landtaxvaluedollarcnt':	The assessed value of the land area of the parcel

'taxamount(tax_amount)':	The total property tax assessed for that assessment year

'assessmentyear':	The year of the property tax assessment 

'taxdelinquencyflag':	Property taxes for this parcel are past due as of 2015

'taxdelinquencyyear':	Year for which the unpaid propert taxes were due 


*Features in parenthesis denote the new name of the column in this project.*


### Project Planning

    Acquire data from the Codeup Database and store the process as a function for replication. Save the function in a wrangle.py file to import into the Final Report Notebook.

    View data to gain understanding of the dataset and to create the readme.

    Create README.md with data dictionary, project and business goals, documentation of the initial hypotheses.

    Clean and prepare data for the first iteration through the data pipeline. Store this as a function to automate the process, store the function in the wrangle.py module, and prepare data in Final Report Notebook by importing and using the funtion.

    Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.

    Establish a baseline accuracy and document well.

    Train four different regression models.

    Evaluate models on train and validate datasets.

    Choose the model with that performs the best and evaluate that single model on the test dataset.

    Document executive summary, conclusions, takeaways, and next steps in the Final Report Notebook.

    Upload README.md, Data Dictionary, wrangle.py, Project Scratch Notebook, Final Report Notebook


### Steps to Reproduce


For example: 

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the zillow dataset. Store that env file locally in the repository. 
2. Clone my repository (including the wrangle3.py) and confirm .gitignore is hiding your env.py file.
3. Import all libraries in first cell of report, a pip install of any unfamiliar libraries into your local system may be required.
4. Dowload wrangle3.py from this repository.
5. Use wrangle to acquire and prep the data. 

#### Wrangle

##### Module (wrangle3.py)

- This module contains user defined functions to acquire and prepare the data.

- These functions:

1. Acquire data from SQL database and store a cached version.
2. Drop outliers using IQR rule.
3. Change column names.
4. Train, test, and split data.
5. Scale data.
6. Scale data based on county.


##### Missing Values (report.ipynb)

- Missing values handled following the IQR principle first.

- Irrelevant data (transaction not in 2017) dropped.

- Nulls dropped.

- Data retention: 78.4%
