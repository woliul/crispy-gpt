import markdown
import weasyprint

def markdown_to_pdf(markdown_file, output_pdf):
    # Read the markdown file
    with open(markdown_file, 'r') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Convert HTML to PDF using WeasyPrint
    weasyprint.HTML(string=html_content).write_pdf(output_pdf)

    print(f"PDF saved as {output_pdf}")

# Provide the path to your Markdown file and desired output PDF file name
markdown_file = 'test/Input/Python180.md'
output_pdf = 'test/Output/testoutput4.pdf'

markdown_to_pdf(markdown_file, output_pdf)
