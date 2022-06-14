# start by pulling the python image
FROM python:3.7

RUN mkdir /app
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# switch working directory
WORKDIR /app

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]