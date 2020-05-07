from zeep import Client
from lxml import etree
import datetime

data = Client('https://www.pttor.com/OilPrice.asmx?WSDL')

class OilPrice:
    def __init__(self, date, oilName):
        self.date = date
        self.oilName = oilName

    def getOilPrice(date, oilName):
        dx= date.split("/")
        result = data.service.GetOilPrice("en",dx[2],dx[1],dx[0])
        #print(result)      #get XML
        root = etree.XML(result)
        for r in root:
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]
            if (product == oilName):
                result = float(price[0])
        return result

    def getCurrentPrice():
        d = datetime.datetime.today()
        date = str(d)
        dx=date[0:10].split("-")
        result = data.service.GetOilPrice("en",dx[2],dx[1],dx[0])
        case = list()
        for r in etree.XML(result):
            product = r.xpath('PRODUCT/text()')
            price = r.xpath('PRICE/text()')
            l = [product, price]
            case.append(l)
        return case

price = OilPrice.getOilPrice("2020/05/01","Gasohol E20")
print("Price =",price)


print(*OilPrice.getCurrentPrice(),sep="\n")

