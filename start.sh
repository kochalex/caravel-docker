#!/bin/bash
#fabmanager create-admin --app caravel --username admin --firstname caravel --lastname Administrator --email admin@test.com --password 1234
if [ -n "$CARAVEL_USERNAME" -a -n "$CARAVEL_PASSWORD" -a -n "$CARAVEL_FIRSTNAME" -a -n "$CARAVEL_LASTNAME" -a -n "$CARAVEL_EMAIL" ];
then
  USERNAME=$CARAVEL_USERNAME;
  PASSWORD=$CARAVEL_PASSWORD;
  FIRSTNAME=$CARAVEL_FIRSTNAME;
  LASTNAME=$CARAVEL_LASTNAME;
  EMAIL=$CARAVEL_EMAIL;
else
  USERNAME=admin;
  PASSWORD=admin;
  FIRSTNAME=caravel;
  LASTNAME=Administrator;
  EMAIL="admin@test.com";
fi

fabmanager create-admin --app caravel --username $USERNAME --firstname $FIRSTNAME --lastname $LASTNAME --email $EMAIL --password $PASSWORD
caravel db upgrade
caravel init
caravel runserver

# if [ `./init_check.py` = 1 ];
# then
#   fabmanager create-admin --app caravel --username $USERNAME --firstname $FIRSTNAME --lastname $LASTNAME --email $EMAIL --password $PASSWORD
#   caravel db upgrade
#   caravel init
#   caravel runserver
# else
#   caravel runserver
# fi
