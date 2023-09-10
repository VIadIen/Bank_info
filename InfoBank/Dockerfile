FROM python:3
RUN apk add git && git clone https://github.com/VIadIen/TestSberTech.git TestSberTechQA
WORKDIR /TestSberTechQA/InfoBank
EXPOSE 0.0.0.0:4000:4005
CMD ["python", "server.py"]

