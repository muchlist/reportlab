from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100, 100, "Welcome Muchlis to PDFLAB!")
c.showPage()
c.save()
