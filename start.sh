#!/bin/bash
/usr/local/bin/fabmanager create-admin --app caravel < /caravel/admin.config
caravel db upgrade
caravel init

caravel runserver
