from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def hello():
    doc = SimpleDocTemplate("hello_platypus.pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftmargin=72,
                            topMargin=72,
                            bottomMargin=18)
    styles = getSampleStyleSheet()
    flowables = []
    text = "Hello, I'am Paragraph asdasdasd adasdasdas asdasdsadasd asdasdasdsad asdasdasd asdasdasdasd adsasdasdas adadasdasd"
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    hello()
