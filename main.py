file_read = open('Codingal.txt', 'r')
print("file in read mode...")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode-")
file_write.write("Hi! i am a penguin i am 10 yrs old")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in append mode...")
file_append.write("Hi! i am a penguin i am 10 yrs old")
file_append.close()
