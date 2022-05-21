def words_count(text):
    count = len(text.split())
    return count

string = str(input())
print(words_count(string))