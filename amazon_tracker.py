import PyPDF2
import requests
import fpdf
from bs4 import BeautifulSoup

from email_alert import alert_system
from threading import Timer


class tracker():
    def __init__(self, message):
        print(message)
        self.message = message

    set_price = 5000
    URL = "https://www.amazon.in/JBL-130NC-Active-Cancellation-Earbuds/dp/B09HGW9V7D/ref=sr_1_1_sspa?adgrpid=60416827593&ext_vrnc=hi&gclid=Cj0KCQiA_bieBhDSARIsADU4zLcLoOnUnyrZ-h0gN6cVoDELuc42wb4ZMFhvLVO0OTw4zuYf1IqLW6caAhyxEALw_wcB&hvadid=398059378063&hvdev=c&hvlocphy=9061989&hvnetw=g&hvqmt=b&hvrand=684592312855445884&hvtargid=kwd-335545237638&hydadcr=24542_1971411&keywords=apple%2Bair%2Bpods%2Bprice&qid=1674508015&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'close'
    }


    def check_price(self,URL):
     try:
        URL=tracker.URL;
        set_price=tracker.set_price
        page = requests.get(tracker.URL, headers=tracker.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id='productTitle').get_text()
        product_title = str(title)
        product_title = product_title.strip()
        pdf.cell(200,10,txt = product_title, ln=1)
        print(soup.find(id='a-price-whole'))

        price = soup.find(class_='a-price-whole').get_text()
        pdf.cell(200, 10, txt="The current price of the product is "+price, ln=1)
        # print(price)
        product_price = ''
        for letters in price:
            if letters.isnumeric() or letters == '.':
                product_price += letters
                print(float(product_price))
            if float(product_price) <= set_price:

                alert_system(product_title, URL)
                print('sent')
                pdf.cell(200, 10, txt="The mail is sent", ln=1)
                return
            else:
                print('not sent')
                pdf.cell(200, 10, txt="The mail is not sent", ln=1)

     except Exception as e:
        print('The error is ' + str(e))


input_file = open("output.pdf",'rb')
input_pdf = PyPDF2.PdfReader(input_file)
watermark_file = open("watermark.pdf",'rb')
watermark_pdf = PyPDF2.PdfReader(watermark_file)

pdf_page = input_pdf.pages[0]
watermark_page = watermark_pdf.pages[0]
pdf_page.merge_page(watermark_page)

out = PyPDF2.PdfWriter()
out.add_page(pdf_page)

merged_file = open("final_output.pdf",'wb')
out.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()


