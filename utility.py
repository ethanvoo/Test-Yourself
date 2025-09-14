import json

def get_choice(choice, mode, write_data=None) -> dict:
    if mode == "r":
        if choice == "Music":
            with open("music.json", "r") as f:
                return json.load(f)
        elif choice == "Computer Science":
            with open("computer_science.json", "r") as f:
                return json.load(f)
        elif choice == "Chemistry":
            with open("chemistry.json", "r") as f:
                return json.load(f)
        return {"error": "Invalid subject"}
    elif mode == "w":
        if write_data is None:
            return {"error": "No data to write"}
        if choice == "Music":
            with open("music.json", "w") as f:
                json.dump(write_data, f, indent=4)
                return write_data
        elif choice == "Computer Science":
            with open("computer_science.json", "w") as f:
                json.dump(write_data, f, indent=4)
                return write_data
        elif choice == "Chemistry": 
            with open("chemistry.json", "w") as f:
                json.dump(write_data, f, indent=4)
                return write_data
    return {"error": "Unknown error"}

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb