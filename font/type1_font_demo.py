import os
import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def embedded_font_demo():
    my_canvas = canvas.Canvas("type_font_demo.pdf", pagesize=letter)
    reportlab_folder = os.path.dirname(reportlab.__file__)
    fonts_folder = os.path.join(reportlab_folder, 'fonts')

    print(f'ReportLab font folder is located at {fonts_folder}')
    afm = os.path.join(fonts_folder, 'DarkGardenMK.afm')
    pfb = os.path.join(fonts_folder, 'DarkGardenMK.pfb')

    # register the font so we can use it
    font_face = pdfmetrics.EmbeddedType1Face(afm, pfb)
    pdfmetrics.registerTypeFace(font_face)

    face_name = 'DarkGardenMK'
    font = pdfmetrics.Font('DarkGardenMK', face_name, 'WinAnsiEncoding')
    pdfmetrics.registerFont(font)

    # use the font!
    my_canvas.setFont('DarkGardenMK', 40)
    my_canvas.drawString(10, 730, 'The DarkGardenMK font')

    my_canvas.save()


if __name__ == "__main__":
    embedded_font_demo()
