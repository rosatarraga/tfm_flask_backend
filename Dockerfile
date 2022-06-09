# start by pulling the python image
FROM python:3.7.10-alpine3.13

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /requirements.txt
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev mariadb-dev libffi-dev openblas-dev libgfortran lapack-dev build-base openssl-dev
RUN apk add --no-cache hdf5-dev
RUN pip install -r /requirements.txt
RUN apk --no-cache del build-base

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]