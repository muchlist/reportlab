from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def frame_demo():
    my_canvas = Canvas("frame-demo.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    heading = styles["Heading1"]

    flowables = []
    flowables.append(Paragraph('Heading #1', heading))
    flowables.append(Paragraph('ipsum lorem', normal))

    right_flowables = []
    right_flowables.append(Paragraph('Heading #2', heading))
    right_flowables.append(Paragraph('ipsum lorem', normal))

    left_frame = Frame(inch, inch, width=3*inch, height=9*inch, showBoundary=1)
    right_frame = Frame(4*inch, inch, width=3*inch, height=9*inch)

    left_frame.addFromList(flowables, my_canvas)
    right_frame.addFromList(right_flowables, my_canvas)

    my_canvas.save()


if __name__ == "__main__":
    frame_demo()
