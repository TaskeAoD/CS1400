
# File name
html_file = "White_Hat_Page2.html"

def write_html(filename):
    """Creates an HTML file with content about White Hat Hackers."""
    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>White Hat Hackers</title>
</head>
<body>
    <h1>White Hat Hackers</h1>
    <p>White hat hackers, also known as ethical hackers, use their skills to protect systems from cyber threats. 
       They legally test security vulnerabilities and help organizations stay secure.</p>
    <h2>Roles of White Hat Hackers:</h2>
    <ul>
        <li>Conduct security testing.</li>
        <li>Improve cybersecurity defenses.</li>
        <li>Assist businesses in preventing cyber attacks.</li>
        <li>Train and educate others on ethical hacking.</li>
    </ul>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"HTML content written to {filename}")


def read_html(filename):
    """Reads and displays content from an HTML file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\n--- HTML File Content ---\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")


# File name
html_file = "White_Hat_Page2.html"

# Writing to an HTML file
write_html(html_file)

# Reading from the HTML file
read_html(html_file)
