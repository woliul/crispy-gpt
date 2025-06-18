import markdown
import weasyprint

def markdown_to_pdf(markdown_file, output_pdf):
    # Read the markdown file with UTF-8 encoding
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Convert markdown to HTML
    # Use the 'codehilite' extension for better code block styling
    html_content = markdown.markdown(md_content, extensions=['fenced_code'])

    # Simplified HTML structure with minimal styling
    html_with_encoding = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        /* Simple styling for code blocks */
        pre, code {{
            background-color: #f4f4f4;
            border-radius: 5px;
            padding: 10px;
            font-family: "Courier New", monospace;
            font-size: 14px;
        }}
        pre {{
            overflow-x: auto;  /* Enable horizontal scroll for long lines */
            white-space: pre-wrap;  /* Ensure code wraps */
            word-wrap: break-word;  /* Break words to avoid overflow */
            margin-bottom: 20px;  /* Space between code blocks */
        }}
    </style>
</head>
<body>{html_content}</body>
</html>'''

    # Convert HTML to PDF using WeasyPrint
    try:
        weasyprint.HTML(string=html_with_encoding).write_pdf(output_pdf)
        print(f"PDF saved as {output_pdf}")
    except Exception as e:
        print(f"Error during PDF generation: {e}")

# Provide the path to your Markdown file and desired output PDF file name
markdown_file = 'test/Input/Python180.md'  # Your Markdown file
output_pdf = 'output5.pdf'  # Desired output PDF name

markdown_to_pdf(markdown_file, output_pdf)
