#!/usr/bin/env python3

import csv
f = open('movies.csv')
title = []
genres = []


movies = list(csv.reader(f))

print(movies[:10])
