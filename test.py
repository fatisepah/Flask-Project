
file_name = "test.txt"
file_name2 = "test2.min.js"

allowed_extensions = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
def checkfileFormat(fileName):
    print("." in fileName)
    print(fileName.split(".")[-1] in allowed_extensions)
    print(fileName.rsplit(".",1)[1] in allowed_extensions)
    return "." in fileName and fileName.split(".")[-1] in allowed_extensions

print(checkfileFormat("index.dox"))