FROM python:3.8

RUN apt-get update

# RUN pip install icevision[all]
RUN wget https://raw.githubusercontent.com/airctic/icevision/master/icevision_install.sh
RUN bash icevision_install.sh cuda11 master

RUN pip install gradio -U -q

COPY . /app
WORKDIR /app    

ENTRYPOINT ["python"]
CMD ["app.py"]