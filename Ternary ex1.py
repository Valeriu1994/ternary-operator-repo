user = input("user: ").strip()
user = input("parola: ").strip()

ok = (user == "admin" and pwd == "1234")
msg = "Autenficat" if ok else "Credintiale invalide"
print (msg)