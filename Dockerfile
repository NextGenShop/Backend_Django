FROM python:3
WORKDIR /src

ENV PYTHONUNBUFFERED=1

COPY isolated_shopping/requirements.txt /src/
RUN pip install -r requirements.txt
COPY isolated_shopping /src/

RUN python manage.py loaddata MockSupermarketDataset.json

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
