import fitz  # PyMuPDF

class Utils:

    def __init__(self):
        print('hi')

    def read_pdf(self, file_name, start_page, till_page):
        file_text = list()
        with fitz.open(file_name) as doc:
            # for page in doc:
            #     page_text = page.get_text()
            #     file_text.append(page_text)
            for page_number in range(start_page - 1, till_page):
                page = doc.load_page(page_number)
                page_text = page.get_text()

                file_text.append(page_text)
                # print(page_text)
        return file_text


