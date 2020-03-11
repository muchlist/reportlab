from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

#Memasukkan flowable ke canvas menggunakan wrapOn dan drawOn
def mixed():
    my_canvas = canvas.Canvas("Mixed_flowables.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    width, height = letter

    text = "Hello, i'am a Paragraph"
    para = Paragraph(text, style= styles["Normal"])
    para.wrapOn(my_canvas, width, height)
    para.drawOn(my_canvas, 20, 760)

    my_canvas.save()

if __name__ == "__main__":
    mixed()