prompt = ("Enter a city you would like to visit: ")
prompt += ("\n Enter 'quit' when you done. ")

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}")