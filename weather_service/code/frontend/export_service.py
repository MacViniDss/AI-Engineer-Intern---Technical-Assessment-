import json
from fpdf import FPDF

def export_json(data: dict) -> str:
    return json.dumps(data, indent=4)

def export_markdown(data: dict) -> str:
    md = f"# Weather in {data.get('name', 'Unknown Location')}\n\n"
    md += f"- **Temperature:** {data['main']['temp']} °C\n"
    md += f"- **Condition:** {data['weather'][0]['description'].title()}\n"
    md += f"- **Humidity:** {data['main']['humidity']}%\n"
    md += f"- **Wind Speed:** {data['wind']['speed']} m/s\n"
    return md
