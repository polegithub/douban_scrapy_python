#coding=utf-8
import urllib
import re


#备注： 这个暂时都导入，后续根据需求再更改

from crawler.getBasicData.getBasicDataFromDouban import SearchData
from crawler.getBasicData.getTianYaData import SearchData
from crawler.getBasicData.getZhihuData import SearchData
from analyse.dbHandle import do_init_db

from crawler.getBasicData.getbooklistfromDB import startSearchBoook
from crawler.getBasicData.getMovielistFromDB import startSearchMovie

print('Let us begin')

if __name__=='__main__' :
    print('enter main')

    # 调试的时候根据需求更改：
    # 调试爬虫 MainValue =1，
    # 数据库  MainValue =2，
    # 其他待定义

    MainValue = 1

    if MainValue == 1:
        # f = SearchData()
        # f.search()
        startSearchMovie()
    elif MainValue == 2:
        # do_init_db()
        pass
    else:
        pass




