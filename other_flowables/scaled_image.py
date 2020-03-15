from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib import utils


def scaled_image(desire_width):
    doc = SimpleDocTemplate("scaled_image.pdf", pagesize=letter)
    story = []

    img = utils.ImageReader('python.jpg')
    img_width, img_height = img.getSize()

    aspect = img_height / float(img_width)

    img = Image("python.jpg", width=desire_width, height=(desire_width * aspect))
    img.hAlign = 'CENTER'

    story.append(img)
    doc.build(story)


if __name__ == "__main__":
    scaled_image(200)
