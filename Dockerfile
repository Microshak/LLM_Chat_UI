FROM nvcr.io/nvidia/tensorflow:23.10-tf2-py3


RUN useradd -m app

WORKDIR /home/llm

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY chat chat

ENV NUM_WORKERS 10
ENV TIMEOUT 6000

RUN chown -R chat:app . 
USER app

EXPOSE 5000
CMD ["gunicorn"  , "-b", "0.0.0.0:5000","--workers","10","--timeout","555555","--threads","10" ,"chat:app"]