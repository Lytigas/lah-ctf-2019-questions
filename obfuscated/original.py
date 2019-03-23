# Puzzle prompt:
# The following python program responds to a specific 4-character base64 input
# If you wish, you may use the table at https://en.wikipedia.org/wiki/Base64#Base64_table

KEY="5rL/"

# FLAG="HeR3I5AFLaG4hhh74ke1tPl3as3"
DATA="yW3GqP45)V#GP[XUVZ]WD51VQN_"
MASK="12at8euse7ds830bb18f0e]e0=l"

C=input("?")
if C==KEY: print(''.join(chr(ord(a) ^ ord(b)) for a,b in zip(DATA,MASK)))
