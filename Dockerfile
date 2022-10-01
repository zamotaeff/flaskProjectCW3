FROM python:3.9.2-alpine

# upgrade pip
RUN pip install --upgrade pip

# get curl for healthchecks
RUN apk add curl

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .

# python setup
#RUN python -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#RUN export FLASK_APP=run.py
#RUN export FLASK_DEBUG=False
RUN pip install --no-cache -r requirements.txt

COPY . .

# define the port number the container should expose
#EXPOSE 5000

#CMD ["python", "run.py"]
ENTRYPOINT ["sh", "entrypoint.sh"]
