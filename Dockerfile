FROM python:3.6.15

RUN pip install Flask requests uwsgi

COPY app /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python api.py

# it should normally run with prod web server
#CMD uwsgi --master \
#    --single-interpreter \
#    --workers $WORKERS \
#    --gevent $ASYNC_CORES \
#    --protocol $PROTOCOL \
#    --socket 0.0.0.0:3000 \
#   --module patched:app