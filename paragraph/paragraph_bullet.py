from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_bullet():
    doc = SimpleDocTemplate("paragraph_bullets.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    flowables = []

    ptext = "I'm a custom bulleted paragraph"
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)

    ptext = "This is Normal bullet"
    para = Paragraph(ptext, style=styles["Normal"], bulletText='\xe2\x80\xa2')
    flowables.append(para)

    ptext = "<bullet>&bull;</bullet>This is Used bullet tag"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_bullet()
