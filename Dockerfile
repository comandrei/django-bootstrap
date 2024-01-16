FROM python:3.12
# Instalez dependinte
RUN pip3 install django
# Adaug cod
ADD my_project my_project
WORKDIR my_project
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
