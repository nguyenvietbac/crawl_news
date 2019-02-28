#!/bin/bash

rm dantri.json
rm vne.json
rm mof.json
rm mpi.json
rm sbv.json
rm vib.json
rm moit.json
rm vcb.json
rm reuters.json
rm economist.json
rm imf.json
rm fed.json

/home/crawler/.local/bin/scrapy crawl dantri -o dantri.json
/home/crawler/.local/bin/scrapy crawl vne -o vne.json
/home/crawler/.local/bin/scrapy crawl mof -o mof.json
/home/crawler/.local/bin/scrapy crawl mpi -o mpi.json
/home/crawler/.local/bin/scrapy crawl sbv -o sbv.json
/home/crawler/.local/bin/scrapy crawl vib -o vib.json
/home/crawler/.local/bin/scrapy crawl moit -o moit.json
/home/crawler/.local/bin/scrapy crawl vcb -o vcb.json
/home/crawler/.local/bin/scrapy crawl reuters -o reuters.json
/home/crawler/.local/bin/scrapy crawl economist -o economist.json
/home/crawler/.local/bin/scrapy crawl imf -o imf.json
/home/crawler/.local/bin/scrapy crawl fed -o fed.json
sleep 30
# /usr/bin/python3 send2.py
/usr/bin/python3 send_email_test.py
/usr/bin/python3 combine_file.py