tool.py
 
# ✅ CHANGES MADE:

# 1️⃣ Removed the class-based approach (no BaseTool subclass).

# 2️⃣ Added the @tool decorator from crewai.tools.

# 3️⃣ Function name and docstring updated to describe purpose.

# 4️⃣ Handles CSV, PDF, TXT, DOCX, JSON safely.

# 5️⃣ Compatible with CrewAI v1.1.0 (no __init__ inheritance needed).
 
from crewai.tools import tool
import csv
import json
import PyPDF2
from docx import Document
 
@tool("read_file_tool")
def read_file_tool(file_path: str):
    """
    Reads and returns content from CSV, PDF, TXT, DOCX, or JSON files.
    """

    file_type = file_path.split(".")[-1].lower()
    try:
        if file_type == "csv":
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = [row for row in reader]
            return data
        elif file_type == "pdf":
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return text
        elif file_type == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif file_type == "docx":
            doc = Document(file_path)
            full_text = "\n".join([p.text for p in doc.paragraphs])
            return full_text
        elif file_type == "json":
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return f"File type .{file_type} is not supported."
    except Exception as e:
        return f"Error reading file: {str(e)}"