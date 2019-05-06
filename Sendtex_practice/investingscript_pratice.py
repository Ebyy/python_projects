# project aims to pull the price to book statistic of companies
# sort through to the data and select above a certain value and
# plot or try to make a financial benefitting graph


import time
import urllib.request
import pandas as pd


sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp', 'cgm']

def yahooKeyStats(stock):
    try:
        sourceCode = urllib.request.urlopen('http://ca.finance.yahoo.com/d/quotes.csv?s=' + stock + '&f=p6').read()
        #urllib.request.urlretrieve(sourceCode, 'quote.csv')

        #reported_pb = pd.read_csv('quote.csv', header=None)
        pbr = sourceCode.partition('Price/Book</span><!-- react-text: 58 --> <!-- /react-text -->'
                                '<!-- react-text: 59 -->(mrq)<!-- /react-text -->'
                                '<sup aria-label="KS_HELP_SUP_undefined" data-reactid="60"></sup></td>'
                                '<td class="Fz(s) Fw(500) Ta(end)" data-reactid="61">')[1].partion('</td>')[0].read()
        pbr=pbr[2][4]
        print('price to book ratio', pbr)
    except Exception as e:
        print('failed in the main loop', str(e))

yahooKeyStats('aapl')
