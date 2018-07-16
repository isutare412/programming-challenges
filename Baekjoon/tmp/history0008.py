CHUNK_SIZE = 10

inputstr = input()

chunks = (
    inputstr[i:i+CHUNK_SIZE]
    for i in range(0, len(inputstr), CHUNK_SIZE)
)
for chunk in chunks:
    print(chunk)
