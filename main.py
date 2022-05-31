text = input()
cyphertext = ""
rot = int(input())
for c in text:
  if c not in "!#$%&*+-=?@^_,." and c != " ":
    if c >= "А" and c <= "Я":
      c = chr((ord(c) + rot - ord("А")) % 32 + ord("А"))
    elif c >= "а" and c <= "я":
      c = chr((ord(c) + rot - ord("а")) % 32 + ord("а"))
    elif c >= "A" and c <= "Z":
      c = chr((ord(c) + rot - ord("A")) % 26 + ord("A"))
    elif c >= "a" and c <= "z":
      c = chr((ord(c) + rot - ord("a")) % 26 + ord("a"))
  cyphertext +=c
print(cyphertext)
print(chr(ord("а") + ((ord("ж") + rot) % ord ("а")) % 32))
print((ord("ж") + rot) % ord ("а") % 32)