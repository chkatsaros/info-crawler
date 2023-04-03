from fpdf import FPDF

title = 'InfoCrawler Report - {Domain Name}'

class PDF(FPDF):
    def header(self):
        self.image("./images/logo.png", 5, 8, 40)
        self.set_font('Times', 'B', 15)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_line_width(1)
        self.cell(w, 25, title, 'C', 1)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Times', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, '%d. %s' % (num, label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

pdf = PDF()
pdf.set_title(title)
pdf.set_author('InfoCrawler')
pdf.print_chapter(1, 'TheHarvester Results', 'test.txt')
pdf.print_chapter(2, 'EmailHarvester Results', 'test.txt')
pdf.print_chapter(3, 'Amass Results', 'test.txt')
pdf.output('test.pdf', 'F')