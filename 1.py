
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
target_hashes = [
 "cf8e69a40709c2460e8788ec8894f2a385c9de21",
 "2bd5fb5dde0bda1e70978f37bc5b9b982cad1395",
 "b1ade531057f51c2992479335d03b774afdeb6fa",
]
result_words = []
used = [False] * len(decoded)
for h in target_hashes:
    for i, word in enumerate(decoded):
        if not used[i] and hashlib.sha1(word.encode()).hexdigest() == h:
            result_words.append(word)
            used[i] = True
            break
        
message = " ".join(result_words)
fingerprint = hashlib.sha256(message.encode()).hexdigest()
print("\nFingerprint:", fingerprint[:12])
print("FINAL LOCATION:")
print(message)