
print("[+] Read whole File [+]")
with open("ports.txt") as line:
	print(line.read())

print("[+] Read line by line [+]")
with open("services.txt") as line:
	for txt in line:
		print("Lines: "+txt.rstrip())
