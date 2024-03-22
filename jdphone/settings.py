# -*- coding: utf-8 -*-
BOT_NAME = 'jdphone'

SPIDER_MODULES = ['jdphone.spiders']
NEWSPIDER_MODULE = 'jdphone.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36",
  "Upgrade-Insecure-Requests": "1",
  "DNT": "1"
}

DOWNLOADER_MIDDLEWARES = {
   'jdphone.middlewares.SeleniumMiddlewares': 543,
}

ITEM_PIPELINES = {
    'jdphone.pipelines.JdphonePipeline': 300,
}
