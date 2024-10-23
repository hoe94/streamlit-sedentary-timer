import streamlit as st
import time
import pygame
#from playsound import playsound
import threading

pygame.mixer.init()
alarm_sound = "assets/alarm.mp3"

def header(url):
    st.markdown(f'<p style="background-color:#cc0300;color:#fbf8f8;font-size:42px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

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
    threading.Thread(target=play_sound).start()

def count_down(ts):
    global timer_finished
    with st.empty():
        while ts > 0:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
        notify()
        


def main():
    global timer_finished, sound_playing

    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/sedentary.png", width = 150, output_format = "auto")
        st.title("Sedentary Timer")

    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=1)
    time_in_seconds = time_minutes * 60

    if st.button("START"):
        count_down(int(time_in_seconds))
        header("Standup!!")

    #if st.session_state.timer_finished and st.session_state.sound_playing:
    if st.button("Stop Music"):
        stop_sound()
    
    
        
if __name__ == '__main__':
    main()