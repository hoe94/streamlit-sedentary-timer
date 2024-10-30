import streamlit as st
from helper import timer_helper


st.markdown(
    """
    <style>
    .time {
        font-size: 100px !important;
        font-weight: 700 !important;
        color: #ec5953 !important;
    }

    .stApp {
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }
    </style>
    """,
    unsafe_allow_html=True
)


def header(url, background_color_code, font_color_code):
    st.markdown(f'<p style="background-color:{background_color_code};color:{font_color_code};font-size:42px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


def main():
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/sedentary.png", width = 150, output_format = "auto")
        st.title("Sedentary Timer")
        #header("Sedentary Timer", "#ffffff", "#070707")

    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=1)
    time_in_seconds = time_minutes * 60

    if st.button('🔴 START'):
        timer_helper.count_down(int(time_in_seconds))
        header("Standup!!", "#cc0300", "#fbf8f8")

    if st.button("STOP Music"):
        timer_helper.stop_sound()
    
    
if __name__ == '__main__':
    main()