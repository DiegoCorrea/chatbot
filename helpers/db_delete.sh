#!/usr/bin/env bash
db_name='chatbot_local_db';
commands=" DROP DATABASE \`${db_name}\`;"
echo "${commands}" | sudo mysql -u root -p
rm -rf ./media/*
