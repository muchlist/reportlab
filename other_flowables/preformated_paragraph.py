from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate,
                                Paragraph,
                                Preformatted)
from reportlab.lib.styles import getSampleStyleSheet


def preformatted_paragraph():
    doc = SimpleDocTemplate("preformated_paragraph.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    text = "<para align=center>Hello, I'm a paragraph</para>"
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    text = "<para align=center>Hello, I'm a preformated paragraph</para>"
    para = Preformatted(text, style=styles["Code"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    preformatted_paragraph()
