import markdown
import weasyprint

def markdown_to_pdf(markdown_file, output_pdf):
    # Read the markdown file
    with open(markdown_file, 'r') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Wrap the HTML content in a simple HTML structure for better styling
    html_template = f"""
    <html>
    <head>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF using WeasyPrint
    weasyprint.HTML(string=html_template).write_pdf(output_pdf)

    print(f"PDF saved as {output_pdf}")

# Provide the path to your Markdown file and desired output PDF file name
markdown_file = 'test/Input/Python180.md'
output_pdf = 'Python180.pdf'

markdown_to_pdf(markdown_file, output_pdf)
