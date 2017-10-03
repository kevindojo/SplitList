#find and replace

words = "It's Thanksgiving day. It's my birthday, too!"
words.find("day")
print words.find("day")
print words.replace("day","month")

# min and max

x = ["hello", 2, 54, -2, 7, 12, 98]
print min([2, 54, -2, 7, 12, 98])
print max([2, 54, -2, 7, 12, 98])

#first and last

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[len(x)-1]
y = []
y.append(x[0])
y.append(x[len(x)-1])
print y

#new list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()          # > [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
y = x[:len(x)/2]    # : means "start of index" x[0]-len(x)/2 => values between x[0] to len(x)/2
x1 = x[len(x)/2:]   # : at the end means; collect values from the split till the end value.
x1.insert(0,y)
print x1

