# Dockerfile

# FROM base image to build upon
FROM phusion/baseimage

# RUN install python and pip
RUN apt-get update
RUN apt-get install -y python python-pip python-dev 


ENV PROJECT=mysite
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT


WORKDIR $CONTAINER_PROJECT

COPY . $CONTAINER_PROJECT

RUN pip install -r requirements.txt


# COPY start.sh into known container location 

COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD execute start.sh to start the server running.

CMD ["/start.sh"]
# done!