import os

full_name = []
rp = "."


def list_files(rp):
    if not os.path.isdir(rp):  # root path
        return None

    loc_files = os.listdir(rp)
    for name in loc_files:
        complete_f = rp + "/" + name
        full_name.append(complete_f)
        if os.path.isdir(complete_f):
            list_files(complete_f)
            # print("-" * 20, complete_f)
    return full_name


if __name__ == "__main__":
    liste = list_files("/home/apch/Documents")
    for x in liste:
        print(x)

    print(len(liste))
