#Advanced concepts - strings

message = 'Mmakaphema_2025'

print(message[0])
print(message[1])

print(message[-1])

print(len(message))


method = ' Phema, 2025! '

print(method.strip()) #Remove leading trailing whitespaces
print(method.lower()) #Lower cases

method2 = ' Phema 2025 '
print(method2.split(',')) #Splits the string into 2 lists based on the comma

print(method2.upper()) #UPPER CASES
print(method2.replace('Phema', 'Walo'))

