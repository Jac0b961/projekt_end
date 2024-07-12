# project.py
import sys
import json

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Loaded data: {data}")
        return data
    except json.JSONDecodeError:
        print("Invalid JSON format")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    if input_file.endswith('.json'):
        data = load_json(input_file)
    else:
        print("Unsupported file format")
        sys.exit(1)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
