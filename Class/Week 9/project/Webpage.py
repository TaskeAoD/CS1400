import webbrowser

def generate_html(webpage, topic, description, uses):   #Generates an HTML file with the topic, description, and list of uses from variables below.
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{topic}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; padding: 20px; }}
            h1 {{ color: #A947FF; }}
            p {{ font-size: 16px; line-height: 1.5; }}
            ul {{ margin-top: 10px; }}
            li {{ font-size: 14px; }}
        </style>
    </head>
    <body>
        <h1>{topic}</h1>
        <p>{description}</p>
        <h2>Ways to use this topic</h2>
        <ul>
            {"".join(f"<li>{use}</li>" for use in uses)}
        </ul>
    </body>
    </html>
    """

    with open(webpage, "w") as file:
        file.write(html_content)

    print(f"Web page '{webpage}' created successfully!")

    webbrowser.open(webpage)   #Open the generated file in the default web browser

#Get info for webpage

webpage = input("Enter the filename (without extension): ") + ".html"  #Doing this to prevent issue of writing double extensions
topic = input("Enter the topic of the page: ")
description = input("Enter a brief explanation (3-4 sentences): ")
print("Enter 3 ways to use this topic or other related information.")
uses = [input(f"Way {i+1}: ") for i in range(3)]

# Generate and open the HTML page
generate_html(webpage, topic, description, uses)
