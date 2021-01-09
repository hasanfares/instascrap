import os


def txt_to_labels(la):
    desc = {}
    if len(la) == 4:
        desc["title"] = la[0] + " " + la[1]
        desc["sizes"] = la[2]
        desc["price"] = la[3]
    elif len(la) == 3:
        desc["title"] = la[0]
        desc["sizes"] = la[1]
        desc["price"] = la[2]
    else:
        print("File {} in {}\n has more or less words than expected".format(obj, item))
        print("Here take a look: \n")
        print(la)
        print("please provide the details yourself here: \n")
        desc["title"] = input("Title(description): ")
        desc["sizes"] = input("Sizes: ")
        desc["price"] = input("Price: ")

    return desc


def get_confirmation():
    confirmation = input("Type 'y' or 'n': ").lower()
    if confirmation == "y":
        return True
    elif confirmation == "n":
        return False
    else:
        print("You typed '{}' which is not 'y' or 'n'.".format(confirmation))
        print("Please type 'y' or 'n' only.")
        get_confirmation()


def labels_to_dic(a):
    details = None
    for word in a:
        if word.lower() == "one" or word.lower() == "xl" or word.lower() == "s" or word.lower() == "m" or \
                word.lower() == "l" or word.lower() == "size" or "bag" in word:
            print("File {} in {} \nhas one or more sizes spread by spaces in it.".format(obj, item))
            print("Or it can have a 'bag' in it.")
            print("Or the word 'one' is in it separated by spaces.")
            print("Or the word 'size' is in it separated by spaces.")
            print("This can be a size instead of description or a price.")
            print("You can choose to continue if you think that is appropriate.")
            print("Here take a look: \n")
            print(info)
            print("\n")
            print("Type 'y' to continue or 'n' to enter the details yourself.")
            answer = get_confirmation()
            if answer:
                details = txt_to_labels(a)
                return details
            elif not answer:
                print("Please provide the details yourself here: \n")
                ab = []
                title = input("Title(description): ")
                ab.append(title)
                sizes = input("Sizes: ")
                ab.append(sizes)
                price = input("Price: ")
                ab.append(price)
                details = labels_to_dic(ab)
                return details

    if not a[0][0].isdigit() and a[0].lower() != "one" and "." not in a[0]:
        details = txt_to_labels(a)

    elif a[0][0].isdigit():
        print("File {} in {}\n starts with a number.".format(obj, item))
        print("this can be a size or a price instead of description.")
        print("You can choose to continue if you think that is appropriate.")
        print("Here take a look: \n")
        print(a)
        print("\n")
        print("Type 'y' to continue or 'n' to enter the details yourself.")
        answer = get_confirmation()
        if answer:
            details = txt_to_labels(a)
        elif not answer:
            print("Please provide the details yourself here: \n")
            a = []
            title = input("Title(description): ")
            a.append(title)
            sizes = input("Sizes: ")
            a.append(sizes)
            price = input("Price: ")
            a.append(price)
            details = labels_to_dic(a)

    elif a[0].lower() == "one":
        print("File {} in {}\n starts with the word 'one'".format(obj, item))
        print("this can be a size or a price instead of description")
        print("You can choose to continue if you think that is appropriate.")
        print("Here take a look: \n")
        print(a)
        print("\n")
        print("Type 'y' to continue or 'n' to enter the details yourself.")
        answer = get_confirmation()
        if answer:
            details = txt_to_labels(a)

        elif not answer:
            print("Please provide the details yourself here: \n")
            a = []
            title = input("Title(description): ")
            a.append(title)
            sizes = input("Sizes: ")
            a.append(sizes)
            price = input("Price: ")
            a.append(price)
            details = labels_to_dic(a)

    elif "." in a[0]:
        print("File {} in {}\n starts with a word that has a '.' in it".format(obj, item))
        print("this can be a size or a price instead of description")
        print("You can choose to continue if you think that is appropriate.")
        print("Here take a look: \n")
        print(a)
        print("\n")
        print("Type 'y' to continue or 'n' to enter the details yourself.")
        answer = get_confirmation()
        if answer:
            details = txt_to_labels(a)
        elif not answer:
            print("Please provide the details yourself here: \n")
            a = []
            title = input("Title(description): ")
            a.append(title)
            sizes = input("Sizes: ")
            a.append(sizes)
            price = input("Price: ")
            a.append(price)
            details = labels_to_dic(a)

    return details


if __name__ == "__main__":

    dire = "f.a.online"
    print("parsing {}".format(dire))
    if os.path.exists(dire):
        main = os.listdir(dire)
        print("Folder contains the following: \n{}".format(main))
        if not main:
            raise Exception("{} is empty".format(dire))
        for item in main:
            full_path = os.path.join(os.getcwd(), dire, item)
            if os.path.isdir(full_path):
                folder = os.listdir(full_path)
                print("folder number: {}".format(item))
                if not folder:
                    raise Exception("Folder {} is empty".format(item))
                txt_files = []
                for obj in folder:
                    full_path_obj = os.path.join(full_path, obj)

                    descriptions = []
                    if os.path.isfile(full_path_obj):
                        file = full_path_obj
                        if file.endswith(".txt"):
                            txt_files.append(file)
                            with open(file, encoding="UTF-8") as f:
                                info = f.readlines()
                                if len(info) == 1:
                                    for line in info:
                                        labels = line.split()
                                        description = labels_to_dic(labels)
                                        print(description)
                                elif len(info) != 1:
                                    print("File {} in {}\n has more than 1 line".format(obj, item))
                                    print("You can choose to continue if you think that is appropriate.")
                                    print("Here take a look: \n")
                                    print(info)
                                    print("\n")
                                    print("Type 'y' to continue or 'n' to enter the details yourself.")
                                    response = get_confirmation()
                                    if response:
                                        desc_set = []
                                        for line in info:
                                            labels = line.split()
                                            description = labels_to_dic(labels)
                                            desc_set.append(description)
                                            print(description)
                                            print(desc_set)
                                    elif not response:
                                        descriptions = []
                                        print("please provide the details yourself here: \n")
                                        descr = input("Title(description): ")
                                        descriptions.append(descr)
                                        size = input("Sizes: ")
                                        descriptions.append(size)
                                        prices = input("Price: ")
                                        descriptions.append(prices)
                                        lab = labels_to_dic(descriptions)
                                        print(lab)

                if len(txt_files) == 0:
                    print("folder {}\n has no text file".format(item))
                    print("please provide the details yourself here: \n")
                    descriptions = []
                    descre = input("Title(description): ")
                    descriptions.append(descre)
                    siz = input("Sizes: ")
                    descriptions.append(siz)
                    pric = input("Price: ")
                    descriptions.append(pric)
                    lab = labels_to_dic(descriptions)
                    print(lab)

    elif not os.path.exists(dire):
        raise FileNotFoundError("{} does not exist".format(dire))
