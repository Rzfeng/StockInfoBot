import bs4
import requests


inf = 0;
stocks = []
numStocks = 0

def checkStock(stock):
	print('\nTICKER IS: ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper())
	try:	
		zacks(stock)
		marketbeat(stock)
		wsj(stock)
		
	except:
		print('failed')
	year(stock)
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

def wsj(ticker):
	curl = 'http://quotes.wsj.com/' + ticker.upper() + '/research-ratings'
	html = requests.get(curl) 
	#BeautifulSoup Object that gets the html of the webpage
	page = bs4.BeautifulSoup(html.text, 'html.parser')
	#print(page.prettify())
	rating = page.find(class_="cr_analystRatings cr_data module").get_text()
	#Getting product style
	rating = rating.split("Consensus")
	a,b,c = rating[1].split()
	target = page.find(class_="cr_data rr_stockprice module").get_text()
	target = target.split("Average")
	target = str(target[1])
	#listOfWords = listOfWords.split()
	#print(listOfWords)
	print('Wall Street Journal info for: ' + ticker.upper() + ' '+ ticker.upper() + ' '+ ticker.upper() + ' '+ ticker.upper())
	print('\n' + 'Ratings: ' + c)
	print('Average: ' + target)
	print('---------------------')


def marketbeat(ticker):
	curl = 'https://www.marketbeat.com/stocks/NASDAQ/' + ticker
	html = requests.get(curl) 
	#BeautifulSoup Object that gets the html of the webpage
	page = bs4.BeautifulSoup(html.text, 'html.parser')
	rating = page.find(id="AnalystRatings").get_text()
	listOfWords = rating.partition("Analysts' Ratings History")
	listOfWords = str(listOfWords[0])
	word = ''
	index = listOfWords.index("Consensus Rating:")
	print('MarketBeat Ratings')
	print('Consensus Rating: ' + listOfWords[index+17] + listOfWords[index+18] + listOfWords[index+19] + listOfWords[index+20] + listOfWords[23])
	index = listOfWords.index("Consensus Price Target:")
	for num in range(0, 30):
		word = word + listOfWords[index+num]
	print(word)
	print('---------------------')


def year(ticker):
	curl = 'https://www.barchart.com/stocks/quotes/' + ticker.lower()
	html = requests.get(curl) 
	#BeautifulSoup Object that gets the html of the webpage
	page = bs4.BeautifulSoup(html.text, 'html.parser')
	#page = page.text
	rating = page.find_all(class_='cell-period-change')
	rating = str(rating)
	#a = page.find(class_='cell-period-change').get_text()
	#b = page.find(class_='odd').get_text()
	#c = page.find(class_='price raising ').get_text()
	try:
		index = rating.index("since 04/28/17</span>")
		index = index + 90
	#print(index)
	#print(rating)
		word = ''
		for num in range(0, 45):
			word = word + rating[index+num]
		print('Past Year Performance: ' + word)
	except:
		print('4/28 didnt work')

	try:
		index = rating.index("since 05/01/17</span>")
		index = index + 90
	#print(index)
	#print(rating)
		word = ''
		for num in range(0, 45):
			word = word + rating[index+num]
		print('Past Year Performance: ' + word)
	except:
		print('4/28 didnt work')
	#print(page.prettify())
	#rating = page.find(class_="rank_view").get_text()
	#rating = rating.split()
	#print('\n' + 'Zacks Rating: ' + rating[0] + rating[1])
	print('---------------------')

while(inf == 0):
	numStocks = numStocks + 1
	ticker = raw_input('\nPlease enter the ticker (' + str(numStocks) + '): ')
	if (ticker == 'DONE'):
		num = 0
		for x in stocks:
			print('----------------------------------------------------')
			checkStock(stocks[num])
			num = num + 1

	else:
		stocks.append(ticker)