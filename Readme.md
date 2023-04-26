Code Explanation
The os library provides a way to interact with the operating system, and is used to access the user's "Documentos" (Documents) folder, where the PDF file will be saved.

The Tkinter library is used to create a file dialog that allows the user to select the text file to be converted.

The reportlab library is used to create a PDF file.

The convertir_archivo_a_pdf() function is the main function that performs the conversion of the text file to PDF. It consists of the following steps:

a. A file dialog is created using the Tkinter library, and the user selects a text file to be converted.

b. The os.path module is used to get the full path of the "Documentos" folder.

c. The os.path module is used to create the name of the PDF file from the selected text file. The .replace() method is used to replace the ".txt" file extension with ".pdf".

d. The os.path module is used to join the path to the "Documentos" folder and the name of the PDF file.

e. The selected text file is opened using a with statement, and its contents are read into the texto variable.

f. The canvas.Canvas class from the reportlab library is used to create a new PDF file at the location specified in step d.

g. The pdf.drawString() method is used to add the contents of the texto variable to the PDF file at position (100, 750) on the canvas.

h. The pdf.save() method is used to save the PDF file.

The main function convertir_archivo_a_pdf() is called at the end of the code to perform the conversion.

Open user interface
![convertidor](https://user-images.githubusercontent.com/86695688/234698403-c912394e-203d-4010-a307-e3c15ecaa291.png)



txt file, converted to pdf


![convert1](https://user-images.githubusercontent.com/86695688/234698578-9d6a71ff-67fb-45c4-b676-8c10f09512dd.png)

