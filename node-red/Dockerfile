ARG TAG=rpi
FROM nodered/node-red-docker:${TAG}

USER root

# TEST -> DHT222
# RUN wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.5.tar.gz && \
#     tar zxvf bcm2835-1.55.tar.gz && \
#     cd bcm2835-1.55 && \
#     ./configure && \
#     make && \
#     make check && \
#     make install && cd ..

RUN apt-get update && apt-get install -y
RUN apt-get update && apt-get install -y gcc \
    make \
    build-essential \
    libavahi-compat-libdnssd-dev

USER node-red
# RUN npm update

RUN npm install node-red-contrib-owfs
RUN npm install node-red-contrib-mqtt-broker
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-ds18b20-sensor

# TEST
# RUN npm install node-red-contrib-homekit
RUN npm install node-red-contrib-pythonshell
# RUN npm install node-red-contrib-google-home-notify
# RUN npm install --unsafe-perm node-dht-sensor && \
#     npm install --unsafe-perm node-red-contrib-dht-sensor
