import csv
import re
import os

def counter_prime():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    counter = {}
    pattern = r'\d\d\/\d\d\/(2015) (?:\d\d[\:]{0,1}){3} [PA]M'
    with open(os.path.join(current_dir, "Crimes.csv")) as file:
        reader = csv.reader(file)
        for line in reader:
            if re.match(pattern, line[2]) is not None:
                if line[5] in counter:
                    counter[line[5]] += 1
                else: 
                    counter[line[5]] = 1
    ans = ""
    max_number = 0
    for key in counter:
        if counter[key] > max_number:
            max_number = counter[key]
            ans = key
    print(ans)

if __name__ == "__main__":
    counter_prime()