# install tk
# install ghostscript
# install camelot-py
import camelot

tables = camelot.read_pdf("table_pdf.pdf", pages="1")
print(tables)

tables.export("pdf_table.pdf", f="csv", compress=True)
tables[0].to_csv("pdf_table.csv")
