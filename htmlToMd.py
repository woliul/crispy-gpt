from bs4 import BeautifulSoup
import html2text

def extract_latex_from_katex(tag):
    """Extract raw LaTeX from a KaTeX tag"""
    annotation = tag.find("annotation", {"encoding": "application/x-tex"})
    return annotation.get_text(strip=True) if annotation else ""

def preprocess_katex(html):
    """Replace KaTeX blocks in HTML with LaTeX markers"""
    soup = BeautifulSoup(html, "html.parser")

    # Replace display math
    for div in soup.find_all("div", class_="katex-display"):
        latex = extract_latex_from_katex(div)
        div.replace_with(soup.new_string(f"\n\n$$\n{latex}\n$$\n\n"))

    # Replace inline math
    for span in soup.find_all("span", class_="katex"):
        if not span.find_parent("div", class_="katex-display"):
            latex = extract_latex_from_katex(span)
            span.replace_with(soup.new_string(f"${latex}$"))

    return str(soup)

def html_to_markdown(html):
    """Convert HTML to Markdown, preserving math"""
    preprocessed_html = preprocess_katex(html)
    h = html2text.HTML2Text()
    h.body_width = 0  # Disable line wrapping
    h.ignore_images = False
    h.ignore_links = False
    h.ignore_emphasis = False
    return h.handle(preprocessed_html)

# Example usage
if __name__ == "__main__":
    with open("test/Input/testhtml.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    markdown = html_to_markdown(html_content)

    with open("test/Output/testmdoutput.md", "w", encoding="utf-8") as f:
        f.write(markdown)
