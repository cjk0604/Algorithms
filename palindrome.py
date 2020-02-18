def palindrome(data):
    if len(data) <= 1:
        return True

    if data[0] == data[-1]:
        return palindrome(data[1:-1])
    else:
        return False

data = 'level'
data2 = 'apple'

print(palindrome(data))
print(palindrome(data2))
