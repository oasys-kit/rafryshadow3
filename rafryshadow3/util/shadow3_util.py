
def check_file_name(file_name):
    if file_name is None:
        return init_file_name()
    else:
        return bytes(file_name, "utf-8")

def init_file_name():
    return bytes("NONESPECIFIED", "utf-8")