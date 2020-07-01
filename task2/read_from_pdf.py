import PyPDF2 

def pdf_reader():
	file = open('example.pdf','rb')
	pdfReader = PyPDF2.PdfFileReader(file) 
	  
	pages = pdfReader.numPages
	print('Page count is:',pages)

	#loop for multiple page pdf
	for i in range(pdfReader.getNumPages()):
		pageObj = pdfReader.getPage(i)

		print("Page №", pdfReader.getPageNumber(pageObj) + 1)
		print(pageObj.extractText()) #type str

pdf_reader()