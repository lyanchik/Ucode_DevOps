import re


def write_file(filename, message='None'):
    filename = str(filename)
    reg = r'^\w+.txt$'
    if re.findall(reg, filename):
        try:
            with open(filename, "w") as w_file:  # opens it for writing
                w_file.write(message)  # writes the given message
            with open(filename, "r") as r_file:  # opens the file again to check if it is not empty
                data = r_file.read()
                if data != message or data == "":  # if  file is empty or its contents are not equal to message
                    return print('Something went wrong...')
                else:
                    return print(f'Your message has been written to file "{filename}".\n'
                                 f'File "{filename}" now contains the following text:\n{data}')
        except:
            return
    else:
        print(f'Please enter the filename in the format "filename.txt".\n'
              f'Failed to write to file "{filename}".')
