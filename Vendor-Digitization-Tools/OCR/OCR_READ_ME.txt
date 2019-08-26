READ ME

This document goes over the various ways used to create OCR files. The OCR tool being used is Google’s Tesseract, which is an open source command line tool. There is a related python library, pytesseract, which is also open source and used here. 
Tesseract interacts most efficiently with TIFF files or PNG files. If you only have access to PDF files, it is worth looking into finding TIFF/PNG versions of the files, or converting the PDFs to TIFF/PNGs. This can be a lengthy process with varying results in terms of quality. However, the process for this will also be discussed. 

<> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <>

                               PART I
              ## WHAT TO DO WITH A MULTIPAGE PDF ##

<> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <>



		<> - - - <><> - - - <><> - - - <>

	1. Converting to individual pages using ImageMagick

		<> - - - <><> - - - <><> - - - <>

Note: This process is relatively slow, especially as you increase the density. Anything below around 800 will suffer badly in terms of quality. Anything much higher, and you can expect it to take quite a while for it to finishing converting. 

## 1-a. Option 1 ##

command line:

~ convert -colorspace rgb -density 800 InFile.pdf OutFile_%d.tif

density == the pixel density of the files
InFile.pdf == the multipage pdf you’d like to convert
OutFile_%d.tif == the name you’d like all of your TIFFs to have, with the “_%d” indicating that you’d like each output TIFF to be numbered sequentially. 


Sizing Note: A PDF that has a page size of 3.8 x 5.33 inches will become a TIFF that is 40.181 x 59.264 inches with a resolution of 72 pixels/ inch


## 1-b. Option 2 ##

command line:
~ convert -colorspace rgb -density 800 InFile.pdf -resize 25% OutFile_%d.tif

resize == changing the W x H of the image. The percentage amount indicate what percentage of the original sized image the final image will be, not what percentage amount it will be reduced by. (Ex: a 40 inch image —> a 10 inch image, NOT 40 inch image —> 30 inch image)


Sizing Note: A PDF that has a page size of 3.8 x 5.33 inches will become a TIFF that is 10.042 x 14.819 inches with a resolution of 72 pixels/ inch. You will notice this is 25% the size of the same command with the resizing tag. 


## 1-c. Option 3 ##

command line:
~ convert -units PixelsPerInch -colorspace rgb -density 800 InFile.pdf OutFile_%d.tif

units PixelsPerInch == tells imagemagick what unit the density is refering too (ppi)  

Sizing Note: A PDF that has a page size of 3.8 x 5.33 inches will become a TIFF that is 3.8 x 5.33 inches with a resolution of 800 pixels/ inch. You will notice the W x H of the image did not change from the original PDF, but the resolution was made to be 800 ppi. 

## 1-c. Option 3 ##

command line:
~ convert -units PixelsPerInch -colorspace rgb -density 800 InFile.pdf -resize 25% OutFile_%d.tif


Sizing Note: A PDF that has a page size of 3.8 x 5.33 inches will become a TIFF that is 0.95 x 1.334 inches with a resolution of 800 pixels/ inch. You will notice the W x H of the image is 25% of the original. 

NOTE: All of these options result in similar image quality, just different image sizes. All are good enough to be OCRed relatively reliably.  


		<> - - - <><> - - - <><> - - - <>

	2. Converting to individual pages using GhostScript

		<> - - - <><> - - - <><> - - - <>

GhostScript is an open source command line tool that is a PostScript and PDF lanugage interpreter and previewer. 

## Only Option (Currently)

command line:

   

-q == quite startup, suppresses normal start up messages, prevents GS from writing messages to standard output which can become mixed with the intended output stream

-dNOPAUSE == disables prompt and pause at end of peach page, meaning you don’t have to interact with the script until it’s finished with every page of the PDF

-sDEVICE == selects an alternate outpute device (meaning we get a TIFF and not a PDF)

-sOutputFile == indicates what the output file should be named, in this case:

Outfile_%d.tif == the actual name you’d like your TIFFs to have, with the %d indicating an additional sequential number at the end of the file name

InFile.pdf == the mulitpage PDF you’d like to convert

-c quit == ends the script


Note: This process is generally faster than imagemagick, and a bit more color true to the images. 

Sizing Note: A PDF that has a page size of 3.8 x 5.33 inches will become a TIFF that is 3.8 x 5.33 inches with a resolution of 800 pixels/ inch. 


		<> - - - <><> - - - <><> - - - <>

	3. Converting to a multi-page TIFF using GhostScript

		<> - - - <><> - - - <><> - - - <>


Used to create a multi-page TIFF from a multipage PDF. 
command line: 

~ gs -sDEVICE=tiff24nc -r800 -o OutFile.tif -dUseBigTIFF InFile.pdf

This will create a single, multi-page TIFF file. 
This is good if you’d like to eventually create a multi-page PDF file with OCR overlaid on it, which is discussed in PART II-2.


<> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <>

			      PART II
                         ## ADDING OCR ##

<> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <><> - - - <>



		<> - - - <><> - - - <><> - - - <>

		1. Adding OCR to multiple TIFFs

		<> - - - <><> - - - <><> - - - <>

## 1-a. Option 1 ##

Using Tesseract as a command line tool

command line: 
~ for i in *.tif: do tesseract $i $i; done;

This will take all TIFF files, perform ocr on them, then produce a TXT file for them with the same name the original file, except for an additional .txt extension. 

## 1-b. Option 2 ##

Using Tesseract in conjuction with Python and the pytesseract library. 

I have written a script (ocr.py) that uses pytesseract and cv2 to manipulate images for potentially better OCR results. 

This can be changed to better accomadate cropping, saturation, and coloring requirements for specific projects. 


Notes on both: certain methods will work better for certain images. I am still working on how to manipulate the images and what methods work best for which types of objects. Neither process takes extremely long, so comparing a few test samples from both methods might help you to decide which one to use.  


		<> - - - <><> - - - <><> - - - <>

		2. Adding OCR to a Multi Page TIFF

		<> - - - <><> - - - <><> - - - <>


This can be done if you have a multi-page TIFF (see Part I-3 for multi-page PDF -> multi-page TIFF conversion)

command line: 

~ tesseract -psm 1 -l eng InFile.tif OutFileWithOCR.pdf pdf
