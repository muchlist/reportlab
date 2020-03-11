from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def textobject_demo():
    my_canvas = canvas.Canvas("txt_obj.pdf", pagesize=letter)

    # create text object
    textobject = my_canvas.beginText()
    # set text location (x, y)
    textobject.setTextOrigin(10, 730)
    textobject.setFont('Times-Roman', 12)

    # write a line of text
    textobject.textLine(text='Python rocks!')

    # write red text
    textobject.setFillColor(colors.red)
    textobject.textLine(text='Python rocks in red!')

    # write text to the canvas
    my_canvas.drawText(textobject)

    my_canvas.save()


if __name__ == '__main__':
    textobject_demo()
