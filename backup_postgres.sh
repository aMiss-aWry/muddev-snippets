#!/bin/bash
# Backup script for postgresql db

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <OUTPUT_FOLDER> <DB_NAME> <DB_USER>"
    exit 1
fi

OUTPUT_FOLDER=$1
DB_NAME=$2
DB_USER=$3

OUTPUT_FILE=$(date +"%Y-%m-%d.%H_%M_%S.sql")
OUTPUT_FILE_PATH="$OUTPUT_FOLDER/$OUTPUT_FILE"

mkdir -p $OUTPUT_FOLDER

# Dump the database
pg_dump -U $DB_USER -W -F p $DB_NAME > $OUTPUT_FILE_PATH

if [ $? -eq 0 ]; then
    echo "Database backed up in server/backups/$OUTPUT_FILE_PATH"
else
    echo "Database backup failed."
fi
