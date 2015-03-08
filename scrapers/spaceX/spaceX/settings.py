# -*- coding: utf-8 -*-

# Scrapy settings for spaceX project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spaceX'

SPIDER_MODULES = ['spaceX.spiders']
NEWSPIDER_MODULE = 'spaceX.spiders'
USER_AGENT = 'spacexjobs (+http://www.spacejobs.us)'

ITEM_PIPELINES = {
	'spaceX.pipelines.SpacexPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spaceX (+http://www.yourdomain.com)'
