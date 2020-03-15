from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    SimpleDocTemplate,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet


def list_flowables_demo():
    doc = SimpleDocTemplate("list_flowables.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    normal = styles["Normal"]
    story = []

    flowables = [
        Paragraph('Paragraph pertama', normal),
        ListItem(Paragraph('Paragraph #2', normal),
                 bulletColor="blue", value=5),
        Paragraph('Paragraph #3', normal)
    ]

    lflow = ListFlowable(flowables)
    story.append(lflow)

    doc.build(story)


if __name__ == "__main__":
    list_flowables_demo()
