# set base image (host OS)
FROM python:3.8-alpine as builder

# set the working directory in the container
WORKDIR /

COPY . .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 12345
# command to run on container start
CMD [ "python3", "padding_oracle.py" ]