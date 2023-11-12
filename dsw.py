#streamlit library
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from PIL import Image
import re
import time
#visualization library
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
#data manipulation library
import pandas as pd
import numpy as np
#data manipulation library
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import altair as alt
import joblib
st.set_page_config(
    page_title="CUSTOMER CHURN ANALYSYS",
    page_icon="📊",
    layout="wide"
)
#css file
with open('style.css')as f:
 st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

with st.sidebar:
    amazon = Image.open(r'logo.png')
    st.image(amazon, width=250)
    st.markdown('\n')
    selected = option_menu("Main Menu", ["Dashboard", 'Prediction'], 
        icons=['clipboard-data', 'gear'], menu_icon="cast", default_index=0)
    

#load data
@st.cache_data()
def load_data(url):
    df = pd.read_excel(url)
    return df

df = load_data('Telco_customer_churn_adapted_v2.xlsx')
#load data
df2 = load_data('Telco_customer_churn_adapted_v2.xlsx')
# Menghapus beberapa kolom lainnya
columns_to_drop = ['Customer ID', 'Location', 'Longitude', 'Latitude']
df2.drop(columns=columns_to_drop, inplace=True)














if selected == "Dashboard":
    st.header('Customer Churn Dashboard')
    st.markdown('')

    m1, m2 = st.columns(2)

    with m1:
        number_of_users = len(df['Customer ID'].unique())
        st.metric(label="Total User", value=number_of_users)
    with m2:
        total_monthly_purchase = df['Monthly Purchase'].sum()
        formatted_total = f'Rp {total_monthly_purchase:,.2f}'
        st.metric(label="Total Monthly Purchase", value=formatted_total)

    cat_opt2 = st.radio("Grouped insight by:", ['Product Insight', 'User Insight', 'Account Insight'], index=0, key='cat_opt2', horizontal=True)
    
    if cat_opt2 == "Product Insight":
        viz1, viz2 = st.columns([1, 1])

        with viz1: 
            st.subheader("Game Products")

            # Membuat bar chart dengan Altair untuk "Games Product" berdasarkan "Churn Label"
            games_churn_chart = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Games Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(games_churn_chart, use_container_width=True)
        with viz2:
            st.subheader("Education Product")

            # Membuat bar chart dengan Altair untuk "Education Product" berdasarkan "Churn Label"
            Education_Product_chart = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Education Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(Education_Product_chart, use_container_width=True)
        with viz1: 
            st.subheader("Video Product")

            # Membuat bar chart dengan Altair untuk "Video Product" berdasarkan "Churn Label"
            video_churn_chart = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Video Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(video_churn_chart, use_container_width=True)

        with viz2:
            st.subheader("Music Product")

            # Membuat bar chart dengan Altair untuk "Music Product" berdasarkan "Churn Label"
            music_churn_chart = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Music Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(music_churn_chart, use_container_width=True)
        

    if cat_opt2 == "Account Insight":

        viz1, viz2 = st.columns([1, 1])
        with viz1: 
            st.subheader("Use MyApp")

            # Membuat bar chart dengan Altair untuk "Games Product" berdasarkan "Churn Label"
            Use_MyApp= (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Use MyApp:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(Use_MyApp, use_container_width=True)
        with viz2:
            st.subheader("Payment Method")

            # Membuat bar chart dengan Altair untuk "Education Product" berdasarkan "Churn Label"
            Payment_Method = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Payment Method:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(Payment_Method, use_container_width=True)
        with viz1: 
            st.subheader("Call Center")

            # Membuat bar chart dengan Altair untuk "Video Product" berdasarkan "Churn Label"
            Call_Center= (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Call Center:N', title=''),
                    y=alt.Y('count():Q', title='Frequency'),
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20'))
                )
                .properties(
                    width=400, height=400
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(Call_Center, use_container_width=True)


    if cat_opt2 == "User Insight":
        viz1, viz2 = st.columns([1, 1])
    
        with viz1: 
            st.subheader("Tenure Months")
        
            # Membuat histogram dengan Altair
            Tenure_Months = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('Tenure Months:Q', bin=alt.Bin(maxbins=6), title=''),
                    alt.Y('count():Q', title='Frekuensi'),
                    color=alt.Color('Churn Label:N', title='Churn Label')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
        
            # Menampilkan histogram di Streamlit
            st.altair_chart(Tenure_Months, use_container_width=True)

        with viz2: 
            st.subheader("Monthly Purchase")
        
            # Membuat histogram untuk "Monthly Purchase"
            Monthly_Purchase= (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('Monthly Purchase:Q', bin=alt.Bin(maxbins=6), title=''),
                    alt.Y('count():Q', title='Frekuensi'),
                    color=alt.Color('Churn Label:N', title='Churn Label')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
        
            # Menampilkan histogram di Streamlit
            st.altair_chart(Monthly_Purchase, use_container_width=True)

        with viz1: 
            st.subheader("CLTV")
        
            # Membuat histogram untuk "CLTV"
            CLTV= (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('CLTV:Q', bin=alt.Bin(maxbins=6), title=''),
                    alt.Y('count():Q', title='Frekuensi'),
                    color=alt.Color('Churn Label:N', title='Churn Label')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
        
            # Menampilkan histogram di Streamlit
            st.altair_chart(CLTV, use_container_width=True)

        with viz2: 
            st.subheader("Device Class")
        
            # Membuat bar chart untuk "Device Class"
            Device_Class = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('Device Class:N', title=''),
                    alt.Y('count():Q', title='Frekuensi'),
                    color=alt.Color('Churn Label:N', title='Churn Label')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
        
            # Menampilkan bar chart di Streamlit
            st.altair_chart(Device_Class, use_container_width=True)

        
      






















    selected_columns = ['Tenure Months', 'Device Class', 'Games Product', 'Music Product', 'Education Product',
                    'Call Center', 'Video Product', 'Use MyApp', 'Payment Method', 'Monthly Purchase', 'CLTV']




    # Pilihan radio untuk mengelompokkan berdasarkan kategori
    cat_opt = st.radio("Grouped chart by:", ['Histogram', 'Boxplot', 'Bar chart', 'Pie chart'], index=0, key='cat_opt', horizontal=True)

    if cat_opt == "Histogram":
        viz1, viz2, viz3 = st.columns([1, 1, 1])

        with viz1: 
            st.subheader("Tenure Months")

            # Membuat histogram dengan Altair
            hist1 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('Tenure Months:Q', bin=alt.Bin(maxbins=6), title='                       Tenure Months'),
                    alt.Y('count():Q', title='Frekuensi')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan histogram di Streamlit
            st.altair_chart(hist1, use_container_width=True)
        with viz2:
            st.subheader("Monthly Purchase")

            # Membuat histogram dengan Altair
            hist2 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('Monthly Purchase:Q', bin=alt.Bin(maxbins=6), title='Monthly Purchase'),
                    alt.Y('count():Q', title='Frekuensi')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan histogram di Streamlit
            st.altair_chart(hist2, use_container_width=True)

        with viz3:
            st.subheader("CLTV")

            # Membuat histogram ketiga dengan Altair
            hist3 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    alt.X('CLTV:Q', bin=alt.Bin(maxbins=6), title='CLTV'),
                    alt.Y('count():Q', title='Frekuensi')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan histogram ketiga di Streamlit
            st.altair_chart(hist3, use_container_width=True)
    if cat_opt == "Boxplot":
        viz1, viz2, viz3 = st.columns([1, 1, 1])

        with viz1: 
            st.subheader("Tenure Months")


            box1 = (
                alt.Chart(df)
                .mark_boxplot()
                .encode(
                    alt.Y('Tenure Months:Q', title='Value')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(box1, use_container_width=True)

        with viz2:
            st.subheader("Monthly Purchase")

            box2 = (
                alt.Chart(df)
                .mark_boxplot()
                .encode(
                    alt.Y('Monthly Purchase:Q', title='Value')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(box2, use_container_width=True)

        with viz3:
            st.subheader("CLTV")

            box3 = (
                alt.Chart(df)
                .mark_boxplot()
                .encode(
                    alt.Y('CLTV:Q', title='Value')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
            st.altair_chart(box3, use_container_width=True)

    if cat_opt == "Bar chart":
        viz1, viz2, viz3 = st.columns([1, 1, 1])


        with viz1: 
            st.subheader("Device Class")

            # Membuat bar chart dengan Altair untuk 'Device Class'
            bar1 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Device Class:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(bar1, use_container_width=True)

        with viz2:
            st.subheader("Call Center")

            bar2 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Call Center:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(bar2, use_container_width=True)

        with viz3:
            st.subheader("Churn Label")

            bar3 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Churn Label:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan bar chart di Streamlit
            st.altair_chart(bar3, use_container_width=True)

        # Menambahkan bar chart kedua untuk tiga variabel tambahan
        with viz1: 
            st.subheader("Education Product")

            bar4 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Education Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar4, use_container_width=True)

        with viz2:
            st.subheader("Games Product")

            bar5 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Games Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar5, use_container_width=True)

        with viz3:
            st.subheader("Video Product")

            bar6 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Video Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar6, use_container_width=True)

        # Menambahkan bar chart ketiga untuk empat variabel tambahan
        with viz1: 
            st.subheader("Use MyApp")

            bar7 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Use MyApp:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar7, use_container_width=True)

        with viz2:
            st.subheader("Payment Method")

            bar8 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Payment Method:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar8, use_container_width=True)

        with viz3:
            st.subheader("Music Product")

            bar9 = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X('Music Product:N', title=''),
                    y=alt.Y('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            st.altair_chart(bar9, use_container_width=True)

    if cat_opt == "Pie chart":
        viz1, viz2, viz3 = st.columns([1, 1, 1])

        with viz1: 
            st.subheader("Device Class")

            # Membuat pie chart dengan Altair untuk 'Device Class'
            pie1 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Device Class:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie1, use_container_width=True)

        with viz2:
            st.subheader("Call Center")

            # Membuat pie chart dengan Altair untuk 'Call Center'
            pie2 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Call Center:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie2, use_container_width=True)

        with viz3:
            st.subheader("Churn Label")

            # Membuat pie chart dengan Altair untuk 'Churn Label'
            pie3 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Churn Label:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie3, use_container_width=True)
        # variabel baris kedua

        with viz1: 
            st.subheader("Education Product")

            # Membuat pie chart dengan Altair untuk 'Education Product'
            pie4 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Education Product:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie4, use_container_width=True)

        with viz2:
            st.subheader("Games Product")

            # Membuat pie chart dengan Altair untuk 'Games Product'
            pie5 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Games Product:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie5, use_container_width=True)

        with viz3:
            st.subheader("Video Product")

            # Membuat pie chart dengan Altair untuk 'Video Product'
            pie6 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Video Product:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie6, use_container_width=True)

        # variabel bari ketiga

        with viz1: 
            st.subheader("Use MyApp")

            # Membuat pie chart dengan Altair untuk 'Use MyApp'
            pie7 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Use MyApp:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie7, use_container_width=True)

        with viz2:
            st.subheader("Payment Method")

            # Membuat pie chart dengan Altair untuk 'Payment Method'
            pie8 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Payment Method:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
            )
            .properties(
                width=300, height=300
            )
            .configure_title(fontSize=16)
            )

            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie8, use_container_width=True)

        with viz3:
            st.subheader("Music Product")

            # Membuat pie chart dengan Altair untuk 'Music Product'
            pie9 = (
                alt.Chart(df)
                .mark_arc()
                .encode(
                    color=alt.Color('Music Product:N', scale=alt.Scale(scheme='category20c')),
                    theta=alt.Theta('count():Q', title='Frequency')
                )
                .properties(
                    width=300, height=300
                )
                .configure_title(fontSize=16)
            )
            # Menampilkan pie chart di Streamlit
            st.altair_chart(pie9, use_container_width=True)
