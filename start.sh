#!/bin/bash
fabmanager create-admin --app caravel --username admin --firstname caravel --lastname Administrator --email admin@test.com --password 1234
echo "create user"
caravel db upgrade
echo "db upgrade"
caravel init
echo "app init"
caravel runserver
