from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet


def page_break():
    doc = SimpleDocTemplate("page-break.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    flowables = []

    text = "Hello i'am Paragraph"
    para = Paragraph(text, styles["Normal"])
    flowables.append(para)

    pagebreak = PageBreak()
    flowables.append(pagebreak)

    text = "Hello i'am Paragraph in page 2"
    para = Paragraph(text, styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    page_break()