import pickle
model_filename = 'random_forest_model.pkl'

with open(model_filename, 'rb') as file:
    rfc = pickle.load(file)

def map_selected_value(selected_value, mapping):
    return [key for key, value in mapping.items() if value == selected_value][0]

def customer_churn_prediction():
    st.header('Customer Churn Prediction')

    # Membuat kamus untuk pemetaan nama kategori
    device_class_mapping = {2: 'Mid End', 0: 'High End', 1: 'Low End'}
    games_product_mapping = {2: 'Yes', 0: 'No', 1: 'No internet service'}
    music_product_mapping = {2: 'Yes', 0: 'No', 1: 'No internet service'}
    education_product_mapping = {0: 'No', 2: 'Yes', 1: 'No internet service'}
    call_center_mapping = {0: 'No', 1: 'Yes'}
    video_product_mapping = {0: 'No', 2: 'Yes', 1: 'No internet service'}
    use_my_app_mapping = {0: 'No', 2: 'Yes', 1: 'No internet service'}
    payment_method_mapping = {2: 'Digital Wallet', 3: 'Pulsa', 1: 'Debit', 0: 'Credit'}

    # Bagi tata letak menjadi dua kolom
    col1, col2 = st.columns(2)

    # Input variabel untuk kolom pertama
    with col1:
        tenure_months = st.number_input('Tenure Months')
        selected_device_class = st.selectbox('Device Class', list(device_class_mapping.values()))
        selected_games_product = st.selectbox('Games Product', list(games_product_mapping.values()))
        selected_music_product = st.selectbox('Music Product', list(music_product_mapping.values()))
        selected_education_product = st.selectbox('Education Product', list(education_product_mapping.values()))

    # Input variabel untuk kolom kedua
    with col2:
        selected_call_center = st.selectbox('Call Center', list(call_center_mapping.values()))
        selected_video_product = st.selectbox('Video Product', list(video_product_mapping.values()))
        selected_use_my_app = st.selectbox('Use MyApp', list(use_my_app_mapping.values()))
        selected_payment_method = st.selectbox('Payment Method', list(payment_method_mapping.values()))
        monthly_purchase = st.number_input('Monthly Purchase')
        cltv = st.number_input('CLTV')

    # Menggunakan fungsi pemetaan untuk mengonversi data kategorikal ke numerik
    selected_device_class = map_selected_value(selected_device_class, device_class_mapping)
    selected_games_product = map_selected_value(selected_games_product, games_product_mapping)
    selected_music_product = map_selected_value(selected_music_product, music_product_mapping)
    selected_education_product = map_selected_value(selected_education_product, education_product_mapping)
    selected_call_center = map_selected_value(selected_call_center, call_center_mapping)
    selected_video_product = map_selected_value(selected_video_product, video_product_mapping)
    selected_use_my_app = map_selected_value(selected_use_my_app, use_my_app_mapping)
    selected_payment_method = map_selected_value(selected_payment_method, payment_method_mapping)

    user_input = {
        'Tenure Months': tenure_months,
        'Device Class': selected_device_class,
        'Games Product': selected_games_product,
        'Music Product': selected_music_product,
        'Education Product': selected_education_product,
        'Call Center': selected_call_center,
        'Video Product': selected_video_product,
        'Use MyApp': selected_use_my_app,
        'Payment Method': selected_payment_method,
        'Monthly Purchase': monthly_purchase,
        'CLTV': cltv
    }

    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])

    if st.button('Predict Churn'):
        # Prediksi churn
        prediction = rfc.predict(input_df)

        # Membuat pemetaan untuk hasil prediksi
        churn_mapping = {0: 'Customer Not Churn', 1: 'Customer Churn'}

        # Menampilkan output prediksi dengan spinner
        with st.spinner("Tunggu Sebentar, Sedang Proses Prediksi..."):
            time.sleep(1)  # Hanya contoh, bisa dihapus jika tidak diperlukan
            result_message = f"Hasil Prediksi: {churn_mapping.get(prediction[0], 'Tidak Diketahui')}"
            if prediction[0] == 0:
                st.success(result_message)
            else:
                st.warning(result_message)


if selected == 'Prediction':
    customer_churn_prediction()
