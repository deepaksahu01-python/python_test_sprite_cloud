from fpdf import FPDF

# Define translated and original content as (English, Dutch) pairs
content_pairs = [
    ("1.1 Introduction", "1.1 Intro"),
    ("a Who are you? Introduce yourself briefly. Which adjective suits you?",
     "a Wie ben je? Introduceer jezelf kort. Welk adjectief past bij jou?"),
    ("b How would you like your fellow students and your teacher to address you?",
     "b Hoe wil je dat je medecursisten en je docent je noemen?"),
    ("c Which personal pronouns suit you?", "c Welke persoonlijke voornaamwoorden passen bij jou?"),
    ("- he, him, his", "- hij, hem, zijn"),
    ("- she, her, her", "- zij, haar, haar"),
    ("- they, them, their", "- hen, hen, hun"),
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

class AddInPdf:
    def __init__(self):
    # Initialize PDF
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_font("Arial", size=12)

    def add_content(self, en, nl, pdf):
        # Add content to PDF
        self.pdf.set_font("Arial", style='B', size=12)
        self.pdf.multi_cell(0, 10, en)
        self.pdf.set_font("Arial", style='', size=12)
        self.pdf.multi_cell(0, 10, nl)
        self.pdf.ln(2)
        return self.pdf
    
    def save_pdf(self, pdf, file_name):
        # Save the PDF
        pdf.output(file_name)
