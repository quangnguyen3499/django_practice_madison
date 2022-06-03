
import pytesseract
import cv2 
import re
import fitz
import requests
from io import BytesIO
from datetime import datetime

def pymupdf_2(*, pdf_file: str):
    response = requests.get(pdf_file)
    opened_file = fitz.open(stream=BytesIO(response.content))

    for page in opened_file:
        pix = page.getPixmap(alpha=False, matrix=fitz.Matrix(2, 2))
        pix.writeImage("pn.png")

    img = cv2.imread("pn.png")
    extracted_text = pytesseract.image_to_string(img)
    factored_text = [x for x in extracted_text.split('\n') if x not in ['', ' ']]
    date_pattern = "([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2})$"
    amount_pattern = "Amount Due"
    id_pattern = "Invoice #"
    result = {}
    for i in factored_text:
        date = re.findall(date_pattern, i)
        amount = i if amount_pattern in i else None
        id_invoice = i if id_pattern in i else None
        if date: 
            result['date'] = '/'.join(date[0])
            result['date'] = datetime.strptime(result['date'], "%d/%m/%Y").strftime("%Y-%m-%d")
        if amount: 
            result['amount'] = i[i.index("$"):]
            result['amount'] = result['amount'].replace(",", ".")
        if id_invoice:
            result['number'] = i.split()[-1]
    return result
