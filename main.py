# Finding outlier data by iqr based filtering



import pandas as pd

# Find the first and third quartiles and the distance between them 
def clean_data(i):
    new_data = []
    q1 = data[i].quantile(0.25)
    q3 = data[i].quantile(0.75)
    iqr = q3 - q1
    upper_limit = q3 + 1.5 * iqr
    lower_limit = q1 - 1.5 * iqr
    z = 0
    for j in data[i]:
        if j < (lower_limit or j > upper_limit):
            new_data.append(j)
            z += 1
    print("number of outliers :", z)
    return new_data

# Create a new file to save the changes
def creat_address(address):
# Variable for filename 
    word = ""
# Variable for file type

    type = ""
    for i in address:
        word += i
        if i == "\\":
            word = ""
    
    for i in word:
        if i == ".":
            type = ""
        type += i
# Variable for the name of the copied file
    final_word = (word.replace(type, "") + "_edit.csv")
# The address of the space where the copied file will be saved
    address = address.replace(word, final_word)
    return final_word, address


columns = []

while True:
    stats = input("1)start 2)exit!\n")
    if stats == "1":
# Enter the location where the data file is located
        address = input('address your file:\n')
        data_og = pd.read_csv(address)
        copy_info = creat_address(address)
        creat_file = data_og.to_csv(copy_info[0])

        print(data_og.shape)
        while True:
# The columns you want to find outlier data	 
            sample = input("columns name? \n0)done!\n")
            if sample == "0":
                break
            columns.append(sample)
        print(columns)
        while True:
            if len(columns) == 0:
                print("final shape :", data.shape)
                exit()


            data = pd.read_csv(copy_info[1])
            data = pd.DataFrame(data)
            del_list = clean_data(columns[0])

            data = pd.read_csv(copy_info[1], index_col=columns[0])
            data = pd.DataFrame(data)
            data.drop(del_list, inplace=True)
            print(data.shape)
            data.to_csv(copy_info[0])

            del columns[0]

