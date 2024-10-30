import pygame
import streamlit as st
import time
import threading

pygame.mixer.init()
alarm_sound = "assets/alarm.mp3"

# Function to play notification sound
def play_sound():
    pygame.mixer.music.load(alarm_sound)
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.stop()

# Function to stop the sound
def stop_sound():
    if pygame.mixer.music.get_busy():  # Check if the sound is playing
        pygame.mixer.music.stop()
        st.write("Music stopped.")
    else:
        st.write("No music is playing at the moment.")


def notify():
    st.balloons() # Ballon will show up
    threading.Thread(target=play_sound).start() # Using thread to execute play_sound() function


def count_down(ts): # Core function for timer app
    with st.empty():
        while ts > 0:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.markdown( f"""<p class="time">{time_now}</p>""",unsafe_allow_html=True)
            time.sleep(1)
            ts -= 1
        notify()