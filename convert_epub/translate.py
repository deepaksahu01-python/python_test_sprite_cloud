import re
from deep_translator import GoogleTranslator
from utils import Utils
from pdf import AddInPdf
from addinepub import AddInEpub

class Translate:

    def __init__(self):
        self.util = Utils()
        
if __name__ == "__main__":
    # Split the Dutch text by lines
    util = Utils()
    add_pdf = AddInPdf()
    start_page_number = 51
    till_page_number = 52
    title = '{} to {}'.format(start_page_number, till_page_number)
    add_epub = AddInEpub(title)
    file_content = util.read_pdf('/home/deepak/workspace/convert_epub/samplebook.pdf', start_page_number, till_page_number)
    ch_no = 0
            
    html_content = ''
    for page in file_content:
        ch_no = ch_no + 1
        page = page.replace("-\n","")
        page = page.replace("\n"," ")
        # lines = page.strip().split('.')
        parts = re.split(r'([?.])', page)
        # Combine text with their delimiter
        lines = [parts[i] + parts[i+1] for i in range(0, len(parts)-1, 2)]
        # Translate line by line
        translated_pairs = []
        for line in lines:
            if line.strip():
                english = GoogleTranslator(source='nl', target='en').translate(line)
                translated_pairs.append((english, line.strip()))
            else:
                translated_pairs.append(("", ""))  # Preserve blank lines

        # Output the translation
        for en, nl in translated_pairs:
            en = en.replace("•","-")
            nl = nl.replace("•","-")
            # print(f"{en}\n{nl}\n")
            # add_pdf.add_content(en, nl, add_pdf.pdf)
            html_content += f'<p><strong>{en}</strong><br>{nl}</p>'
    # add_pdf.save_pdf(add_pdf.pdf, 'convert_epub/{}.pdf'.format(title))
    add_epub.add_chapter(html_content, add_epub.book, ch_no)
    add_epub.write_to_file(add_epub.book, 'convert_epub/{}.epub'.format(title))

