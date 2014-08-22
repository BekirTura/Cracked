#!/usr/bin/python 

print("Cracking...")
f=open("LD-ENGTUR.EXE","rb")
s=str(f.read())
f.close()
s=s.replace('\x8b\xce\x74\x3a', '\x8b\xce\x74\x06')

with open("LD-ENGTUR-CRACKED.EXE","wb") as f:
  f.write(s)
  
  print("done...")

