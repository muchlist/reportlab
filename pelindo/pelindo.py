from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
#import time


def pelindo_form():
    # A4 = (210*mm,297*mm)
    doc = SimpleDocTemplate("pelindo.pdf",
                            pagesize=A4,
                            rightMargin=72,
                            leftmargin=72,
                            topMargin=5,
                            bottomMargin=5)
    story = []

    """
    ------------------------------------------------------------------------
    DATA HEADER
    """
    img = Image("pelindo.png", 68, 50, hAlign='CENTER')
    data = [
        [img, "Sistem Manajemen\nMutu, Keselamatan & Kesehatan Kerja, Keamanan, dan Lingkungan"],
        ["", "FORMULIR\nCONTAINER DAMAGE REPORT"]
    ]

    # (SPAN, (begincol, beginrow), (endcol, endrow))
    tblstyle = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('SPAN', (0, 0), (0, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ])

    tbl = Table(data, colWidths=[30*mm, 160*mm])
    tbl.setStyle(tblstyle)
    story.append(tbl)
    story.append(Spacer(0, 10))

    """
    -------------------------------------------------------------------------
    DATA DETAIL KONTAINER
    """
    data = [
        ["KONTAINER", ": MRTU 1234567", "AKTIFITAS",  ": MUAT"],
        ["UKURAN", ": 20 FEET", "KAPAL",  ": MERATUS BORNEO"],
        ["TIPE",  ": TNK", "VOYAGE",  ": 001"],
        ["STATUS",  ": FULL", "INT/DOM",  ": DOMESTIK"],
        ["TANGGAL",  ": 01-Jan-2020 09:00", "", ""],
    ]

    tbl = Table(data, colWidths=[27*mm, 57*mm, 27*mm, 77*mm])
    story.append(tbl)
    story.append(Spacer(0, 10))

    """
    -------------------------------------------------------------------------
    DATA STATUS PENGECEKAN HEADER
    """

    data = [
        ["DETAIL PENGECEKAN"],
    ]

    tblstyle = TableStyle([
        ('GRID', (0, 0), (0, 0), 0.25, colors.black),
        ('ROWBACKGROUNDS', (0, 0), (0, 0), [colors.lightblue]),
        ('ALIGN', (0, 0), (0, 0), 'CENTER')
    ])

    tbl = Table(data, colWidths=[190*mm])
    tbl.setStyle(tblstyle)
    story.append(tbl)
    story.append(Spacer(0, 5))

    """
    -------------------------------------------------------------------------
    DATA STATUS PENGECEKAN
    """

    data = [
        # Header Table
        ["WAKTU", "LOKASI", "OLEH", "SAKSI", "CATATAN", "STATUS"],
        ["10-Mar 09:00", "GATEIN", "MUCHLIS", "MAMAN", "Nihil", "GOOD"],
        ["10-Mar 12:00", "LOADING", "MUCHLIS", "MAMAN",
            para("kontainer sebelah kiri terpotong dan berlubang"), "CUT"],
        ["10-Mar 12:05", "LOADING", "MUCHLIS", "MAMAN",
            para("Kontainer terbakar dengan sendirinya, negara api menyerang ?"), "BURN"],
        ["10-Mar 12:05", "LOADING", "MUCHLIS", "MAMAN",
            para("Kontainer terbakar dengan sendirinya, negara api menyerang ?"), "BURN"],
        ["10-Mar 12:05", "LOADING", "MUCHLIS", "MAMAN",
            para("Kontainer terbakar dengan sendirinya, negara api menyerang ?"), "BURN"],
    ]

    tblstyle = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ROWBACKGROUNDS', (0, 0), (-1, 0), [colors.lightblue]),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 1), (-1, -1), "TOP"),
    ])

    tbl = Table(data, colWidths=[30*mm, 20*mm, 25*mm, 25*mm, 70*mm, 20*mm])
    tbl.setStyle(tblstyle)
    story.append(tbl)
    story.append(Spacer(0, 5))

    """
    -------------------------------------------------------------------------
    TANDA TANGAN
    """
    img = Image("qr.png", width=80, height=80)
    data = [
        ["SHIP'S AGENT", "VESSEL FOREMAN"],
        [img, img],
        ["ANTONIUS BOOMERANG", "MUCHLIS"],
    ]
    tblstyle = TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), "MIDDLE"),
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
    ])
    tbl = Table(data, colWidths=[95*mm, 95*mm])
    tbl.setStyle(tblstyle)
    story.append(tbl)
    
    story.append(Spacer(0, 10))



    """
    -------------------------------------------------------------------------
    FOTO HEADER
    """

    data = [
        ["FOTO KONTAINER"],
    ]

    tblstyle = TableStyle([
        ('GRID', (0, 0), (0, 0), 0.25, colors.black),
        ('ROWBACKGROUNDS', (0, 0), (0, 0), [colors.lightblue]),
        ('ALIGN', (0, 0), (0, 0), 'CENTER')
    ])

    tbl = Table(data, colWidths=[190*mm])
    tbl.setStyle(tblstyle)
    story.append(tbl)
    story.append(Spacer(0, 5))

    """
    -------------------------------------------------------------------------
    FOTO
    """
    img = scale_image("test.jpg", 55*mm)
    data = [
        [img, img, img],
        [img, img, img],
    ]
    tblstyle = TableStyle([
        ('VALIGN', (0, 0), (-1, -1), "MIDDLE"),
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
    ])
    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)
    story.append(Spacer(0, 5))

    """
    -------------------------------------------------------------------------
    Disclaimer
    """
    data = [
        [para("""Catatan : Setiap kerusakan pada kontainer atau kargo yang ditemukan
     sebelum kontainer dibongkar dari kapal bukan tanggung jawab dari
     PT. PELABUHAN INDONESIA III""")],
    ]

    tbl = Table(data, colWidths=[190*mm])
    story.append(tbl)

    doc.build(story)


def para(text: str) -> Paragraph:
    """
    Menginputkan text dan mengembalikan paragraph normal
    """
    normal_style = getSampleStyleSheet()["Normal"]
    return Paragraph(text, normal_style)


def scale_image(image: str, desire_width: int) -> Image:
    """
    Menginputkan path image dan width dan mengembalikan scaled image
    """

    img = ImageReader(image)
    img_width, img_height = img.getSize()
    aspect = img_height / float(img_width)

    img = Image(image, width=desire_width, height=(
        desire_width * aspect), hAlign='CENTER')

    return img


if __name__ == "__main__":
    #tic = time.perf_counter()
    pelindo_form()
    #toc = time.perf_counter()
    #print(f"Membuat PDF dalam {toc - tic:0.4f} detik")
