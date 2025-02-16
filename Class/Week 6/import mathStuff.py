import mathStuff

x = ''
y = ''

x = float(input("Please enter first number for maths: "))
y = float(input("Please enter second number for maths: "))

print(mathStuff.add(x, y))
print(mathStuff.multiply(x, y))
print(mathStuff.evaluate(mathStuff.add(x, y)))
print(mathStuff.evaluate(mathStuff.multiply(x, y)))