import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
start_dir = os.path.join(current_dir, 'main')
ans = []
for dir, dirs, files in os.walk(start_dir):
    for file in files:
        if ".py" in file:
            ans.append(dir.replace(current_dir + "\\", ''))
            break
ans.sort()

with open(os.path.join(current_dir, 'ans.txt'), "w") as output_file:
    for dir in ans:
        output_file.write(dir)
        output_file.write("\n")    
