!/bin/sh
#. venv/bin/activate
# flask db upgrade
# flask translate compile

#echo "start gunicorn with $NUM_WORKERS workers and timeout value $TIMEOUT"
gunicorn  --bind 0.0.0.0:5000 --workers=10 --threads=10 --timeout 2200  app:app 
