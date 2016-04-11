FROM python:2.7.11

# Install caravel
RUN pip install caravel

RUN pip install mysqlclient

RUN mkdir /caravel

COPY . /caravel/

WORKDIR /caravel

# Create an admin user
RUN /usr/local/bin/fabmanager create-admin --app caravel < /caravel/admin.config

# Initialize the database
RUN caravel db upgrade

# Create default roles and permissions
RUN caravel init

# expose port
EXPOSE 8088

# Start the development web server
CMD ["caravel","runserver"]
