FROM alpine:latest
RUN apk update && apk add python python-dev g++ git
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install

FROM alpine:latest
RUN apk update && apk add python py-setuptools
COPY --from=0 /usr/lib/python2.7/site-packages/Adafruit_DHT-1.3.2-py2.7-linux-armv7l.egg /usr/lib/python2.7/site-packages/Adafruit_DHT-1.3.2-py2.7-linux-armv7l.egg
RUN echo "./Adafruit_DHT-1.3.2-py2.7-linux-armv7l.egg" > /usr/lib/python2.7/site-packages/adafruit.pth
ADD sensor.py /sensor.py
RUN chmod 755 /sensor.py
CMD /sensor.py

