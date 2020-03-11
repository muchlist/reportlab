from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def apply_scripting(textobject, text, rise):
    textobject.setFont("Helvetica-Oblique", 8)
    #set rise plus maka text keatas (pangkat), minus maka text kebawah
    textobject.setRise(rise)
    textobject.textOut(text)
    textobject.setFont("Helvetica-Oblique", 12)
    textobject.setRise(0)


def main():
    canvas_obj = canvas.Canvas("textobj_rising.pdf", pagesize=letter)

    # create text object
    textobject = canvas_obj.beginText()
    textobject.setFont("Helvetica-Oblique", 12)

    # set text location (x, y)
    textobject.setTextOrigin(10, 730)

    textobject.textOut('ReportLab ')
    apply_scripting(textobject, 'superscript', 7)

    textobject.textOut('and ')
    apply_scripting(textobject, 'subscript', -7)

    canvas_obj.drawText(textobject)
    canvas_obj.save()


if __name__ == "__main__":
    main()