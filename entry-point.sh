#!/bin/bash
mkdir /app/logs
touch /etc/supervisor/conf.d/supervisord.conf
j2 /app/conf/supervisord.conf.j2 > /etc/supervisor/conf.d/supervisord.conf
exec supervisord -n
