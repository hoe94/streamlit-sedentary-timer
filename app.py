import streamlit as st
import time

st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
        if time_now < '00:01':
            st.write("Standup!!")

def main():
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/sedentary.png", width = 150, output_format = "auto")
        st.title("Sedentary Timer")

    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=1)
    time_in_seconds = time_minutes * 60
    if st.button("START"):
        count_down(int(time_in_seconds))
        st.write("Standup!!")
        
if __name__ == '__main__':
    main()