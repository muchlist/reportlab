from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_spacing():
    doc = SimpleDocTemplate("paragraph_spacing.pdf", pagesize=letter)

    styles = getSampleStyleSheet()
    #Mengahasilkan spasi antar paragraf sehinga tidak diperlukan <br/>
    styles["Normal"].spaceBefore = 10
    styles["Normal"].spaceAfter = 10

    flowables = []

    text = """
    This <b>text</b> is important,
    not <strong>strong</strong>.
    """
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    text = """
    This <b>text</b> is important,
    not <strong>strong</strong>.
    """
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_spacing()
