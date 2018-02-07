ARG TAG=rpi
FROM nodered/node-red-docker:${TAG}

RUN npm install node-red-contrib-owfs
RUN npm install node-red-contrib-mqtt-broker
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-ds18b20-sensor

# TEST
RUN npm install node-red-contrib-pythonshell

# RUN apt-get update && apt-get install gcc make build-essential
# RUN npm update
