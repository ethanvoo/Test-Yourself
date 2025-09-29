import json, os

def get_choice(choice, mode, write_data=None) -> dict:
    if mode == "r":
        try:
            with open(f"./subjects/{choice}.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"error": "Invalid subject"}
    elif mode == "w":
        if write_data is None:
            return {"error": "No data to write"}
        
        try:
            with open(f"./subjects/{choice}.json", "w") as f:
                json.dump(write_data, f, indent=4)
            return {}
        
        except FileNotFoundError:
            return {"error": f"File ({choice}.json) Not Found"}

    return {"error": "Unknown error"}

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def remove_punctuation(words) -> list[str] | str:
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''

    if type(words) is list:
        no_punct = []
        for word in words:
            no_punct.append(''.join(char for char in word if char not in punctuation))

        return no_punct
    elif type(words) is str:
        return ''.join(char for char in words if char not in punctuation)
    else:
        return "Error"

def get_subjects() -> list[str]:
    filenames: list[str] = os.listdir("./subjects")
    subjects: list[str] = [filenam.strip(".json") for filenam in filenames if filenam.endswith(".json")]

    return subjects

def add_subject(name) -> None:
    with open(f"./subjects/{name}.json", "w") as f:
        f.write("{}")
