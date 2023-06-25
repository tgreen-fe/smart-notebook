import glob
import os.path
import os
import openai
import re
import json
from pathlib import Path

openai.api_key = "YOUR_OPENAI_API_KEY"

folder_path = r'C:\Users\tbbgr\iCloudDrive\Home Projects\smartNotebook\notebookExtracts'
file_type = r'\*.txt'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
fileName = Path(max_file).stem


def summaryGenerate(max_file):
    f = open(max_file, "r", encoding="utf8")
    scanContent = f.read()

    try:
        messages1 = [ {"role": "system", "content": 
                    "You are a intelligent assistant."} ]

        message1 = "Correct all spelling mistakes in this passage: \n" + "\"" + scanContent + "\""

        messages1.append({"role": "user", "content": message1})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages1)

        reply1 = chat.choices[0].message.content

    except:

        reply1 = "Failed"


    try:
        messages2 = [ {"role": "system", "content": 
                    "You are a intelligent assistant that only outputs six word titles and nothing else."} ]

        message2 =  "Give a six word title of this passage \n" + "\"" + reply1 + "\""

        messages2.append({"role": "user", "content": message2})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages2)

        reply2 = chat.choices[0].message.content

    except:
        
        reply2 = "Failed"


    try:
            
        messages3 = [ {"role": "system", "content": 
                    "You are a intelligent assistant."} ]

        message3 =  "Give a summary of this bassage in no more than 40 words: \n" + "\"" + reply1 + "\""

        messages3.append({"role": "user", "content": message3})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages3)

        reply3 = chat.choices[0].message.content

    except:

        reply3 = "Failed"



    try:
        messages4 = [ {"role": "system", "content": 
                    "You are a intelligent assistant that only outputs dates in the format 'xx/xx/xxxx', if no date is available output '01/01/1999"} ]

        message4 =  "Extract the date from this passage \n" + "\"" + reply1 + "\"\n. If no date is available then return only '01/01/1999' and do not output any other text."

        messages4.append({"role": "user", "content": message4})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages4)

        reply4 = chat.choices[0].message.content

    except:

        reply4 = "Failed"

    #Extracting just the title
    try:
        title = re.findall(r'\b\d+\b',reply2)[-1]
    except:
        title = reply2

    #Finding page number
    try:
        pageNumber = re.findall(r'\b\d+\b',reply1)[-1]
    except:
        pageNumber = "NA"

    #Extracting date in standard format
    try:
        writeDate = re.findall(r'"([^"]*)"', reply4)[0]
    except:
        writeDate = "01/01/1999"

    #Conversion to json format
    dataUpload = [
                {
                "fileName" : fileName,
                "title" : title,
                "summary" : reply3,
                "date" : writeDate,
                "pageNum" : pageNumber
                }
            ]   
    
    return dataUpload


if os.path.getsize("C:/pico/webHost/testUpload.json") >0:

    with open("C:/pico/webHost/testUpload.json") as f:
        
        oldData = json.load(f)

        for i in range(len(oldData)):
            if fileName != oldData[-1]["fileName"]:

                dataUpload = summaryGenerate(max_file)

                dataUpload = oldData + dataUpload
                
                with open("C:/pico/webHost/testUpload.json", 'w') as outfile:
                    
                    json.dump(dataUpload, outfile, indent = 4)

                

else:
    
    with open("C:/pico/webHost/testUpload.json", 'w') as outfile:
        
        dataUpload = summaryGenerate(max_file)

        outfile.write(json.dumps(dataUpload, indent = 4))







# dataUpload = oldData + dataUpload
# with open("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json", 'w') as outfile:



# json.dump(dataUpload, outfile, indent = 4)

    

#jsonObject = json.dumps(dataUpload, indent=4)


#Writing output file
# fOutput = open("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json", "w")
# fOutput.write(jsonObject)
# fOutput.close()

# if os.path.getsize("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json") >0:

#     with open("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json") as f:
        
#         oldData = json.load(f)

#         for i in range(len(oldData)):
#             if fileName != oldData[-1]["fileName"]:

#                 dataUpload = oldData + dataUpload

#                 with open("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json", 'w') as outfile:
                    
#                     json.dump(dataUpload, outfile, indent = 4)

# else:
    
#     with open("C:/Users/tbbgr/iCloudDrive/Home Projects/smartNotebook/webHost/testUpload.json", 'w') as outfile:
        
#         outfile.write(json.dumps(dataUpload, indent = 4))

