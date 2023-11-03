FROM nvcr.io/nvidia/tensorflow:23.10-tf2-py3


RUN useradd -m user

WORKDIR /home/worker
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .
RUN  pip install -r requirements.txt

CMD ["python3"  , "image.py"]