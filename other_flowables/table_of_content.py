from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm


class MyDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        template = PageTemplate(
            'normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
        self.addPageTemplates(template)

    def afterFlowable(self, flowable):
        """Registers the table Of Contents entries"""
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Heading2':
                self.notify('TOCEntry', (1, text, self.page))


def main():
    heading1_style = ParagraphStyle(name='Heading1',
                                    fontsize=16,
                                    leading=16)
    heading2_style = ParagraphStyle(name='Heading2',
                                    fontsize=12,
                                    leading=14)

    story = []
    toc = TableOfContents()

    # set paragraph style in table of content
    toc.levelStyles = [heading1_style, heading2_style]
    story.append(toc)
    story.append(PageBreak())

    ipsum = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur porta ex rhoncus, auctor massa quis, consequat nunc. Integer tortor tortor, condimentum vitae accumsan ac, cursus ac diam. Donec molestie neque vitae nunc vulputate tristique. Sed quis eleifend dolor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum at nisl tempor lorem varius interdum ut eu neque. Duis suscipit efficitur velit nec hendrerit.
    '''

    story.append(Paragraph('Heading #1', heading1_style))
    story.append(Paragraph(ipsum, ParagraphStyle('body')))

    story.append(Paragraph('Sub-Heading #1', heading2_style))
    story.append(Paragraph(ipsum, ParagraphStyle('body')))

    story.append(PageBreak())

    story.append(Paragraph('Sub-Heading #2', heading2_style))
    story.append(Paragraph(ipsum, ParagraphStyle('body')))

    story.append(Paragraph('Heading #2', heading1_style))

    doc = MyDocTemplate('toc.pdf')
    doc.multiBuild(story)


if __name__ == "__main__":
    main()
