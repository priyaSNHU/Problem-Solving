# Hacker rank problem link: https://www.hackerrank.com/challenges/contacts/problem

class trie:
    def __init__(self):
        self.trie = dict()
    def add_contact(word):
        curr = trie
        for i in word:
            if i not in curr:
                curr[i] = dict()
                curr[i]['count'] = 1
            else:
                curr[i]['count'] += 1
            curr = curr[i]
        curr[None] = None
    def find_partial(word):
    curr = trie
    for i in word:
        if i not in curr:
            return 0
        curr = curr[i]
    return curr['count']

trie = trie()  
N = int(input())
for n in range(N):
    query = input().strip().split(' ')
    if query[0] == 'add':
        trie.add_contact(query[1])
    else:
        print(trie.find_partial(query[1]))
