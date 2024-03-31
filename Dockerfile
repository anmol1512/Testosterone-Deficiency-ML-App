FROM python:3.9.12-slim




COPY ./model /app/model
COPY ./utils /app/utils
COPY ./main.py /app
COPY ./requirements.txt /app




WORKDIR /app



RUN pip install -r requirements.txt



EXPOSE 80







ENTRYPOINT [ "streamlit" , "run" ]



CMD [ "main.py" ]
