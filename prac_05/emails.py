email = input("Email: ")
parts = email.split("@")[0]
name_parts = parts.split(".")
name = " ".join(name_parts)
print(name)