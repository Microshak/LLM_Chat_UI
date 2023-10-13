FROM python:3.9.16-bullseye


RUN useradd -m llm

WORKDIR /home/llm

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY app app
COPY boot.sh ./

ENV NUM_WORKERS 10
ENV TIMEOUT 6000

RUN chown -R app:app . && \
    chmod +x boot.sh
USER app

EXPOSE 5000
#ENTRYPOINT ["./boot.sh"]
# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:5000/health
CMD ["gunicorn"  , "-b", "0.0.0.0:5000","--workers","10","--timeout","555555","--threads","10" ,"app:app"]