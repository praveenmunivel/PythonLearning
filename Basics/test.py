# list files

import os
import json

folder_path = "C:\\Users\praveen.munivel\Downloads\instagram\connections\\followers_and_following"
# instagram\connections\followers_and_following
files = os.listdir(folder_path)
following_data_list_of_list = []
print(files)
# Loop through each file
for file in files:
    # Only read files ending with .json
    if file.endswith('following.json'):
        file_path = os.path.join(folder_path, file)

        try:
            # Open and read the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                following_data_list_of_list.append(data['relationships_following'])  # Add JSON content to the list
        except json.JSONDecodeError:
            print(f"⚠️ Failed to decode JSON in file: {file}")
        except Exception as e:
            print(f"❌ Error reading file {file}: {e}")
# Output the combined list of JSON data
# for i in range(0, len(following_data_list_of_list)):
#     print(following_data_list_of_list[0])
following_list = []
for following_data in following_data_list_of_list:
    for following in following_data:
        for user in following['string_list_data']:
            following_list.append(user['value'])

followers_data_list_of_list = []
for file in files:
    # Only read files ending with .json
    if file.endswith('followers_1.json'):
        file_path = os.path.join(folder_path, file)

        try:
            # Open and read the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                followers_data_list_of_list.append(data)  # Add JSON content to the list
        except json.JSONDecodeError:
            print(f"⚠️ Failed to decode JSON in file: {file}")
        except Exception as e:
            print(f"❌ Error reading file {file}: {e}")
# Output the combined list of JSON data
# for i in range(0, len(following_data_list_of_list)):
#     print(following_data_list_of_list[0])
followers_list = []
for followers_data in followers_data_list_of_list:
    for followers in followers_data:
        for user in followers['string_list_data']:
            followers_list.append(user['value'])
for i in following_list:
    if i not in followers_list:
        print(i)