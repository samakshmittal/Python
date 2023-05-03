try:
    pass
except FileNotFoundError:
    print("File is not found")
except IOError:
    print("Input/Output error whie reading or writing the file")
except PermissionError:
    print("Access not granted")
except IsADirectoryError:
    print("Specify a file instead of a directory")
except NotADirectoryError:
    print("Specify a directory instead of a file")
except ValueError:
    print("Invalid argument passed")
except UnicodeDecodeError:
    print("Error in decoding the file due to invalid character encoding")
except FileExistsError:
    print("File with same name already exists")
except EOFError:
    print("End of File is reached unexpectedly while reading")
except OSError:
    print("Operating system error")
