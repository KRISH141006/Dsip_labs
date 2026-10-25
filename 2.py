
import hashlib
import base64
print("=== MIND BYTE CLUE ===")
print("Decode the clues below. The correct sequence reveals the destination.\n")
clues = [
 "NXRo",
 "c2hlbGY=",
 "cmVsaWM=",
 "ZW50ZXJhbmNl",
 "Y2VudHJl",
 "c2VtaW5hciBoYWxs",
 "Zmxvb3I=",
 "Z2FyZGVu",
]
decoded = [base64.b64decode(c).decode() for c in clues]

print("Recovered clues:")
for word in decoded:
 print("-", word)

