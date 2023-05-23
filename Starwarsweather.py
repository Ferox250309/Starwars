import streamlit as st
import requests
import json
from PIL import Image


st.set_page_config(page_title="Star Wars weather Aarhus", page_icon=":flag_denmark:", layout="wide")

st.subheader("Star Wars weather Aarhus")

response = requests.get("https://api.weatherapi.com/v1/current.json?key=36fec4787ae4493db02202139232005&q=Aarhus&aqi=no")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

if response.status_code == 200:
    data = response.json()
    text = jprint(data)  # Print the JSON data and get the text variable

elif response.status_code == 404:
    print("Unable to reach URL.")
else:
    print("Unable to connect to API or retrieve data.")

def getdata(text):
    y = json.loads(text)
    temp = y["current"]["temp_c"]
    return temp

if response.status_code == 200:
    temperature = getdata(text)
    if temperature < -10:
        add_bg_from_url():
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://cdnb.artstation.com/p/assets/images/images/001/793/559/large/jaromir-hrivnac-20160103iiiiiiiii.jpg?1452809128");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
             )

        add_bg_from_url() 
        st.title("Feels like Hoth")
        st.write(str(temperature) + "°C. Weather like on Hoth")
        st.write("Better put on a jacket")
    if -10 <= temperature <= 43:
        def add_bg_from_url():
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://comicyears.com/wp-content/uploads/2020/04/7.jpg");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
             )

        add_bg_from_url() 
        st.title("Feels like Tatooine")
        st.write(str(temperature) + "°C. Tatooine-like weather.")


