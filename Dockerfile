FROM python:3.10.4-slim

RUN mkdir /stockpriceapp

WORKDIR /stockpriceapp

COPY . /stockpriceapp

RUN pip install -r requirements.txt
# RUN apt-get update
# RUN pip3 install streamlit
# RUN pip3 install yfinance

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["stockpriceapp.py"]
