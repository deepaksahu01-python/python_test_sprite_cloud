from ebooklib import epub
import random
class AddInEpub:
# Define translated and original content as (English, Dutch) pairs
    content_pairs = [
        ("1.1 Introduction", "1.1 Intro"),
        ("a Who are you? Introduce yourself briefly. Which adjective suits you?",
        "a Wie ben je? Introduceer jezelf kort. Welk adjectief past bij jou?"),
        ("b How would you like your fellow students and your teacher to address you?",
        "b Hoe wil je dat je medecursisten en je docent je noemen?"),
        ("c Which personal pronouns suit you?", "c Welke persoonlijke voornaamwoorden passen bij jou?"),
        ("• he, him, his", "• hij, hem, zijn"),
        ("• she, her, her", "• zij, haar, haar"),
        ("• they, them, their", "• hen, hen, hun"),
        ("1.2 Dialogue and vocabulary", "1.2 Dialoog en vocabulaire"),
        ("The following dialogues contain these international words. Do you know them?",
        "In de dialogen hierna staan deze internationale woorden. Ken je ze?"),
        ("creative | the guitar | the piano | the orchestra | published (to publish) | academic | "
        "medical | the telephone",
        "creatief | de gitaar | de piano | het orkest | gepubliceerd (publiceren) | universitair | "
        "medisch | de telefoon"),
        ("Jip de Jong and John Mulenga talk about themselves.",
        "Jip de Jong en John Mulenga vertellen over zichzelf."),
        ("Dialogue 1 | Interview with Jip de Jong", "Dialoog 1 | Interview met Jip de Jong"),
        ("Name: Jip de Jong", "Naam: Jip de Jong"),
        ("Age: 23", "Leeftijd: 23"),
        ("Study: fourth-year law student in Rotterdam", "Studie: vierdejaarsstudent rechten in Rotterdam"),
        ("Where does your first name come from?", "Waar komt je voornaam vandaan?"),
        ("My name comes from a book, a children's book. Maybe you know it: Jip and Janneke. Jip is the boy and Janneke the girl. "
        "I'm a woman, but my name is Jip. Funny, right? My brother is named after our grandmother; her name was Anne. People find our names confusing, haha.",
        "Mijn naam komt uit een boek, een kinderboek. Misschien ken je het: Jip en Janneke. Jip is de jongen en Janneke het meisje. "
        "Ik ben een vrouw, maar ik heet Jip. Grappig hè? Mijn broer is vernoemd naar oma, ze heette Anne. Mensen vinden onze namen verwarrend, ha ha.")
    ]
    def __init__(self, title):
        # Create EPUB self.book
        self.book = epub.EpubBook()
        self.book.set_identifier('id123456')
        self.book.set_title(title)
        self.book.set_language('en')

        self.book.add_author('local')

    def create_content(self, en, nl):
        # Create content
        html_content += f'<p><strong>{en}</strong><br>{nl}</p>'
        return html_content
    def add_chapter(self, html_content, book, ch_no):
        # Create a chapter
        title_name = 'Chapter_{}'.format(ch_no)
        filename = 'chap_0{}.xhtml'.format(ch_no)
        chap_name = 'chap_{}'.format(ch_no)

        chapter = epub.EpubHtml(title=title_name, file_name=filename, lang='en')
        chapter.content = html_content

        # Add chapter and navigation
        book.add_item(chapter)
        book.toc = (epub.Link(filename, title_name, chap_name),)
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        # Define default CSS
        style = 'BODY { font-family: Arial, sans-serif; line-height: 1.6; }'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        # Set spine
        book.spine = ['nav', chapter]
        return book
    def write_to_file(self, book, file_name):

        # Write to file
        epub.write_epub(file_name, book)
