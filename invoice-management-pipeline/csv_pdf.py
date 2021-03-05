from fpdf import FPDF
import pandas as pd


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

    def company(self, companyName):
        self.set_font('Arial', 'B', 12)
        self.cell(5)
        self.cell(60, 10, companyName, 1, 0, 'C')
        self.ln(15)

    def headerDetails(self, invoiceNumber, invoiceDate, paymentTerms, invoiceCurrency):
        self.set_font('Arial', 'B', 8)
        self.cell(130)
        self.cell(60, 5, f'Invoice Number - {invoiceNumber}', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, f'Invoice Date - {invoiceDate}', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, f'Payment Terms - {paymentTerms}', 1, 0, 'L')
        self.ln()
        self.cell(130)
        self.cell(60, 5, f'Invoice Currency - {invoiceCurrency}', 1, 0, 'L')
        self.ln(20)

    def lineTable(self):
        self.set_font('Arial', 'B', 8)
        self.cell(15, 5, 'Line #', 1, 0, 'C')
        self.cell(90, 5, 'Item Name', 1, 0, 'C')
        self.cell(20, 5, 'Quantity', 1, 0, 'C')
        self.cell(20, 5, 'Amount', 1, 0, 'C')
        self.cell(35, 5, 'Line Amount', 1, 0, 'C')
        self.ln()

    def lineDetails(self, lineNumber, item, quantity, amount, lineAmount):
        self.set_font('Arial', '', 8)
        self.cell(15, 5, lineNumber, 1, 0, 'C')
        self.cell(90, 5, item, 1, 0, 'C')
        self.cell(20, 5, quantity, 1, 0, 'C')
        self.cell(20, 5, amount, 1, 0, 'C')
        self.cell(35, 5, lineAmount, 1, 0, 'C')
        self.ln(20)

    def footerDetails(self, vat, invoiceAmount):
        self.set_font('Arial', 'B', 10)
        self.cell(110)
        self.cell(40, 5, 'VAT : ', 1, 0, 'L')
        self.cell(20, 5, f'{vat}%', 1, 0, 'R')
        self.ln()
        self.cell(110)
        self.cell(40, 5, 'Invoice Amount : ', 1, 0, 'L')
        self.cell(20, 5, invoiceAmount, 1, 0, 'R')


if __name__ == "__main__":
    df = pd.read_csv('MOCK_DATA.csv', index_col=False)
    # print(df.head(5))
    fileNumber = 0

    for index, rows in df.iterrows():
        invoiceList = [rows["Invoice Number"], rows["Invoice Date"], rows["Payment Terms"], rows["Invoice Currency"], rows["Company Name"],
                       rows["Line Number"], rows["Item Name"], rows["Quantity"], rows["Amount"], rows["Total Amount"], rows["VAT"], rows["Invoice Amount"]]
        fileNumber += 1
        # Instantiation of inherited class
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.company(invoiceList[4])
        pdf.headerDetails(
            invoiceList[0], invoiceList[1], str(invoiceList[2]), invoiceList[3])
        pdf.lineTable()
        pdf.lineDetails(str(invoiceList[5]), invoiceList[6],
                        str(invoiceList[7]), str(invoiceList[8]), str(invoiceList[9]))
        pdf.footerDetails(str(invoiceList[10]), str(invoiceList[11]))
        fileName = f"/home/krushna/Documents/Krushna/Projects/InvoiceManagement/PDFFiles/INV{fileNumber}.pdf"
        pdf.output(fileName, 'F')
        print(f"PDF {fileNumber} created..")
