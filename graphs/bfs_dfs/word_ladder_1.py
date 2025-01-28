from collections import deque
from string import ascii_lowercase

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

def word_sequence_length(begin_word, end_word, word_list):
    # TC: O(n x word len x 26), SC: O(n)
    word_set = set(word_list)
    if end_word not in word_set: return 0
    q = deque()
    q.append((begin_word, 1))

    while q:
        word, steps = q.popleft()
        if word == end_word: return steps

        for i in range(len(word)):
            for c in ascii_lowercase:
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    q.append((new_word, steps + 1))
                    word_set.remove(new_word)
    return 0
print(word_sequence_length(begin_word, end_word, word_list))

