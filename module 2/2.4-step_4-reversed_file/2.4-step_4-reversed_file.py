import os

def reversed_file():
    current_dir = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(current_dir, 'first file.txt'), "r") as input_file, open(os.path.join(current_dir, 'reversed file.txt'), "w") as output_file:
        input_file = input_file.read().split()
        for i in range(len(input_file) - 1, -1, -1):
            output_file.write(input_file[i])
            output_file.write('\n')
    

if __name__ == "__main__":
    reversed_file()