import pymongo
import pandas as pd
pd.set_option("display.max_columns",None)
import warnings
warnings.filterwarnings("ignore")



Client= pymongo.MongoClient("mongodb+srv://mansabhat530:Fluffy53@cluster0.j3nhz4s.mongodb.net/?retryWrites=true&w=majority")


database= Client["sample_airbnb"]
collection= database["listingsAndReviews"]

data= []
for i in collection.find({},{"_id":1, "listing_url":1, "name":1, "property_type":1, "room_type":1, "bed_type":1, "minimum_nights":1, "maximum_nights":1, "cancellation_policy":1, "accommodates":1, "bedrooms":1, "beds":1, "number_of_reviews":1, "bathrooms":1, "price":1, "extra_people":1, "guests_included":1, "images.picture_url":1, "review_scores":1,"cleaning_fee":1}):
    data.append(i)
df_1= pd.DataFrame(data)


df_1["images"]= df_1["images"].apply(lambda x: x["picture_url"])
df_1["review_scores"]= df_1["review_scores"].apply(lambda x: x.get("review_scores_rating",0))
df_1.describe().T
df_1["minimum_nights"]= df_1["minimum_nights"].astype(int)
df_1["maximum_nights"]= df_1["maximum_nights"].astype(int)
df_1["bedrooms"]= df_1["bedrooms"].astype(int)
df_1["beds"]= df_1["beds"].astype(int)
df_1["bathrooms"]= df_1["bathrooms"].astype(str).astype(float).astype(int)
df_1["price"]= df_1["price"].astype(str).astype(float).astype(int)
df_1["extra_people"]= df_1["extra_people"].astype(str).astype(float).astype(int)
df_1["guests_included"]= df_1["guests_included"].astype(str).astype(float).astype(int)
df_1["cleaning_fee"]= df_1["cleaning_fee"].astype(str).astype(float).astype(int)


#Host details
host= []
for i in collection.find({},{"_id":1, "host":1}):
    host.append(i)

df_host= pd.DataFrame(host)

host_columns= {'_id':[],'host_id':[], 'host_url':[], 'host_name':[], 'host_location':[],"host_response_time":[], 'host_thumbnail_url':[], 'host_picture_url':[], 'host_neighbourhood':[], 'host_response_rate':[], 'host_is_superhost':[], 'host_has_profile_pic':[], 'host_identity_verified':[], 'host_listings_count':[], 'host_total_listings_count':[], 'host_verifications':[]}

for i in df_host["_id"]:
    host_columns["_id"].append(i)
for i in df_host["host"]:
    host_columns["host_id"].append(i["host_id"])
    host_columns["host_url"].append(i["host_url"])
    host_columns["host_name"].append(i["host_name"])
    host_columns["host_location"].append(i["host_location"])
    host_columns["host_response_time"].append(i.get("host_response_time"))
    host_columns["host_thumbnail_url"].append(i["host_thumbnail_url"])
    host_columns["host_picture_url"].append(i["host_picture_url"])
    host_columns["host_neighbourhood"].append(i["host_neighbourhood"])
    host_columns["host_response_rate"].append(i.get("host_response_rate"))
    host_columns["host_is_superhost"].append(i["host_is_superhost"])
    host_columns["host_has_profile_pic"].append(i["host_has_profile_pic"])
    host_columns["host_identity_verified"].append(i["host_identity_verified"])
    host_columns["host_listings_count"].append(i["host_listings_count"])
    host_columns["host_total_listings_count"].append(i["host_total_listings_count"])
    host_columns["host_verifications"].append(i["host_verifications"])
df_host_1= pd.DataFrame(host_columns)

#neighbourhood data

list_index= []
for index,row in df_host_1.iterrows():
    if row["host_neighbourhood"] =='':
        list_index.append(index)

#address

address= []
for i in collection.find({}, {"_id":1, "address":1}):
    address.append(i)

df_address= pd.DataFrame(address)
address_columns= {'_id':[], 'street':[], 'suburb':[], 'government_area':[], 'market':[], 'country':[],
                   'country_code':[], 'location_type':[], "longitude":[], "latitude":[],
                    "is_location_exact":[]}

for i in df_address["_id"]:
    address_columns["_id"].append(i)

