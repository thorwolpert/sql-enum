#! /bin/bash
cat << EOF | psql postgresql://postgres:password@localhost:5432

create database sql_enum;
EOF
