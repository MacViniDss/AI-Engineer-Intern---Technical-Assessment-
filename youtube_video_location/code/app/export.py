import json
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def export_json(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def export_md(data, filename="output.md"):
    with open(filename, "w") as f:
        for v in data:
            f.write(f"- [{v['title']}]({v['url']})\n")


def export_pdf(data, filename="output.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []
    for v in data:
        elements.append(Paragraph(f"{v['title']} - {v['url']}", styles["Normal"]))

    doc.build(elements)
    