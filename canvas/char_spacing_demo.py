from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def textobject_char_spacing():
    canvas_obj = canvas.Canvas("textobj_char_spacing.pdf", pagesize=letter)

    textobject = canvas_obj.beginText()
    textobject.setTextOrigin(10, 730)

    spacing = 0
    for indent in range(8):
        #set char  membuat jarak antar huruf
        textobject.setCharSpace(spacing)
        #set word membuat jarak antar word
        textobject.setWordSpace(spacing)
        line = f"{spacing} - reportlab spacing"
        textobject.textLine(line)
        spacing += 0.7

    canvas_obj.drawText(textobject)
    canvas_obj.save()


if __name__ == "__main__":
    textobject_char_spacing()
