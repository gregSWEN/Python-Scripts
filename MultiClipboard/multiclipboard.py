import sys 
import clipboard 
import json 

#Function creates json file with dictionary data from script

SAVED_FILE = "test.json"

def save_items(path, data):
    #Write the data to the json file, allowing more than one item on the clipboard 
    with open(path, 'w') as f:
        json.dump(data, f) 


def load_json(path):
    try:
        with open(path, 'r') as f:
            #loads the data into the json file
            data = json.load(f)
            return data 
    except:
        return{}


def print_keys(data):
    for key in data:
        print("Key: ", key, " Data: ", data[key])


def main():

        arg = sys.argv

        if len(arg) == 2:
            command = sys.argv[1].lower()
            data = load_json(SAVED_FILE)
            if command == 'save':
                key = input("Enter a key to be associated with the current clipboard: ")
                data[key] = clipboard.paste()
                save_items(SAVED_FILE, data)

            elif command == 'load':
                print("Enter a key to be loaded into clipboard\nPossible Keys:")
                print_keys(data)
                key = input(">>> ")
                if key in data:
                    clipboard.copy(data[key]) 
                    print("Data was copied to the clipbaord: ", clipboard.paste())
                else:
                    print("Key does not exist")
            elif command == 'list':
                print_keys(data)
            elif command == 'delete':
                print("Please select key to delete")
                print_keys(data)
            else:
                print("Error, command not recognized.")
        else:
            print("Please enter exactly one command.")

if __name__ == '__main__':
    main()