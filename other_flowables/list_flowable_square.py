from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    SimpleDocTemplate,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet


def list_flowables_squares():
    doc = SimpleDocTemplate("list_flowables-sqiuares.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    normal = styles["Normal"]
    story = []

    flowables = [
        Paragraph('Paragraph pertama', normal),
        ListItem(Paragraph('Paragraph #2', normal),
                 bulletColor="blue"),
        Paragraph('Paragraph #3', normal)
    ]

    flowables.append(
        ListFlowable(
            [Paragraph("I'am sublist item", normal),
             ListItem(Paragraph("I'am another sublist item", normal),
                      bulletColor="blue"),
             ListItem(Paragraph("I'am the last sublist item", normal), bullerColor='red')],
            bulletType='bullet',
            start='square'
        )
    )

    lflow = ListFlowable(flowables, bulletType='I')
    story.append(lflow)

    doc.build(story)


if __name__ == "__main__":
    list_flowables_squares()
