from string import ascii_lowercase
from collections import deque

begin_word = "bat"
end_word = "coz"
word_list = ["pat", "bot", "pot", "poz", "coz"]

def word_sequences(begin_word, end_word, word_list):
    word_set = set(word_list)
    q = deque()
    q.append([begin_word])
    used_on_level = set()
    level = 0
    ans = []
    while q:
        seq = q.popleft()
        if len(seq) > level:
            level += 1
            word_set -= used_on_level
            used_on_level.clear()

        word = seq[-1]
        if word == end_word:
            if len(ans) == 0:
                ans.append(seq)
            elif len(ans[-1]) == len(seq):
                ans.append(seq)

        for i in range(len(word)):
            for c in ascii_lowercase:
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    new_seq = seq + [new_word]
                    used_on_level.add(new_word)
                    q.append(new_seq)
    return ans
print(word_sequences(begin_word, end_word, word_list))

