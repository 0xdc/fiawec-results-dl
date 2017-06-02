fiawec - download timing data for official fia wec events
====

The FIA WEC's timekeepers place timing data from official events onto a publically available webserver
However, the contents do not have an easily accessible API and download option. This module
scrapes the HTML forms via BeautifulSoup and downloads the provided files.

Quickstart
----
> $ pip install -r requirements.txt
> $ python -mfiawec