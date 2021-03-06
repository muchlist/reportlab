from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


def coord(x, y, unit=1):
    x, y = x * unit, y * unit
    return x, y


c = canvas.Canvas("hello.pdf", bottomup=0)

c.drawString(*coord(50, 30, mm), text="welcome to Reportlab!")
c.showPage()
c.save()
