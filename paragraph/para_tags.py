from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_para_markup():
    doc = SimpleDocTemplate("para_tags.pdf",
                            pagesize=letter)
    styles = getSampleStyleSheet()

    flowables = []

    # dibungkus xml para untuk memakai xml center dan sebagainya
    text = "<para align=center>Hello, I'm a Paragraph</para>"
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_para_markup()
