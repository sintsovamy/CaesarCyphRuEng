text = input()
cyphertext = ""
rot = int(input())
for c in text:
  if c not in "!#$%&*+-=?@^_,." and c != " ":
    if c >= "А" and c <= "Я":
      c = chr(ord("А") + (ord(c) + rot) % ord ("А") % 32)
    elif c >= "а" and c <= "я":
      c = chr(ord("а") + (ord(c) + rot) % ord ("а") % 32)
    elif c >= "A" and c <= "Z":
      c = chr(ord("A") + (ord(c) + rot) % ord ("A") % 26)
    elif c >= "a" and c <= "z":
      c = chr(ord("a") + (ord(c) + rot) % ord ("a") % 26)
  cyphertext +=c
print(cyphertext)