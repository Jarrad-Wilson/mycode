#!/usr/bin/env python3
import csv

# Asks for search criteria from user
search = input("Choose a # from 1 - 149532:\n")

# Opens csv data file
file = csv.reader(open("movies.csv"))

# Go over each row and print it if it contains user input.
for row in file:
    if search in row:
        print(row)
