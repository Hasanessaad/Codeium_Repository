def read_file(filename, file_type):
    if file_type == "txt":
        with open(filename, "r") as file:
            return file.read()
    elif file_type == "json":
        import json
        with open(filename, "r") as file:
            return json.load(file)
    elif file_type == "csv":
        import csv
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
    else:
        raise ValueError("Invalid file type")

def write_file(filename, data, file_type):
    if file_type == "txt":
        with open(filename, "w") as file:
            file.write(data)
    elif file_type == "json":
        import json
        with open(filename, "w") as file:
            json.dump(data, file)
    elif file_type == "csv":
        import csv
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        raise ValueError("Invalid file type")
