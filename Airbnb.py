import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part

#Streamlit
st.set_page_config(layout="wide")
import streamlit as st

st.markdown("""
    <style>
        .airbnb-title {
            background-color: rgba(255, 255, 255, 0.9);
            color: #FF5A5F;
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            padding: 15px;
            border-radius: 20px;
            margin-bottom: 20px;

        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='airbnb-title'>Airbnb Analysis</p>", unsafe_allow_html=True)

def dataframe():
    df= pd.read_csv("C:/Users/Sujay/New folder/Airbnb.csv")
    return df

df= dataframe()


select = option_menu(None, ["Home", "Data exploration"],
                       icons=["house", "upload"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "28px", "text-align": "center", "margin": "5px",
                                            "color": "#000", "border-radius": "15px", "padding": "10px", 
                                            "background-color": "#FFFAFA", "transition": "background-color 0.3s",
                                            "--hover-color": "#FA8072"},
                               "icon": {"font-size": "28px", "margin-right": "5px"},
                               "container": {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#FF5A5F"}})


if select == "Home":
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image('https://logos-download.com/wp-content/uploads/2016/03/Airbnb_logo.png', width=650)

    with col2:
        st.markdown("<h1 style='color: #FF5A5F; text-decoration: underline white;'>Inception of Airbnb</h1>", unsafe_allow_html=True)
        st.write("")
        st.write("<p style='font-size: 26px;'>Airbnb's inception traces back to 2007 when two hosts graciously opened their San Francisco residence to three guests. Since its modest beginnings, the platform has burgeoned into a global phenomenon, boasting a network of over 4 million hosts who have warmly welcomed more than 1.5 billion guests from around the world. This exponential growth underscores Airbnb's profound impact, transcending geographical boundaries to redefine the hospitality landscape on a global scale.</p>", unsafe_allow_html=True)

    st.markdown("<h1 style='color: #FF5A5F; text-decoration: underline white;'>About Airbnb</h1>", unsafe_allow_html=True)
    st.write("<p style='font-size: 26px;'>Airbnb Inc. (Airbnb) operates a sophisticated online platform dedicated to hospitality services. The corporation offers a mobile application, empowering users worldwide to effortlessly showcase, explore, and secure distinctive accommodations. This innovative app enables hosts to present their properties for short-term lease, facilitating guests in accessing a diverse range of lodging options including vacation rentals, apartments, homestays, castles, treehouses, and hotel rooms. With a global presence spanning across China, India, Japan, Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy, Norway, Portugal, Russia, Spain, Sweden, the United Kingdom, and numerous other regions, Airbnb establishes itself as a pioneering force in the hospitality industry. The company's headquarters are situated in San Francisco, California, United States.</p>", unsafe_allow_html=True)


    
    

if select == "Data exploration":
    st.title("Data Exploration")

   
    tab = ["PRICE ANALYSIS", "AVAILABILITY ANALYSIS", "GEOSPATIAL ANALYSIS", "EXPLORATORY ANALYSIS"]
    tab = st.radio(" ", tab)
    

    if tab=="PRICE ANALYSIS":
        st.title("**PRICE DISPARITY ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique())

            count_df= df[df["country"] == country]
            count_df.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",count_df["room_type"].unique())
            
            room_df= count_df[count_df["room_type"] == room_ty]
            room_df.reset_index(drop= True, inplace= True)

            bar= pd.DataFrame(room_df.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            bar.reset_index(inplace= True)

            bar_chart= px.bar(bar, x='property_type', y= "price", title= "Property Price Discrepancy Analysis",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Pinkyl_r, width=600, height=500)
            st.plotly_chart(bar_chart)

        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            
     
            proper_ty= st.selectbox("Select the Property Type",room_df["property_type"].unique())

            prop_df= room_df[room_df["property_type"] == proper_ty]
            prop_df.reset_index(drop= True, inplace= True)

            pie= pd.DataFrame(prop_df.groupby("host_response_time")[["price","bedrooms"]].sum())
            pie.reset_index(inplace= True)

            pie_chart= px.pie(pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.Magenta_r,
                            title="Comparative Analysis of Price Disparity with Host Response Time",
                            width= 600, height= 500)
            st.plotly_chart(pie_chart)

        col1,col2= st.columns(2)

        with col1:

            
            hostresponsetime= st.selectbox("Choose Host Response Time",prop_df["host_response_time"].unique())

            host_df= prop_df[prop_df["host_response_time"] == hostresponsetime]

            bar_1= pd.DataFrame(host_df.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            bar_1.reset_index(inplace= True)

            bar_chart_1 = px.bar(bar_1, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='Minimum and Maximum Stay Duration Comparison',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Agsunset_r, width=600, height=500)
            

            st.plotly_chart(bar_chart_1)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            bar_2= pd.DataFrame(host_df.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            bar_2.reset_index(inplace= True)

            bar_chart_2 = px.bar(bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='Bedroom and Accommodation Capacity Comparison',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.OrRd, width= 600, height= 500)
           
            st.plotly_chart(bar_chart_2)

    if tab=="AVAILABILITY ANALYSIS":

        st.title("**AVAILABILITY OVERVIEW**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Choose the Country",df["country"].unique())

            country= df[df["country"] == country_a]
            country.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Choose the Property Type",country["property_type"].unique())
            
            property= country[country["property_type"] == property_ty_a]
            property.reset_index(drop= True, inplace= True)

            sunburst_30= px.sunburst(property, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="30-Days Availability",color_discrete_sequence=px.colors.sequential.Burg)
            st.plotly_chart(sunburst_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            sunburst_60= px.sunburst(property, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="60-Days Availability",color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            st.plotly_chart(sunburst_60)

        col1,col2= st.columns(2)

        with col1:
            
            sunburst_90= px.sunburst(property, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="90-Days Availability",color_discrete_sequence=px.colors.sequential.ice_r)
            st.plotly_chart(sunburst_90)

        with col2:

            sunburst_365= px.sunburst(property, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="365-Days Availability",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(sunburst_365)
        
        roomtype_a= st.selectbox("Choose the Room Type", property["room_type"].unique())

        room= property[property["room_type"] == roomtype_a]

        multiple_bar= pd.DataFrame(room.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        multiple_bar.reset_index(inplace= True)

        multiple_bar_a = px.bar(multiple_bar, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='Availability Trends by Host Response Time',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Purp,width=1000)

        st.plotly_chart(multiple_bar_a)


    if tab=="GEOSPATIAL ANALYSIS":

        st.title("**GEOSPATIAL VISUALIZATION**")
        st.write("")

        map = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "PinkYl_r",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        map.update_layout(width=1100,height=800,title='Airbnb Listing Geospatial Distribution')
        st.plotly_chart(map)   


    if tab=="EXPLORATORY ANALYSIS":

        country_t= st.selectbox("Select the Country.",df["country"].unique())

        cont= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property Type.",cont["property_type"].unique())

        propt= cont[cont["property_type"] == property_ty_t]
        propt.reset_index(drop= True, inplace= True)

        propt_sort= propt.sort_values(by="price")
        propt_sort.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(propt_sort.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "Price Variation Across Host Neighborhoods", width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Pinkyl_r)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "Mean Price Analysis across Host Neighborhood",width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Purp)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(propt_sort.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Peach,
                                title= "Price Analysis across Host Location")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Magenta,
                                title= "Mean Price Analysis across Host Location")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room Type.",propt_sort["room_type"].unique())

        roomt= propt_sort[propt_sort["room_type"] == room_type_t]

        price_sort= roomt.sort_values(by= "price")

        price_sort.reset_index(drop= True, inplace = True)

        top_50_price= price_sort.head(100)

        fig_top_50_price_1= px.bar(top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "blues",
                                range_color=(0,top_50_price["price"].max()),
                                title= "Stay Duration and Accommodation Capacity Analysis",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "RedOr",
                                 title= "Bedroom, Bed, and Accommodation Analysis by Bed Type",
                                range_color=(0,top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)




        
