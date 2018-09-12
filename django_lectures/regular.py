import re

patterns = ['term1', 'term2']

text = "This is a string with a term1, not the other"

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern, text):
        print("MATCH!")
    else:
        print("NO MATCH!")

match = re.search('term1', text)
print(match.start())

split_term = '@'
email = 'user@gmail.com'
print(email)
match = re.split(split_term, email)
print(match)

print(re.findall('match', 'test match phrase match in middle'))

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")

# test_phrase = 'sdd..sdsd..sssddd..sdddsddd.dsds...dsss....dsss.sdddddd'
# # test_patterns = ['sd*']
# # test_patterns = ['sd+']
# # test_patterns = ['sd?']
# # test_patterns = ['sd{2,3}']
# test_patterns = ['s[sd]+']
# multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"

test_patterns = ['[!.?]+']
test_patterns = ['[^!.?]+']
test_patterns = ['[a-z]+']
test_patterns = ['[A-Z]+']

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_patterns = [r'\d+'] # search for number/digit
test_patterns = [r'\D+'] # non-digits
test_patterns = [r'\s+'] # whitespace
test_patterns = [r'\S+'] # non-whitespace
test_patterns = [r'\w+'] # alpha numeric
test_patterns = [r'\W+'] # non-alpha numeric
multi_re_find(test_patterns, test_phrase)

