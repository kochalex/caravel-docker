#!/bin/bash
fabmanager create-admin --app caravel --username admin --firstname caravel --lastname Administrator --email admin@test.com --password admin
caravel db upgrade
caravel init
caravel runserver
