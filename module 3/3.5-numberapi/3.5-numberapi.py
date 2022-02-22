import requests
import os

def main():

    inp_data = []
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_dir, 'input.txt'), "r") as inp:
        for number in inp:
            inp_data.append(int(number))

    with open(os.path.join(current_dir, 'output.txt'), "w") as outp:
        for number in inp_data:
            api_url = f"http://numbersapi.com/{number}/math?json=true"
            res = requests.get(api_url)
            if res.json()["found"]:
                outp.write("Interesting\n")
            else:
                outp.write("Boring\n")

if __name__ == "__main__":
    main()