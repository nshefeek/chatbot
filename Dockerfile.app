FROM python:3.9.4

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/prediction_app

ADD ./prediction_app /opt/prediction_app
RUN pip install --upgrade pip
RUN pip install -r /opt/prediction_app/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]