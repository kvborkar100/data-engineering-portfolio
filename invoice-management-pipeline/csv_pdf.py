from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('logo.jpg', 10, 8,33)
        # Arial bold 15
        self.set_font('Arial', 'B', 35)
        # Move to the right
        self.cell(60)
        # Title
        self.cell(60, 20, 'INVOICE', 1, 0, 'C')
        # Line break
        self.ln(40)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def company(self):
        self.set_font('Arial', 'B', 12)
        self.cell(5)
        self.cell(60, 10, 'Apple Corporation US', 1, 0, 'C')
        self.ln(15)

    def headerDetails(self):
        self.set_font('Arial', 'B', 8)
        self.cell(130)
        self.cell(60, 5, 'Invoice Number - ', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, 'Invoice Date - ', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, 'Payment Terms - ', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, 'Invoice Currency - ', 1, 0, 'L')
        self.ln(20)

    def lineTable(self):
        self.set_font('Arial', 'B', 8)
        self.cell(15, 5, 'Line #', 1, 0, 'C')
        self.cell(90, 5, 'Item Name', 1, 0, 'C')
        self.cell(20, 5, 'Quantity', 1, 0, 'C')
        self.cell(20, 5, 'Amount', 1, 0, 'C')
        self.cell(35, 5, 'Line Amount', 1, 0, 'C')
        self.ln()

    def lineDetails(self):
        self.set_font('Arial', '', 8)
        self.cell(15, 5, '1', 1, 0, 'C')
        self.cell(90, 5, 'New Avanger Game', 1, 0, 'C')
        self.cell(20, 5, '1', 1, 0, 'C')
        self.cell(20, 5, '120', 1, 0, 'C')
        self.cell(35, 5, '120', 1, 0, 'C')
        self.ln(20)

    def footerDetails(self):
        self.set_font('Arial', 'B', 10)
        self.cell(110)
        self.cell(40, 5, 'VAT : ', 1, 0, 'L')
        self.cell(20, 5, '20%', 1, 0, 'R')
        self.ln()
        self.cell(110)
        self.cell(40, 5, 'Invoice Amount : ', 1, 0, 'L')
        self.cell(20, 5, '12345', 1, 0, 'R')


# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.company()
pdf.headerDetails()
pdf.lineTable()
pdf.lineDetails()
pdf.footerDetails()
pdf.set_font('Times', '', 12)
# pdf.cell(1,1,'Hello')
# for i in range(1, 41):
#     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output('tuto2.pdf', 'F')
