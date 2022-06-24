import camelot

tables = camelot.read_pdf("table_pdf.pdf", pages="1")
print(tables)