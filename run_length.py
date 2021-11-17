
def encoder(array):
    #array = "7750027"
    encoded_array = ""
    i = 0
    while i <= len(array)- 1:
        count = 1
        char = array[i]
        j = i
        while j < len(array)-1:
            if array[j] == array[j+1]:
                count += 1
                j += 1
            else:
                break
        encoded_array = encoded_array + str(count) + char
        i = j+1
    return encoded_array


value = input("Enter an array: ")
result = encoder(value)
print(result)
