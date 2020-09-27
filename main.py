from converter import converter

if __name__ == "__main__":
    path = input('Path to file or directory: ')
    c = converter(path)
    c.convert()