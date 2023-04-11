import json
from fpdf import FPDF
from pathlib import Path

from helpers import create_table, produce_txt

chapter_title = {
    "harvester": "TheHarvester Results",
    "emailharvester": "EmailHarvester Results",
    "amass": "Amass Results"
}

class PDF(FPDF):
    def header(self):
        self.image("./images/logo.png", 5, 8, 40)
        self.set_font('Times', 'B', 15)
        w = self.get_string_width(self.title) + 6
        self.set_x((210 - w) / 2)
        self.set_line_width(1)
        self.cell(w, 25, self.title, 'C', 1)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Times', 'B', 12)
        self.set_fill_color(17, 132, 120)
        self.cell(0, 6, '%d. %s' % (num, label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name, title, data):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)
        if chapter_title['harvester'] == title:
            create_table(self, title, data['TheHarvester'])
        elif chapter_title['amass'] == title:
            create_table(self, title, data['Amass'])

    def print_chapter(self, num, title, name, data):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name, title, data)  

def pdf_creator(title, path, password = ""):
    json_path = Path(path).joinpath(f'{title}.json')
    json_file = json_path.open()
    
    data = json.load(json_file)
    
    produce_txt(data)
    
    pdf = PDF()
    pdf.set_title(f'InfoCrawler report: {title}')
    pdf.set_author('InfoCrawler')
    
    i = 1
    for key, value in chapter_title.items():
        pdf.print_chapter(i, value, f'./temp/{key}.txt', data)
        i += 1
    
    if password != "":
        pdf.set_encryption(
            owner_password=password,
            user_password=password
        ) 
    
    pdf.output(f'{path}/{title}.pdf', 'F')
    