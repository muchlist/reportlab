from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch


def first_page(canvas, document):
    title = 'PLATYPUS demo'
    PAGE_HEIGHT = defaultPageSize[1]
    PAGE_WIDTH = defaultPageSize[0]
    canvas.saveState()
    canvas.setFont('Times-Bold', 18)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, title)

    canvas.setFont('Times-Roman', 10)
    text = 'Welcome to the first PLATYPUS Page!'
    canvas.drawString(inch, 10*inch, text)
    canvas.restoreState()


def later_pages(canvas, document):
    canvas.saveState()
    canvas.setFont('Helvetica', 10)
    #membuat nomer halaman 7 inch kekanan 0.5 inch keatas dari bawah
    canvas.drawString(7*inch, 0.5*inch, f'Page {document.page}')
    canvas.restoreState()


def create_document():
    doc = SimpleDocTemplate("platypus_first_later.pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18) #showBoundary=True
    styles = getSampleStyleSheet()
    flowables = []
    spacer = Spacer(1, 0.25*inch)

    # Create alot of context to make multipage pdf
    for i in range(50):
        text = f'paragraph #{i}'
        para = Paragraph(text, styles["Normal"])
        flowables.append(para)
        flowables.append(spacer)

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)
    #doc.build(flowables)


if __name__ == "__main__":
    create_document()