for i in df_address["address"]:
    address_columns["street"].append(i["street"])
    address_columns["suburb"].append(i["suburb"])
    address_columns["government_area"].append(i["government_area"])
    address_columns["market"].append(i["market"])
    address_columns["country"].append(i["country"])
    address_columns["country_code"].append(i["country_code"])
    address_columns["location_type"].append(i["location"]["type"])
    address_columns["longitude"].append(i["location"]["coordinates"][0])
    address_columns["latitude"].append(i["location"]["coordinates"][1])
    address_columns["is_location_exact"].append(i["location"]["is_location_exact"])
df_address_1= pd.DataFrame(address_columns)

#availablitiy
availability= []
for i in collection.find({}, {"_id":1, "availability":1}):
    availability.append(i)
df_availabe= pd.DataFrame(availability)
availabe_columns= {'_id':[], 'availability_30':[], 'availability_60':[], 'availability_90':[], 'availability_365':[]}

for i in df_availabe["_id"]:
    availabe_columns["_id"].append(i)

for i in df_availabe["availability"]:
    availabe_columns["availability_30"].append(i["availability_30"])
    availabe_columns["availability_60"].append(i["availability_60"])
    availabe_columns["availability_90"].append(i["availability_90"])
    availabe_columns["availability_365"].append(i["availability_365"])
df_availabe_1= pd.DataFrame(availabe_columns)

#amenities

amenities= []
for i in collection.find({},{"_id":1, "amenities":1}):
    amenities.append(i)
df_amenities= pd.DataFrame(amenities)
def sort_amenities(x):
    a= x
    a.sort()
    return a

df_amenities["amenities"]= df_amenities["amenities"].apply(lambda x: sort_amenities(x))

#empty values
id_e=[]
stre_e=[]
suburb_e=[]
gov_e=[]
mark_e=[]
cntry_e=[]
cntry_co_e=[]
loc_ty_e=[]
long_e=[]
lat_e=[]
is_loc_tr_e=[]
for index,row in df_address_1.iterrows():
    if row["_id"] == '':
        id_e.append(index)

    if row["street"] == '':
        stre_e.append(index)
        
    if row["suburb"] == '':
        suburb_e.append(index)

    if row["government_area"] == '':
        gov_e.append(index)

    if row["market"] == '':
        mark_e.append(index)

    if row["country"] == '':
        cntry_e.append(index)
    
    if row["country_code"] == '':
        cntry_co_e.append(index)

    if row["location_type"] == '':
        loc_ty_e.append(index) 

    if row["longitude"] == '':
        long_e.append(index)

    if row["latitude"] == '':
        lat_e.append(index)

    if row["is_location_exact"] == '':
        is_loc_tr_e.append(index)

empty_columns=[id_e,stre_e,suburb_e,gov_e,mark_e,cntry_e,cntry_co_e,loc_ty_e,long_e,lat_e,is_loc_tr_e]
for i in empty_columns:
    print(len(i))

#Handling null values
df_1["beds"].fillna(0,inplace= True)
df_1["bedrooms"].fillna(0,inplace= True)
df_1["bathrooms"].fillna(0,inplace= True)
df_1["cleaning_fee"].fillna(0,inplace= True)

df_host_1["host_response_time"].fillna("Not Specified",inplace= True)
df_host_1["host_response_rate"].fillna("Not Specified",inplace= True)
df_host_1["host_neighbourhood"]= df_host_1["host_neighbourhood"].replace({'':"Not Specified"})
df_host_1["host_is_superhost"]= df_host_1["host_is_superhost"].map({False: "No", True: "Yes"})
df_host_1["host_has_profile_pic"]= df_host_1["host_has_profile_pic"].map({False: "No", True: "Yes"})
df_host_1["host_identity_verified"]= df_host_1["host_identity_verified"].map({False: "No", True: "Yes"})

df_address_1["suburb"]= df_address_1["suburb"].replace({'':"Not Specified"})
df_address_1["market"]= df_address_1["market"].replace({'':"Not Specified"})
df_address_1["is_location_exact"]= df_address_1["is_location_exact"].map({False:"No", True:"Yes"})


#merging
dataframe= pd.merge(df_1, df_host_1, on="_id")
dataframe= pd.merge(dataframe, df_address_1, on="_id")
dataframe= pd.merge(dataframe, df_availabe_1, on="_id")
dataframe= pd.merge(dataframe, df_amenities, on="_id")

dataframe.to_csv("Airbnb.csv", index= False)
df= pd.read_csv("C:/Users/Sujay/New folder/Airbnb.csv")