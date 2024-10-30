FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    alsa-utils \
    pulseaudio \
    libasound2 \
    libglib2.0-0 \ 
    libasound2-plugins

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]