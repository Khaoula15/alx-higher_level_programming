#!/bin/bash
# Get the byte size of the HTTP response header for a given URL using curl
curl -s "$1" | wc -c
