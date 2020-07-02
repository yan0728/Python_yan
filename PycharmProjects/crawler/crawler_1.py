from bs4 import BeautifulSoup

with open('E:/python/Plan-for-combating-master/week1/1_2/1_2code_of_video/web/new_index.html','r')as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    print(Soup)