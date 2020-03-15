from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Spacer,
    Paragraph,
    Image)
from reportlab.lib import colors


def table_with_images():
    doc = SimpleDocTemplate("table_with_images.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    img = Image("Whats.jpeg", 50, 50, hAlign='CENTER')

    ptext = 'This is some <font color=blue size=14>formated</font> text'
    p = Paragraph(ptext, styles["Normal"])

    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [p for x in range(1, 6)],
        [img, img, img, img, img]
    ]

    tblstyle = TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)

    story.append(tbl)

    doc.build(story)


if __name__ == "__main__":
    table_with_images()
