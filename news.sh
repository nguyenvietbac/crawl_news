#!/bin/bash

rm dantri.json
rm vne.json
rm mof.json
rm mpi.json
rm sbv.json
rm vib.json
rm moit.json
rm vcb.json

/home/crawler/.local/bin/scrapy crawl dantri -o dantri.json
/home/crawler/.local/bin/scrapy crawl vne -o vne.json
/home/crawler/.local/bin/scrapy crawl mof -o mof.json
/home/crawler/.local/bin/scrapy crawl mpi -o mpi.json
/home/crawler/.local/bin/scrapy crawl sbv -o sbv.json
/home/crawler/.local/bin/scrapy crawl vib -o vib.json
/home/crawler/.local/bin/scrapy crawl moit -o moit.json
/home/crawler/.local/bin/scrapy crawl vcb -o vcb.json

sleep 30
/usr/bin/python3 send_email_test.py
/usr/bin/python3 combine_file.py