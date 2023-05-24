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
    st.error("Unable to reach URL.")
else:
    st.error("Unable to connect to API or retrieve data.")

def getdata(text):
    y = json.loads(text)
    temp = y["current"]["temp_c"]
    return temp

def getweather(text):
    y = json.loads(text)
    weather = y["current"]["condition"]["text"]
    return weather

if response.status_code == 200:
    temperature = getdata(text)
    weathertoday = getweather(text)

    if temperature < 0:
        if weathertoday == "Cloudy" or weathertoday == "Partly cloudy":
            st.markdown(
                """
                <style>
                .stApp {{
                    background-image: url("https://cdnb.artstation.com/p/assets/images/images/001/793/559/large/jaromir-hrivnac-20160103iiiiiiiii.jpg?1452809128");
                    background-attachment: fixed;
                    background-size: cover;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        elif weathertoday == "clear":
            st.markdown(
                """
                <style>
                .stApp {{
                    background-image: url("https://github.com/Vroomfrondal/Star-Wars-Weather/blob/main/images/coruscant-night.jpg?raw=true");
                    background-attachment: fixed;
                    background-size: cover;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        elif weathertoday == "rain" or "Patchy rain possible" or "Patchy light rain" or "Light rain" or "Moderate rain at times" or "Moderate rain" or "Heavy rain at times" or "Heavy rain" or "Light freezing rain" or "Moderate or heavy freezing rain" or "Light rain shower" or "Moderate or heavy rain shower" or "Torrential rain shower" or "Patchy light rain with thunder" or "Moderate or heavy rain with thunder":
            st.markdown(
                """
                <style>
                .stApp {{
                    background-image: url("https://images.squarespace-cdn.com/content/v1/5fbc4a62c2150e62cfcb09aa/bb00eb67-6495-465e-820c-2d41f481f075/tumblr_b29b936a28c62e42a412b9a269ff83ad_fd215628_1280.jpg");
                    background-attachment: fixed;
                    background-size: cover;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                .stApp {{
                    background-image: url("https://imagedelivery.net/9sCnq8t6WEGNay0RAQNdvQ/UUID-cl9ehesyw1017qqom0lkrckex/public");
                    background-attachment: fixed;
                    background-size: cover;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

        st.title("Feels like Hoth")
        st.write(str(temperature) + "°C. Weather like on Hoth")
        st.write("Better put on a jacket")
    if temperature >= 40:
        if weathertoday == "Sunny":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://media.wired.com/photos/5954651b38978176dacc5b06/3:2/w_1600%2Cc_limit/He_Tatooine_19.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
        if weathertoday == "Cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://cdna.artstation.com/p/assets/images/images/010/188/366/large/gimena-ferrari-tattoinebinarysunset.jpg?1523042202");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
        if weathertoday == "Partly cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://cdna.artstation.com/p/assets/images/images/010/188/366/large/gimena-ferrari-tattoinebinarysunset.jpg?1523042202");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
        else:
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://w0.peakpx.com/wallpaper/987/752/HD-wallpaper-tatooine-dust-storm-scene-star-wars-battlefront-live-youtube-star-wars-desert.jpg");
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
    if 0 <= temperature <= 5:
        weathertoday = getweather(text)
        if weathertoday == "Cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://66.media.tumblr.com/02c239052e0822ea073b60b09267753d/tumblr_oa6w4unWhi1uf0h9xo1_1280.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Rhen Var")
            st.write(str(temperature) + "°C. Ren Var-like weather.")
        if weathertoday == "Partly cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://66.media.tumblr.com/02c239052e0822ea073b60b09267753d/tumblr_oa6w4unWhi1uf0h9xo1_1280.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Rhen Var")
            st.write(str(temperature) + "°C. Ren Var-like weather.")
        if weathertoday == "Fog":
            def add_bg_from_url():
                st.markdown(
                    f"""
                            <style>
                            .stApp {{
                                background-image: url("https://db4sgowjqfwig.cloudfront.net/campaigns/157048/assets/697322/Rhen_var.jpg?1486692550");
                                background-attachment: fixed;
                                background-size: cover
                            }}
                            </style>
                            """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Rhen Var")
            st.write(str(temperature) + "°C. Ren Var-like weather.")
        if weathertoday == "Sunny":
            def add_bg_from_url():
                st.markdown(
                    f"""
                            <style>
                            .stApp {{
                                background-image: url("https://static.wikia.nocookie.net/starwars/images/7/7d/ForgottenSithTemple-EotEEtU.jpg/revision/latest?cb=20130808165307");
                                background-attachment: fixed;
                                background-size: cover
                            }}
                            </style>
                            """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Rhen Var")
            st.write(str(temperature) + "°C. Ren Var-like weather.")
        else:
            def add_bg_from_url():
                st.markdown(
                    f"""
                            <style>
                            .stApp {{
                                background-image: url("https://static.wikia.nocookie.net/starwars/images/7/7d/ForgottenSithTemple-EotEEtU.jpg/revision/latest?cb=20130808165307");
                                background-attachment: fixed;
                                background-size: cover
                            }}
                            </style>
                            """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Rhen Var")
            st.write(str(temperature) + "°C. Ren Var-like weather.")
    if 5 <= temperature <= 10:
        if weathertoday == "Sunny":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://pm1.aminoapps.com/7621/f0855d03f0c81856c1860ff818f28ae558ba4589r1-1920-1080v2_uhq.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Endor")
            st.write(str(temperature) + "°C. Endor-like weather.")
        if weathertoday == "Cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3e954c54-d0a2-4aef-9a06-d9ca6419da97/ddfba4u-55eccc09-f132-4fca-af19-a80ea4056881.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNlOTU0YzU0LWQwYTItNGFlZi05YTA2LWQ5Y2E2NDE5ZGE5N1wvZGRmYmE0dS01NWVjY2MwOS1mMTMyLTRmY2EtYWYxOS1hODBlYTQwNTY4ODEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.gdS6F0OmDc7NGoxS5EEYdvj44rkPEptVcjY8EvWk8a8");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Endor")
            st.write(str(temperature) + "°C. Endor-like weather.")
        if weathertoday == "Partly cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3e954c54-d0a2-4aef-9a06-d9ca6419da97/ddfba4u-55eccc09-f132-4fca-af19-a80ea4056881.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNlOTU0YzU0LWQwYTItNGFlZi05YTA2LWQ5Y2E2NDE5ZGE5N1wvZGRmYmE0dS01NWVjY2MwOS1mMTMyLTRmY2EtYWYxOS1hODBlYTQwNTY4ODEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.gdS6F0OmDc7NGoxS5EEYdvj44rkPEptVcjY8EvWk8a8");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Endor")
            st.write(str(temperature) + "°C. Endor-like weather.")
        else:
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://femto.scrolller.com/endor-redwoods-jedediah-smith-redwoods-state-park-646p9somdx.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Endor")
            st.write(str(temperature) + "°C. Endor-like weather.")
    if 10 <= temperature <= 15:
        if weathertoday == "Sunny":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://pbs.twimg.com/media/D43ndl0UwAEBwYr?format=jpg&name=4096x4096");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Naboo")
            st.markdown("<h1 style='text-align: center; color: white;'>Naboo</h1>" , unsafe_allow_html=True)
            st.write(str(temperature) + "°C. Naboo-like weather.")
        if weathertoday == "Cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://media.contentapi.ea.com/content/dam/walrus/images/2018/11/mapvista-theed-grid.jpg.adapt.crop191x100.628p.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Naboo")
            st.markdown("<h1 style='text-align: center; color: white;'>Naboo</h1>", unsafe_allow_html=True)
            st.write(str(temperature) + "°C. Naboo-like weather.")
        if weathertoday == "Partly cloudy":
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://media.contentapi.ea.com/content/dam/walrus/images/2018/11/mapvista-theed-grid.jpg.adapt.crop191x100.628p.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Naboo")
            st.markdown("<h1 style='text-align: center; color: white;'>Naboo</h1>", unsafe_allow_html=True)
            st.write(str(temperature) + "°C. Naboo-like weather.")
        else:
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://rare-gallery.com/uploads/posts/4579455-star-wars-naboo-digital-art.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url()
            st.title("Feels like Naboo")
            st.markdown("<h1 style='text-align: center; color: white;'>Naboo</h1>", unsafe_allow_html=True)
            st.write(str(temperature) + "°C. Naboo-like weather.")
