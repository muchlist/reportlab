from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate,
                                Paragraph,
                                XPreformatted)
from reportlab.lib.styles import getSampleStyleSheet


def xpreformatted_paragraph():
    doc = SimpleDocTemplate("xpreformated_paragraph.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    text = """<font color=blue>Hello, I'am paragraph</font>"""
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    text = """Hello i'am a<font color=blue>XPreformater paragraph</font>"""
    para = XPreformatted(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    xpreformatted_paragraph()
