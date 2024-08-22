import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import plotly.express as px

st.set_page_config(layout="wide")    
selected = option_menu("", ['Home','Data Explore','Contact Us'],default_index=0,orientation="horizontal")

if selected == "Home":         
    st.title("*:blue[Welcome to Mukilan's Airbnb Analysis]*")
    st.markdown("***:violet[Vacation rental American company]***")
    st.divider()
    coll1, coll2 = st.columns(2)
    coll3, coll4 = st.columns(2)
    coll5, coll6 = st.columns(2)
    
    with coll1: 
        st.subheader("""**Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.**""")
        st.divider()
        st.divider()
        
    with coll2: 
        st.image('D:\\Project Files\\New folder\\Airbnb-Analysis\\front.jpg',width=420)
        st.caption("***Headquarters at 888 Brannan Street, in San Francisco, California, United States***")

    with coll3: 
        st.image("D:\\Project Files\\New folder\\Airbnb-Analysis\\logo.jpg",width=465)
        st.caption("***Airbnb is a shortened version of its original name, AirBedandBreakfast.com***") 

    with coll4: 
        st.subheader("""**The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents,and for a lack of regulation**""")
        st.divider()
        st.divider()
        
    with coll5: 
        st.subheader("**Lodging, Hospitality, Homestay, Travel Industry, Property management and Tourism**")
        st.subheader("**Number of employees- 6,907 (2023) Revenue(Decrease) US$5.99 billion (2023)**")
        
    with coll6:         
        st.image("D:\\Project Files\\New folder\\Airbnb-Analysis\\dom.jpg",width=465)
        st.caption("***Area served - Worldwide***")
    st.divider()
    
    st.subheader("Power Bi Data Visualization") 
    st.image('D:\\Project Files\\New folder\\Airbnb-Analysis\\Airbi.png')
    
      
elif selected=="Data Explore":
    
    df=pd.read_csv("D:\\Project Files\\New folder\\Airbnb-Analysis\\Airbnb.csv")
    country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
    prop = st.sidebar.multiselect('Select Property_Type',sorted(df.Property_Type.unique()),sorted(df.Property_Type.unique()))
    room = st.sidebar.multiselect('Select Room_Type',sorted(df.Room_Type.unique()),sorted(df.Room_Type.unique()))

    query = f'Country in {country} & Room_Type in {room} & Property_Type in {prop}'    

    col1,col2=st.columns([1,1],gap='small')

    with col1:
      
        df1 = df.query(query).groupby(["Property_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                         title='Top 10 Property Types With Count',
                         x='Property_Type', y='count',
                         orientation='v',color='Property_Type',
                         hover_name='Property_Type',
                         color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
        
        
        df1= df.query(query).groupby(["Room_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title=' Room_Type With Count',
                             values='count',names="Room_Type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True)    
        
              
        df1= df.query(query).groupby(["Cancellation_policy"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.line(df1,
                             title=' Cancellation_Policy With Count',
                             x='Cancellation_policy',y='count',text='count',markers=True)
        fig.update_traces(textposition="top center")                    
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df.query(query).groupby(["Number_Of_Reviews"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Number_Of_Reviews With Count',
                             x="Number_Of_Reviews",y="count",
                             text="count", orientation='v',
                             color='count',color_continuous_scale=px.colors.sequential.Darkmint_r)
        fig.update_traces( textposition='outside')
        st.plotly_chart(fig,use_container_width=True)
        
        
    with col2: 
      
        df1= df1= df.query(query).groupby('Property_Type',as_index=False)['Minimum_Nights'].mean()
        fig = px.pie(df1,
                             title='Minimum_Nights With Property_Type',
                             values="Minimum_Nights",names="Property_Type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True) 
        
        
        df1= df1= df.query(query).groupby(["Maximum_Nights"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title='Maximum_Nights With Count',
                             values='count',names="Maximum_Nights")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12)
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df1= df.query(query).groupby(["Host_Neighbourhood"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title='Host Neighbourhood With Count',
                             x="Host_Neighbourhood", y="count",
                             orientation='v',color='count',
                             color_continuous_scale=px.colors.sequential.Bluered_r)
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df1= df.query(query).groupby("Property_Type",as_index=False)['Price'].mean().sort_values(by='Price',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Property With Mean Price ',
                             x="Property_Type",y="Price",
                             text="Price", orientation='v',
                             color='Property_Type',color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
        
           
        
elif selected=="Contact Us":      
    st.subheader(':violet[Airbnb Data Visualisation]')
    st.markdown('''**I Created this Airbnb Data Analysis Project Using "Python" to perform Data Cleansing, Understand Dataset, 
                "Exploratery Data anslysis (EDA)" and Creating "Dashboard report" Using "Power BI".
                Since 2008, guests and hosts have used Airbnb to expand on travelling possibilities and present more unique,
                personalized way of experiencing the world. This dataset describes the listing activity and metrics in Amsterdam,
                Netherland for 2019.The objective of the project is to perform data visualization techniques to understand the insight of the data.
                This project aims to apply Exploratory Data Analysis (EDA) and Business Intelligence tools such as Power BI to get a visual understanding of the data.**''')

    coll1, coll2 = st.columns(2)
    with coll1: 
        st.title("Contact Us")  
        st.caption(":red[Note:*fill all mandatory fields]") 
                
        Name = st.text_input("Name*")
        Mobile = st.text_input("Mobile*")
        Email = st.text_input("Email*")
        Message = st.text_area("Message (optional)")
        
        if st.button("Submit"):
            st.success('''Thank you for your Message, We will get back to you soon''')

    with coll2:
        st.subheader('**MUKILAN ELANCHEZHIAN**')
        st.caption('**Mobile:- 8778350485, E-Mail - mukhilan1642@gmail.com**')


