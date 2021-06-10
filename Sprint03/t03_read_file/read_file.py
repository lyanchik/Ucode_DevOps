def read_file(filename):
    try:
        open_file = open(filename)    # open the  file
        data = open_file.read()       # reads the file and saves its contents in a variable
        open_file.close()             # closes the file
        print(f'File "{filename}" has the following message:\n{data}')  # prints the file content
    except :
         print(f'Failed to read file "{filename}".')  # no such file in the current directory or no read permissions