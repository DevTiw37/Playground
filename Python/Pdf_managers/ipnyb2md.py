from nbconvert import HTMLExporter
import html2text
# import bs4

ipynb_file = r"C:\Users\Asus\Downloads\dsmp-task-and-solution-20240820T172913Z-001\dsmp-task-and-solution\week-1\1-session_1_tasks.ipynb"
html_file = "output.html"
exporter = HTMLExporter()
try:
    (body, resources) = exporter.from_filename(ipynb_file)
    with open(html_file, 'w') as f:
        f.write(body)
    print("Conversion successful!")
except Exception as e:
    print("Error during conversion:", e)




def html_to_markdown(markdown_file):
    """Converts an HTML file to a Markdown file.

    Args:
        html_file (str): Path to the HTML file.
        markdown_file (str): Path to the output Markdown file.
    """

    # with open(html_file, 'r') as html_input, open(markdown_file, 'w') as markdown_output:
    with open(markdown_file, 'w') as markdown_output:
        markdown_content = html2text.html2text(body)
        markdown_output.write(markdown_content)

if __name__ == '__main__':
    markdown_file_path = 'your_markdown_file.md'
    html_to_markdown(markdown_file_path)
    print("HTML file converted to Markdown successfully!")