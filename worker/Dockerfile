FROM nvcr.io/nvidia/tensorflow:23.10-tf2-py3


#RUN useradd -m user

WORKDIR /home/worker
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./worker /home/worker
RUN  pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt

#CMD ["python3"  , "timage.py"]