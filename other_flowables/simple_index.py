from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate,
                                Paragraph,
                                PageBreak)
from reportlab.platypus.tableofcontents import SimpleIndex
from reportlab.lib.styles import getSampleStyleSheet


def simple_index():
    doc = SimpleDocTemplate("simple_index.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    ptext = """
    I'am custom <index item="bulletted"/>bulleted paragraph
    """
    para = Paragraph(ptext, styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())

    ptext = """
    <index item="Python"/>Python is an indexed word
    """
    para = Paragraph(ptext, styles["Normal"], bulletText='-')
    flowables.append(para)

    index = SimpleIndex(dot='.')
    flowables.append(PageBreak())
    flowables.append(index)

    doc.build(flowables, canvasmaker=index.getCanvasMaker())


if __name__ == "__main__":
    simple_index()
