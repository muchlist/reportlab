from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def paragraph_para_markup():
    doc = SimpleDocTemplate("Para_tag2.pdf",
                            pagesize=letter)
    styles = getSampleStyleSheet()
    # menambahkan style baru bernama Centered
    styles.add(ParagraphStyle(name='Centered', alignment=TA_CENTER))
    print(styles)

    flowables = []

    text = "<para align=center>Hello, I'm a Paragraph</para>"
    # menggunakan style centered
    para = Paragraph(text, style=styles["Centered"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_para_markup()
