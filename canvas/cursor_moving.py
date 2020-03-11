from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def textobject_cursor():
    canvas_obj = canvas.Canvas("textobj_cursor.pdf", pagesize=letter)

    # Create text object
    textobject = canvas_obj.beginText()

    # set text location
    textobject.setTextOrigin(10, 730)

    for indent in range(4):
        textobject.textLine('Reportlab Cursor Demo')
        #dx , dy geser ke kanan 15, geser kebawah 15
        textobject.moveCursor(15, 15)

    canvas_obj.drawText(textobject)
    canvas_obj.save()


if __name__ == "__main__":
    textobject_cursor()
