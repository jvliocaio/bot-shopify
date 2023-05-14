FROM selenium/standalone-firefox-debug
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip
RUN pip3 install selenium

COPY geckodriver /usr/bin
#RUN ln -s /firefox/firefox /usr/bin/firefox
WORKDIR /app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY shop.py .
RUN touch geckodriver.log
#CMD ["bash", "-c", "while true; do python3 shop.py; sleep 3600; done; > 2>&1"]