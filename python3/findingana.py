from sys import stdin, stdout
word = stdin.readline()
stdout.write(word[word.find('a'):])
# for i,c in enumerate(word):
#     if c == 'a':
#         stdout.write(word[i:])
#         exit()