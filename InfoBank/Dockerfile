FROM python:3
RUN apk add git && git clone https://github.com/VIadIen/TestSberTech.git TestSberTech
WORKDIR /TestSberTech/InfoBank
EXPOSE 0.0.0.0:4000:4005
CMD ["python", "server.py"]

