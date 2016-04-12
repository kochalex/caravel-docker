FROM python:2.7.11

# Install caravel
RUN pip install caravel

RUN pip install mysqlclient

RUN mkdir /caravel

COPY . /caravel/

WORKDIR /caravel

RUN chmod a+x /caravel/start.sh
RUN chmod a+x /caravel/init_check.py

ENV PYTHONPATH  /caravel/
# expose port
EXPOSE 8088

# Start the development web server
CMD ["/caravel/start.sh"]
