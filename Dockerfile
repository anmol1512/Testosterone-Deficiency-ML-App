FROM python:3.9.12




COPY ./model /app/model
COPY ./utils /app/utils
COPY ./main.py /app
COPY ./requirements.txt /app




WORKDIR /app



RUN pip install -r requirements.txt



EXPOSE 80



RUN mkdir ~/.streamlit



COPY config.toml ~/.streamlit/config.toml
COPY credentials.toml ~/.streamlit/credentials.toml



ENTRYPOINT [ "streamlit" , "run" ]



CMD [ "main.py" ]
