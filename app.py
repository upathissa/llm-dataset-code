import requests
base_url = "https://tripitaka.online/sutta/live/sutta/"

def save_data_to_file(data, i):
    # Extract 'content' values
    content_list = [item["content"] for item in data["data"]]

    # Define the path to the output text file
    output_file_path = f"textdata/{i}.txt"

    # Write 'content' values to the text file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for content in content_list:
            output_file.write(content + "\n") 

for i in range(7785, 15000):
    # Define the API endpoint URL
    api_url = base_url + str(i)
    
    # Make the GET request
    response = requests.get(api_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Check if there is data property in response
        if 'data' in response.json():
            data = response.json()
            
            save_data_to_file(data, i)
            print(f"i: {i} file_saved")
        else:
            print(f"i: {i} No data property")
            
    else:
        print(f"Request failed with status code {response.status_code}")


# api_url = "https://tripitaka.online/sutta/live/sutta/980"  # Replace with the actual API URL

# Make the GET request
# response = requests.get(api_url)




            
# Check if the request was successful (status code 200)
# if response.status_code == 200:

    # Parse and work with the response data
    # data = response.json()  # Assuming the response is in JSON format
    
    # save_data_to_file(data)
    # if 'data' in data:
        # print(data)
    # else:
        # print('No data property')

#     print(f"Contents saved to ")
# else:
#     print(f"Request failed with status code {response.status_code}")
    
   

