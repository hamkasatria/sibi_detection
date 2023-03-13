FROM python:3.8

RUN apt-get update

RUN pip install icevision[inference]
RUN pip install icedata
RUN pip install gradio
# RUN pip install icevision[all]
# # RUN wget https://raw.githubusercontent.com/airctic/icevision/master/icevision_install.sh
# # RUN bash icevision_install.sh cuda11 master

# RUN pip install gradio -U -q

COPY . /app
WORKDIR /app    

ENTRYPOINT ["python"]
CMD ["app.py"]

# Dockerfile: with instructions on what to add to the IceVision image



## ---------------------------
# FROM python:3.8
# RUN pip install PyYAML>=5.1 -U
# RUN pip install datascience -U
# RUN pip install torchtext==0.9.0 -U
# RUN pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html -U
# RUN pip install fastai==2.3.1 -U
# RUN pip install git+git://github.com/airctic/icevision.git#egg=icevision[all] -U
# RUN pip install git+git://github.com/airctic/icedata.git -U
# RUN pip install yolov5-icevision -U 
# RUN pip install mmcv-full==1.3.7 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.8.0/index.html -U
# RUN pip install mmdet==2.13.0 -U
# RUN pip install ipywidgets -U