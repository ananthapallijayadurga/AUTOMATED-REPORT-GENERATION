from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
data = [
    ["City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"],
    ["Hyderabad", 32, 58, 4.6],
    ["Bengaluru", 28, 65, 3.2],
    ["Chennai", 34, 60, 5.1]
]
doc = SimpleDocTemplate("Weather_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []
elements.append(Paragraph("Automated Weather Report", styles["Title"]))
elements.append(Spacer(1, 20))
elements.append(Paragraph(
    "This report is automatically generated using Python and ReportLab. "
    "It presents analyzed weather data in a structured format.",
    styles["Normal"]
))
elements.append(Spacer(1, 20))
table = Table(data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold")
]))

elements.append(table)

doc.build(elements)

print("PDF Report Generated Successfully")
