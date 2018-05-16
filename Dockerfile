FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install psutil
RUN mkdir /script
WORKDIR /script
ADD https://github.com/Leanivets/TestScript/raw/master/metrics.py /script/
RUN chmod +x /script/metrics.py
ENTRYPOINT ["./metrics.py"]
CMD ["all"]