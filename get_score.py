import urllib,urllib2
import re
import BeautifulSoup


def isbn_2_score(isbn):
    url1 = 'http://www.douban.com/subject_search?search_text='
    try:
        response = urllib2.urlopen(url1+isbn)
    except Exception,e:
        return 0.0
    doc = response.read()
    soup = BeautifulSoup.BeautifulSoup(''.join(doc))
    try:
        book_info = soup.find("a",{"class":"nbg"})
    except Exception,e:
        return 0.0
    if isinstance(book_info,BeautifulSoup.Tag):
        url_book_info = book_info['href']
        try:
            response = urllib2.urlopen(url_book_info)
        except Exception,e:
            return 0.0
        book_page = response.read()
        soup = BeautifulSoup.BeautifulSoup(''.join(book_page))
        score_info = soup.find('strong','ll rating_num')
        if isinstance(book_info,BeautifulSoup.Tag):
            score = score_info.string
            return score
        return 0.0
    return 0.0

def read_file(file_name):
    file_handler = open(file_name,'r')
    return file_handler

def return_isbn(file_handler):
    isbn = file_handler.readline()
    return isbn


if __name__ == '__main__':
data = read_file('data.csv')
	f = open('dump','w')
	k = return_isbn(data)
	while k is not None:
    	score = isbn_2_score(k)
    	result = k[0:-1]+":"+str(score)+"\n"
    	print result
    	f.write(result)
    	k=return_isbn(data)
	f.close()
