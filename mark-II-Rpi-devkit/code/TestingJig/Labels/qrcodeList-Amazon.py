#!/usr/bin/env python3.4

'''
Use these labels:
https://smile.amazon.com/gp/product/B014IPO134/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
White Rectangular Labels + Bonus Color Labels - Value Pack - White Coding Labels Produce Excellent Results with Standard Laser Printer-Template Included! 1138 Pack
White Sticker size: 1" x 0.375";

'''
import tempfile
import csv

from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
import qrcode
import qrcode.image.svg
from svglib.svglib import svg2rlg

point = 1
inch = 72
csvList = []
line_count = 0
with open('MycroftSerialNumbers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        csvList.append(row[0])
        line_count = line_count + 1
	
def make_qr_code_drawing(data, size):
    qr = qrcode.QRCode(
        version=1,  # QR code version a.k.a size, None == automatic
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # lots of error correction
        box_size=size,  # size of each 'pixel' of the QR code
        border=4  # minimum size according to spec
        )
    qr.add_data(data)
    qrcode_svg = qr.make_image(image_factory=qrcode.image.svg.SvgPathFillImage)
    svg_file = tempfile.NamedTemporaryFile()
    qrcode_svg.save(svg_file)  # store as an SVG file
    svg_file.flush()
    qrcode_rl = svg2rlg(svg_file.name)  # load SVG file as reportlab graphics
    svg_file.close()
    return qrcode_rl

def make_pdf_file(output_filename, data):
    global line_count
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    topMarg    = 0.38
    leftMarg   = 0.44
    horizPitch = 1.1
    vertPitch  = 0.471
    '''
    c.grid([leftMarg*inch,
            leftMarg*inch + horizPitch * inch * 1, 
            leftMarg*inch + horizPitch * inch * 2,
            leftMarg*inch + horizPitch * inch * 3,
            leftMarg*inch + horizPitch * inch * 4,
            leftMarg*inch + horizPitch * inch * 5,
            leftMarg*inch + horizPitch * inch * 6,
            leftMarg*inch + horizPitch * inch * 7], 
            [topMarg*inch, 
            topMarg*inch + vertPitch * inch * 1,
            topMarg*inch + vertPitch * inch * 2,
            topMarg*inch + vertPitch * inch * 3,
            topMarg*inch + vertPitch * inch * 4,
            topMarg*inch + vertPitch * inch * 5,
            topMarg*inch + vertPitch * inch * 6,
            topMarg*inch + vertPitch * inch * 7,
            topMarg*inch + vertPitch * inch * 8,
            topMarg*inch + vertPitch * inch * 9,
            topMarg*inch + vertPitch * inch * 10,
            topMarg*inch + vertPitch * inch * 11,
            topMarg*inch + vertPitch * inch * 12,
            topMarg*inch + vertPitch * inch * 13,
            topMarg*inch + vertPitch * inch * 14,
            topMarg*inch + vertPitch * inch * 15,
            topMarg*inch + vertPitch * inch * 16,
            topMarg*inch + vertPitch * inch * 17,
            topMarg*inch + vertPitch * inch * 18,
            topMarg*inch + vertPitch * inch * 19,
            topMarg*inch + vertPitch * inch * 20,
            topMarg*inch + vertPitch * inch * 21,
            topMarg*inch + vertPitch * inch * 22,
            ])
    '''
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12 * point)
    count = 0

    while count < line_count:
        for col in range(7):
            for i in range(22):
                if(count < line_count):
                    currentSerial = data[count]
                    #currentSerialStr = "0x{:08x}".format(currentSerial).upper()[2:10]
                    currentSerialStr = currentSerial
                    print(currentSerialStr)
                    qrcode_rl = make_qr_code_drawing(currentSerialStr, 3.5)
                    left1 = leftMarg * inch + (col * 1 )   * horizPitch * inch
                    #left1 = leftMarg * inch + (col * 2 )   * horizPitch * inch
                    #left2 = leftMarg * inch + (col * 2 + 1)* horizPitch * inch
                    top  = (11 - topMarg * 2.0 - vertPitch * i) * inch
                    renderPDF.draw(qrcode_rl, c,left1 + 0.1 * inch, top + 0.05 * inch )
                    #renderPDF.draw(qrcode_rl, c,left2 + 0.1 * inch, top + 0.05 * inch )
                    c.drawString( left1 + 0.5 * inch, top + 0.25  * inch, currentSerialStr[0:4] )
                    #c.drawString( left2 + 0.5 * inch, top + 0.25  * inch, currentSerialStr[0:4] )
                    #print( currentSerialStr[0:4])
                    c.drawString( left1 + 0.5 * inch, top + 0.08  * inch, currentSerialStr[4:9] )
                    #c.drawString( left2 + 0.5 * inch, top + 0.08  * inch, currentSerialStr[4:9] )
                    #print( currentSerialStr[4:8])
                    #currentSerial = currentSerial + 1
                    count = count + 1
        c.showPage()
    c.save()
    

if __name__ == "__main__":
    filename = "label.pdf"
    #make_pdf_file(filename, 0x01AABBCC)
    make_pdf_file(filename, csvList)