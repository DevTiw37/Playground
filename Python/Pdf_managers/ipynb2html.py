# This program converts python notebook file into html

from nbconvert import HTMLExporter

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
