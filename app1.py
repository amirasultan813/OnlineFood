
import pandas as pd 
import streamlit as st
import plotly.express as px 

df = pd.read_csv('food_edited.csv')

def income():
    
    tab1 , tab2 , tab3 , tab4 , tab5 = st.tabs(['Gender' , 'Age' , 'Marital Status','Eduactional' , 'Occupation'])
    
    with tab1 :
        st.plotly_chart(px.histogram(data_frame=df , x='monthly income' , color='gender',
            category_orders={'monthly income': df['monthly income'].value_counts().index},text_auto=True , 
            title='Distribution of Monthly Income with Gender'))
        
    with tab2 :
            average_age = df.groupby('monthly income')['age'].mean().reset_index()
            fig = px.bar(average_age, x='monthly income', y='age',
            labels={'monthly income': 'Monthly Income', 'age': 'Average Age'},
            title='Average age by Monthly Income')
            st.plotly_chart(fig)
        
    with tab3 :
        st.plotly_chart(px.histogram(data_frame=df , x='monthly income' , color='marital status',
            category_orders={'monthly income': df['monthly income'].value_counts().index},text_auto=True
            ,title='Distribution of Monthly Income with Marital Status'))
        
    with tab4 :
        st.plotly_chart(px.histogram(data_frame=df , x='monthly income' , color='educational qualifications',
            category_orders={'monthly income': df['monthly income'].value_counts().index},text_auto=True
            ,title='Distribution of Monthly Income with Educational Qualifications'))
        
    with tab5 :
        st.plotly_chart(px.histogram(data_frame=df , x='monthly income' , color='occupation',
            category_orders={'monthly income': df['monthly income'].value_counts().index},text_auto=True
            ,title='Distribution of Monthly Income with Occupation'))
        
##############################################################################################################        

def gender():
    
    tab1 , tab2 , tab3 , tab4 , tab5 ,tab6 = st.tabs(['Family Size' , 'Age' , 'Marital Status','Eduactional' , 'Feedback','Occupation'])
    
    with tab1:
        st.plotly_chart(px.histogram(data_frame=df , x = 'age' , color ='gender',marginal='box'
        ,title='Distribution of Age with Gender'))
        
    with tab2:
        st.plotly_chart(px.histogram(data_frame=df , x='family size',color='gender' , text_auto=True
        ,title='Distribution of Family Size with Gender'))
        
    with tab3:
        st.plotly_chart(px.histogram(data_frame=df , x='educational qualifications', color='gender',
            category_orders={'educational qualifications': df['educational qualifications'].value_counts().index}
            ,title='Distribution of Educational Qualifications with Gender'))
    
    with tab4:
        st.plotly_chart(px.histogram(data_frame=df , x='marital status',color='gender'
        ,title='Distribution of Marital Status with Gender'))
        
    with tab5:
        st.plotly_chart(px.histogram(data_frame=df , x='feedback' , color='gender',text_auto=True
        ,title='Distribution of Feedback with Gender'))

    with tab6:
        st.plotly_chart(px.histogram(data_frame=df , x='occupation' , color='gender',
            category_orders={'occupation ': df['occupation'].value_counts().index},text_auto=True
        ,title='Distribution of Occupation with Gender'))
        
####################################################################################################

def family():
    
    tab1 , tab2 , tab3 , tab4= st.tabs(['Age' , 'Marital Status','Eduactional','Occupation'])
    
    with tab1:
        average_family_size = df.groupby(['age','occupation'])['family size'].mean().reset_index()
        fig = px.bar(average_family_size, x='age', y='family size',color = 'occupation', 
             labels={'age': 'age', 'family size': 'Average Family Size'},
             title='Average Family Size by age')
        st.plotly_chart(fig)
        
    with tab2:
        average_family_size = df.groupby('marital status')['family size'].mean().reset_index()
        fig = px.bar(average_family_size, x='marital status', y='family size', 
             labels={'marital status': 'marital status', 'family size': 'Average Family Size'},
             title='Average Family Size by Marital Status')
        st.plotly_chart(fig)
        
    with tab3:
        average_family_size = df.groupby('educational qualifications')['family size'].mean().reset_index()
        fig = px.bar(average_family_size, x='educational qualifications', y='family size', 
             labels={'educational qualifications': 'Educational Qualifications', 'family size': 'Average Family Size'},
             title='Average Family Size by Educational Qualifications')
        st.plotly_chart(fig)
        
    with tab4:
        average_family_size = df.groupby('occupation')['family size'].mean().reset_index()
        fig = px.bar(average_family_size, x='occupation', y='family size', 
             labels={'occupation': 'Occupation', 'family size': 'Average Family Size'},
             title='Average Family Size by Occupation')
        st.plotly_chart(fig)
        
############################################################################################

def order_count():
        order_counts_by_occupation = df['occupation'].value_counts().reset_index()
        order_counts_by_occupation.columns = ['Occupation', 'Order Counts']
        
        fig = px.bar(order_counts_by_occupation, x='Occupation', y='Order Counts', 
             title='Order Counts by Occupation',
             labels={'Occupation': 'Occupation', 'Order Counts': 'Order Counts'})
        st.plotly_chart(fig)

##########################################################################################        

def marital():
    
    tab1 , tab2 = st.tabs(['Occupation','Educational'])
    
    
    with tab1:
        st.plotly_chart(px.histogram(data_frame=df , x='educational qualifications' , color='marital status'
            ,text_auto=True , title='Distribution of Educational Qualifications with Marital Status'))
    
    with tab2:
        st.plotly_chart(px.histogram(data_frame=df , x='occupation' , color='marital status'
            ,text_auto=True , title='Distribution ofOccupation with Marital Status'))
        
##############################################################################################

def map_():
    
    import folium
    from streamlit_folium import folium_static

    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=10)
        
    for index, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=f"Pin code: {row['pin code']}").add_to(m)
    folium_map_html = folium_static(m)

    st.components.v1.html(folium_map_html, width=800, height=600)
        
pages = {'income' : income,
        'gender':gender,
         'family':family,
         'order_count': order_count,
         'marital':marital,
         'map_':map_
        }
pg = st.sidebar.radio('Navigate Pages' , pages.keys())

pages[pg]()
