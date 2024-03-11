FROM python:3.12
# Instalez dependinte
RUN apt-get update && apt-get install build-essential graphviz graphviz-dev --assume-yes
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Adaug cod
RUN mkdir /my_project
ADD my_project /my_project
WORKDIR /my_project
EXPOSE 8000
ENTRYPOINT ["./docker_entrypoint.sh"]
