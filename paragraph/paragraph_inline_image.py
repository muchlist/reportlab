from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_inline_images():
    doc = SimpleDocTemplate("paragraph_inline_images.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    ptext = '''Here is a picture:
    <img src="Whats.jpeg" width="50" height="50"/> in middle of our text'''
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_inline_images()
