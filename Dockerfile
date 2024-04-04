FROM python:3.9.12-slim


WORKDIR /app


COPY ./model /app/model
COPY ./utils /app/utils
COPY ./main.py /app
COPY ./requirements.txt /app


RUN pip install virtualenv
RUN python -m virtualenv venv


RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt




EXPOSE 80







ENTRYPOINT [ "streamlit" , "run" ]



CMD [ "main.py" ]
