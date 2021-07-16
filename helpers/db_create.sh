#!/usr/bin/env bash
newDb='chatbot_local_db';
newUser='chatbot_local_user';
newDbPassword='chatbot_local_pwd';
host='%';
commands="CREATE DATABASE \`${newDb}\` CHARACTER SET utf8;GRANT USAGE ON *.* TO '${newUser}'@'${host}' IDENTIFIED BY '${newDbPassword}';GRANT ALL privileges ON \`${newDb}\`.* TO '${newUser}'@'${host}';FLUSH PRIVILEGES;"
echo "${commands}" | sudo mysql -u root -p
