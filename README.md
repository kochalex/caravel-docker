### This is a Dockerfile of Caravel

#### need to set up this environment variables
+ CARAVEL_USERNAME
+ CARAVEL_PASSWORD
+ CARAVEL_FIRSTNAME
+ CARAVEL_LASTNAME
+ CARAVEL_EMAIL

+ POSTGRESQL_ENV_POSTGRES_USER
+ POSTGRESQL_ENV_POSTGRES_PASSWORD
+ POSTGRESQL_ENV_POSTGRES_DB
+ POSTGRESQL_PORT_5432_TCP_ADDR
+ POSTGRESQL_PORT_5432_TCP_PORT


Caravel
=========
<img src="http://i.imgur.com/H0Kyvyi.jpg" style="border-radius: 20px; box-shadow:5px 5px 5px gray;" alt="Caravel" width="500"/>


Caravel is a data exploration platform designed to be visual, intuitive
and interactive.

[this project used to be named **Panoramix**]


Video - Introduction to Caravel
---------------------------------
[![Caravel - ](http://img.youtube.com/vi/3Txm_nj_R7M/0.jpg)](http://www.youtube.com/watch?v=3Txm_nj_R7M)

Screenshots
------------
![img](http://i.imgur.com/JRbTnTx.png)
![img](http://i.imgur.com/4wRtxwb.png)

Caravel
---------
Caravel's main goal is to make it easy to slice, dice and visualize data.
It empowers users to perform **analytics at the speed of thought**.

Caravel provides:
* A quick way to intuitively visualize datasets by allowing users to create
    and share interactive dashboards
* A rich set of visualizations to analyze your data, as well as a flexible
    way to extend the capabilities
* An extensible, high granularity security model allowing intricate rules
    on who can access which features, and integration with major
    authentication providers (database, OpenID, LDAP, OAuth & REMOTE_USER
    through Flask AppBuiler)
* A simple semantic layer, allowing to control how data sources are
    displayed in the UI, by defining which fields should show up in
    which dropdown and which aggregation and function (metrics) are
    made available to the user
* Deep integration with Druid allows for Caravel to stay blazing fast while
    slicing and dicing large, realtime datasets
