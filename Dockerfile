FROM python:3.8
WORKDIR /rlenv
# Set PYTHONUNBUFFERED to ensure that Python output is sent immediately to the console
ENV PYTHONUNBUFFERED=1
COPY sasrl_env/runServer.py ${SRC_DIR}/

# install box2d
RUN apt-get install -y swig
RUN pip install gym['box2d']

# isntall sasrl-env
RUN pip install sasrl-env

CMD ["python", "runServer.py"]

