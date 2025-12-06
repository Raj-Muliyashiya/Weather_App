import requests
import streamlit as st



Weather_API_key = st.secrets.get("openweather", {}).get("api_key")

st.set_page_config(


    page_title="Weather App",
    page_icon="cloudy.png",
    layout="wide"
)

st.title("Weather App🌥️")

col1 ,col2, col3 = st.columns(3)

with col2:
    city_name = st.text_input("",placeholder="City Name").strip()


def weather():

    if not city_name:
        return
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Weather_API_key}"

    weather_respons = requests.get(weather_url, timeout=10)
    data = weather_respons.json()

    if data["cod"] == 200:

        st.space("medium")
        colls1,colls2,colls3,colls4,colls5 = st.columns(5)

        with colls3:
            icon = data["weather"][0]["icon"] 
            url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
            st.image(url, width=80)

        cols1,cols2,cols3,cols4,cols5 = st.columns(5,gap="medium")

        with cols1:
            st.metric(label="City",value=data["name"])

        with cols2:
            st.metric(label="Temperature",value=f"{round(data['main']['temp']-273.15)}°C")

        with cols3:
            st.metric(label="Weather",value=data["weather"][0]["main"]) 

        with cols4:
            st.metric(label="Wind Speed", value=f"{round(data['wind']['speed']*2.237)} M/H")
        
        with cols5:
            st.metric(label="clouds", value=data["clouds"]["all"])

    else:
        st.warning("Unable to locate City, Check The Spelling")


weather()