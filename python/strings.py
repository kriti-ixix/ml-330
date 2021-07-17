myString = "Hello world"
myString2 = "How is everyone"

print(myString[2])
print(myString[6])
print(myString[-1]) #Refers to the last index

#myString[start=0 : stop=len (exclusive) : step=1]
print(myString[2:6]) #String slicing

print(len(myString)) #Length of myString
print(myString + myString2) #String concatenation

#Converting Cases
print(myString.lower())
print(myString.upper())

tweet = "Hi everyone #niceweather #nicemood #feelinggood"

#String Splitting
print(myString2.split())
print(tweet.split('#'))
print(tweet.split('#', 1))