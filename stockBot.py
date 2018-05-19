import web
import bs4
import requests

inf = 0;
stocks = []
numStocks = 0

#______________________________________________________________________________
#OUR CODE IS HERE
def searchStock(stock):
    print('\nTICKER IS: ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper())
    try:
        result = zacks(stock)
    except Exception as e:
        print str(e) #ask TA whether we print or return None
        return None
    else:
        return result

	#print('The rating is' + str(listOfWords[201]))

def zacks(ticker):
    curl = 'https://www.zacks.com/stock/quote/' + ticker.upper() + '?q=' + ticker.lower();
    html = requests.get(curl)
	#BeautifulSoup Object that gets the html of the webpage
    page = bs4.BeautifulSoup(html.text, 'html.parser')
    rating = page.find_all(class_="rank_view")
	#style = str(page.find_all(class_='float_right'))
    rating = str(rating)
    rating = rating.split()

	#style = style.split()
	#print(rating)
    print('\nZacks Rating: ' + rating[2])
	#print('\nStyle Rating: ' + style)
	#for num in range (0,10)
    print('---------------------')

    result = '\nZacks Rating: ' + rating[2] + ' <br /> for the ticker ' + ticker.upper()
    return result
