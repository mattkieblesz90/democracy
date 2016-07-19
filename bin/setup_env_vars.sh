#!/bin/sh

export DJANGO_SETTINGS_MODULE="conf.settings"
export DJANGO_SECRET_KEY="akr2icmg1n8%z^3fe3c+)5d0(t^cy-2_25rrl35a7@!scna^1#"
export DATABASE_USER="democracy"
export DATABASE_PASSWORD="democracy"
export STATIC_ROOT=/home/mat/Projects/democracy/collected_static

# for ansible file encryption
export ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_pass.txt
export ssh_pass="yvlsQ>Zb>D+2I&1\k#Z*XEo/5vu|H1asKypd#Zlxd4;PW+).R-Z?^q'9)X/}_c#"