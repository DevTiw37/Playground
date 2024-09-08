import webbrowser

# Open the text file containing URLs
with open('urls.txt', 'r') as file:
  urls = [line.strip().split()[1] for line in file]  # Extract only the second element after split

# Open each URL in a new tab
for url in urls:
  webbrowser.open_new_tab(url)