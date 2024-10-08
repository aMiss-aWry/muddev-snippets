#!/bin/bash

# A useful script for backing up your postgres database to git

# Variables
DB_NAME="your db name"
DB_USER="your db user"
OUTPUT_FILE="backup.sql"

# Dump the database
pg_dump -U $DB_USER -W -F p $DB_NAME > $OUTPUT_FILE

# Add the dump to Git
git add $OUTPUT_FILE
git commit -m "Database backup on $(date +'%Y-%m-%d')"
