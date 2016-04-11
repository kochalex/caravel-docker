FROM python:2.7.11

# Install caravel
RUN pip install caravel

RUN pip install mysqlclient

RUN mkdir /caravel

COPY . /caravel/

WORKDIR /caravel

RUN chmod a+x /caravel/start.sh

# expose port
EXPOSE 8088

# Start the development web server
CMD ["/caravel/start.sh"]
