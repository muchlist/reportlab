from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image


def full_size_image():
    doc = SimpleDocTemplate("image_ful_size.pdf", pagesize=letter)
    story = []

    img = Image("python.jpg")
    story.append(img)
    doc.build(story)


def no_scaling():
    doc = SimpleDocTemplate("image_no_scaling_.pdf", pagesize=letter)
    story = []

    img = Image("python.jpg", width=50)
    story.append(img)
    doc.build(story)


if __name__ == "__main__":
    full_size_image()
    no_scaling()
