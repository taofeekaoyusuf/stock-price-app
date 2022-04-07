FROM python:3.10-alpine
WORKDIR /stockpriceapp
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . /stockpriceapp
ENTRYPOINT ["streamlit", "run"]
CMD ["stockpriceapp.py"]