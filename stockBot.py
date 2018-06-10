import web
import bs4
import requests


def searchStock(stock):
    print('\nTICKER IS: ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper() + ' ' + stock.upper())
    try:
        result = thestock(stock)
    except Exception as e:
        print str(e) #ask TA whether we print or return None
        return None
    else:
        return result


def thestock(stock):
    url = 'https://investorplace.com/stock-quotes/' + stock.lower() + '-stock-quote/'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("div", {"id":"stock_analysis_ctrl_box"})


    for item in search:
        step1=item.find_all("h4", {"class": "grade"})
        l= step1[1].text
        
    url1 = 'https://www.zacks.com/stock/quote/' + stock.upper() + '?q=' + stock.lower();
    html = requests.get(url1) 
    page = bs4.BeautifulSoup(html.text, 'html.parser')
    rating = page.find_all(class_="rank_view")
    rating = str(rating)
    rating = rating.split()
    m = rating[2]

    price = page.find_all(class_="last_price")

    for xx in price:
        xxx = xx.text

    print stock.upper()+ " is currently priced at " + xxx
    print ""

    if str(l[-1]) == 'A' and str(m[0]) == str(5):
        rec = "HOLD"
    if str(l[-1]) == 'A' and str(m[0]) == str(4):
        rec = "BUY"
    if str(l[-1]) == 'A' and str(m[0]) == str(3):
        rec = "BUY"
    if str(l[-1]) == 'A' and str(m[0]) == str(2):
        rec = "STRONG BUY"
    if str(l[-1]) == 'A' and str(m[0]) == str(1):
        rec = "STRONG BUY"
    if str(l[-1]) == 'B' and str(m[0]) == str(5):
        rec = "HOLD"
    if str(l[-1]) == 'B' and str(m[0]) == str(4):
        rec = "STRONG BUY"
    if str(l[-1]) == 'B' and str(m[0]) == str(3):
        rec = "BUY"
    if str(l[-1]) == 'B' and str(m[0]) == str(2):
        rec = "STRONG BUY"
    if str(l[-1]) == 'B' and str(m[0]) == str(1):
        rec = "STRONG BUY"
    if str(l[-1]) == 'C' and str(m[0]) == str(5):
        rec = "BUY"
    if str(l[-1]) == 'C' and str(m[0]) == str(4):
        rec = "BUY"
    if str(l[-1]) == 'C' and str(m[0]) == str(3):
        rec = "HOLD"
    if str(l[-1]) == 'C' and str(m[0]) == str(2):
        rec = "HOLD"
    if str(l[-1]) == 'C' and str(m[0]) == str(1):
        rec = "HOLD"
    if str(l[-1]) == 'D' and str(m[0]) == str(5):
        rec = "HOLD"
    if str(l[-1]) == 'D' and str(m[0]) == str(4):
        rec = "HOLD"
    if str(l[-1]) == 'D' and str(m[0]) == str(3):
        rec = "SELL"
    if str(l[-1]) == 'D' and str(m[0]) == str(2):
        rec = "SELL"
    if str(l[-1]) == 'D' and str(m[0]) == str(1):
        rec = "SELL"
    if str(l[-1]) == 'F' and str(m[0]) == str(5):
        rec = "STRONG SELL"
    if str(l[-1]) == 'F' and str(m[0]) == str(4):
        rec = "STRONG SELL"
    if str(l[-1]) == 'F' and str(m[0]) == str(3):
        rec = "STRONG SELL"
    if str(l[-1]) == 'F' and str(m[0]) == str(2):
        rec = "STRONG SELL"
    if str(l[-1]) == 'F' and str(m[0]) == str(1):
        rec = "STRONG SELL"


    result = 'Your Ticker: ' + stock.upper() + ' - Current Price: ' + xxx + ' - Financial Grade: ' + l[-1] + ' - Secure Rating:  '+ m[0] + ' out of 5 (1 is the best) || Overall Recommendation: ' + rec
    return result



