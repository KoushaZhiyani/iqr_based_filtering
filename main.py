import pandas as pd


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


def creat_address(address):
    word = ""
    type = ""
    for i in address:
        word += i
        if i == "\\":
            word = ""
    # print(word)
    for i in word:
        if i == ".":
            type = ""
        type += i
    # print(type)
    final_word = (word.replace(type, "") + "_edit.csv")
    address = address.replace(word, final_word)
    return final_word, address


columns = []

while True:
    stats = input("1)start 2)exit!\n")
    if stats == "1":
        address = input('address your file:\n')
        data_og = pd.read_csv(address)
        copy_info = creat_address(address)
        creat_file = data_og.to_csv(copy_info[0])

        print(data_og.shape)
        while True:
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

# a = df.corr()["Selected"]
# print(a.sort_values())
