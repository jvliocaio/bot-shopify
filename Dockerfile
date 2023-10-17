FROM selenium/standalone-chrome-debug

ENV TZ=America/Sao_Paulo
# $ echo "America/Sao_Paulo" > /etc/timezone
# $ dpkg-reconfigure -f noninteractive tzdata
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip
#RUN pip3 install selenium

#COPY geckodriver /usr/bin
#RUN ln -s /firefox/firefox /usr/bin/firefox
WORKDIR /app

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN sudo dpkg -i google-chrome-stable_current_amd64.deb

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY shop.py .

RUN touch geckodriver.log
#CMD ["bash", "-c", "while true; do python3 shop.py; sleep 3600; done; > 2>&1"]

#RUN sudo echo "0 * * * * python3 /app/script.py" > /etc/crontab

