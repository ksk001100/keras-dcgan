from icrawler.builtin import GoogleImageCrawler
import sys
import os

word = sys.argv[1]

crawler = GoogleImageCrawler(storage={"root_dir": "inputs/"+word})
crawler.crawl(keyword=word, max_num=1000)
