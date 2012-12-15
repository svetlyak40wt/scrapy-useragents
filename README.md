scrapy-useragents
=================

This is a middleware for Scrapy framework. It allows to set random
User-Agent for each request.

Configuration
-------------

Create a text file with one user agent per line.

This way you can grep user agents from Nginx logs:

    egrep -h -o '"[^"]+" "[^"]+"$' * | cut -d '"' -f 2 | sort -u > user-agents.txt

Call this file `user-agents.txt` or use another name and write it's path
in the `USER_AGENTS_LIST_FILE` setting.

Then add it into the middleware list, and remove default middleware:

    DOWNLOADER_MIDDLEWARES = {
        # we'll turn off standart user agent middleware
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_useragents.middleware.UserAgentsMiddleware': 400,
    }

Contribution
------------

Author of this project is Alexander Artemenko. You are welcomed to
send patches and pull requests to the [GitHub](https://github.com/svetlyak40wt/scrapy-useragents).
