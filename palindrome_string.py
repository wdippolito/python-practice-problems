import re

s = "reverse this string by spaces"
s2 = s.split()
print(s2)
s3 = ""

s2 = s2[::-1]
s3 = ' '.join(s2)
print(s3)

index  = s3.find("this")
print(index)

removed = s3[0:index] + s3[index+len("this")+1:]

print(removed)

s4 = "there is a url in this string https://hello.org"

# regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# url = regex.search(s4)
print(s4)



