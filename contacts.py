# Hacker rank problem link: https://www.hackerrank.com/challenges/contacts/problem

trie = dict()
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
    
N = int(input())
for n in range(N):
    query = input().strip().split(' ')
    if query[0] == 'add':
        add_contact(query[1])
    else:
        print(find_partial(query[1]))
