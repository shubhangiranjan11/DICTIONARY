


file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
  
# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("SAPNA \n")
file1.close()
  
# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()
  
# # Write-Overwrites
# file1 = open("myfile.txt", "w")  # write mode
# file1.write("SapnaDeshmukh\n")
# file1.close()
  

