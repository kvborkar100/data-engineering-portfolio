from xml.dom import minidom
import os
import pandas as pd


def createXML(invoiceData, fileNumber):

    root = minidom.Document()

    xml = root.createElement('invoice')
    root.appendChild(xml)

    #creating invoice header tags
    headerElement = root.createElement('header')
    invoiceNumber = root.createElement('invoiceNumber')
    invoiceNumber.setAttribute('value', invoiceData[0])
    headerElement.appendChild(invoiceNumber)

    invoiceDate = root.createElement('invoiceDate')
    invoiceDate.setAttribute('value', invoiceData[1])
    headerElement.appendChild(invoiceDate)

    paymentTerms = root.createElement('paymentTerms')
    paymentTerms.setAttribute('value', str(invoiceData[2]))
    headerElement.appendChild(paymentTerms)

    invoiceCurrency = root.createElement('invoiceCurrency')
    invoiceCurrency.setAttribute('value', invoiceData[3])
    headerElement.appendChild(invoiceCurrency)

    companyName = root.createElement('companyName')
    companyName.setAttribute('value', invoiceData[4])
    headerElement.appendChild(companyName)

    xml.appendChild(headerElement)

    #creating invoice lines tags
    lineElement = root.createElement('lines')
    lineNumber = root.createElement('lineNumber')
    lineNumber.setAttribute('value', str(invoiceData[5]))
    lineElement.appendChild(lineNumber)

    itemName = root.createElement('itemName')
    itemName.setAttribute('value', invoiceData[6])
    lineElement.appendChild(itemName)

    totalQuantity = root.createElement('totalQuantity')
    totalQuantity.setAttribute('value', str(invoiceData[7]))
    lineElement.appendChild(totalQuantity)

    itemAmount = root.createElement('itemAmount')
    itemAmount.setAttribute('value', str(invoiceData[8]))
    lineElement.appendChild(itemAmount)

    lineAmount = root.createElement('lineAmount')
    lineAmount.setAttribute('value', str(invoiceData[9]))
    lineElement.appendChild(lineAmount)

    xml.appendChild(lineElement)

    #creating invoice footer tags
    footerElement = root.createElement('footer')
    vat = root.createElement('vat')
    vat.setAttribute('value', str(invoiceData[10]))
    footerElement.appendChild(vat)

    invoiceAmount = root.createElement('invoiceAmount')
    invoiceAmount.setAttribute('value', str(invoiceData[11]))
    footerElement.appendChild(invoiceAmount)

    xml.appendChild(footerElement)

    xml_str = root.toprettyxml(indent="\t")

    fileName = f"INV{fileNumber}.xml"

    save_path_file = '/home/krushna/Documents/Krushna/Projects/InvoiceManagement/XMLFiles/' + fileName

    with open(save_path_file, "w") as f:
        f.write(xml_str)
    print(f"Invoice - {fileName} created...")


if __name__ == "__main__":
    df = pd.read_csv('MOCK_DATA.csv', index_col=False)
    # print(df.head(5))
    fileNumber = 0

    for index, rows in df.iterrows():
        invoiceList = [rows["Invoice Number"], rows["Invoice Date"], rows["Payment Terms"], rows["Invoice Currency"], rows["Company Name"],
                       rows["Line Number"], rows["Item Name"], rows["Quantity"], rows["Amount"], rows["Total Amount"], rows["VAT"], rows["Invoice Amount"]]
        fileNumber += 1

        createXML(invoiceList, fileNumber)
