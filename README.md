### A quick web scraping script that will get you the contact details of all technology companies in Malta

Malta has one of the most vibrant technology ecosystems in Europe

This web scraping script will get you a list of all the technology companies that operate in Malta

Specifically, you will get an excel with:
* Name
* Telephone
* Email
* Sector where they operate


This project has two frequent web scraping complexities:
 1. The site is protected by a CDN. So we pass the headers in the request to mimic the behavior of a regular browser
 2. The page uses dynamic rendering. So we need to wait for JavaScript to render each page before parsing and saving the data. We use the [requests-html](https://pypi.org/project/requests-html/) library to account for that and we set a 5 seconds waiting time after each request

This code is not optimized for production. But it will get to the job done in a few minutes.

To run the script:

Clone (or download and unzip) the repository

Enter the directory
```linux
cd web-scraping-malta-tech-mt
```

Create an environment
```linux
python3 -m venv venv
```

Activate the environment
```linux
source venv/bin/activate
```

Install dependencies
```python
pip install -r requirements.txt
```

Execute the script
```python
python scrape_tmt_malta.py
```


Hope you like it and find it useful!
