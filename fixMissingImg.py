import os
# <img src="images/temp_2019.png" alt="drawing" width="600"/>
# <img src="https://raw.githubusercontent.com/MLcmore2023/MLcmore2023/main/Section 2 - 3 Exercise/images/temp_2019.png" alt="drawing" width="600"/>

before = r'<img src=\"'
after  = r'<img src=\"https://raw.githubusercontent.com/MLcmore2023/MLcmore2023/main/'

def replace_in_file(file_path,root):
    with open(file_path, 'r') as file:
        content = file.read()
        if before not in content:
            return 
        updated_content = content.replace(before, after+root[2:]+"/")
    with open(file_path, 'w') as file:
        file.write(updated_content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path,root)
                # print(root, "\n\t",file)

# Replace the current directory with your desired directory path
directory_path = './'

process_directory(directory_path)
