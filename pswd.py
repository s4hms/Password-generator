import random
import string


def pswd_len():
    while True:
        leng = int(input("Enter the length of the password to be generated: "))

        if leng <= 0:
            print(f"\n!!! {leng} is not a positive integer !!! \n")
        else:
            return leng


def str_req(inp):

    while True:
        dic_str_req = dict()

        nos_uc = int(input("Number of uppercase: "))
        dic_str_req["nos_uc"] = nos_uc
        avl_spa = inp - nos_uc

        if avl_spa == 0:
            pass
        else:
            print(f"\n{avl_spa} places are available")

        if avl_spa == 0:
            dic_str_req["nos_lc"] = 0
        else:
            nos_lc = int(input("Number of lowercase: "))
            dic_str_req["nos_lc"] = nos_lc
            avl_spa = inp - nos_uc - nos_lc

        if avl_spa == 0:
            dic_str_req["nos_numb"] = 0
        else:
            print(f"\n{inp-nos_uc-nos_lc} places are available")
            nos_numb = int(input("Number of numbers: "))
            dic_str_req["nos_numb"] = nos_numb
            avl_spa = inp - nos_uc - nos_lc - nos_numb

        if avl_spa == 0:
            dic_str_req["nos_sc"] = 0
        else:
            print(
                f"\nNumber of special charecters will be {inp-nos_uc-nos_lc-nos_numb}"
            )
            nos_sc = inp - nos_uc - nos_lc - nos_numb
            dic_str_req["nos_sc"] = nos_sc
            avl_spa = inp - nos_uc - nos_lc - nos_numb - nos_sc

        if avl_spa == 0:
            return dic_str_req


def gen_uc(inp):
    ucl = string.ascii_uppercase
    return "".join(random.choices(ucl, k=inp))


def gen_lc(inp):
    lcl = string.ascii_lowercase
    return "".join(random.choices(lcl, k=inp))


def gen_numb(inp):
    numbl = string.digits
    return "".join(random.choices(numbl, k=inp))


def gen_sc(inp):
    sc_str = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    return "".join(random.choices(sc_str, k=inp))


def main():
    sc_str = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    print(f"\nNOTE: Following are allowed special charecters: {sc_str}\n")

    pswd_length = pswd_len()
    req_str = str_req(pswd_length)

    op_gen_uc = gen_uc(req_str["nos_uc"])
    op_gen_lc = gen_lc(req_str["nos_lc"])
    op_gen_numb = gen_numb(req_str["nos_numb"])
    op_gen_sc = gen_sc(req_str["nos_sc"])

    raw_op = op_gen_uc + op_gen_lc + op_gen_numb + op_gen_sc

    op = "".join(random.sample(raw_op, len(raw_op)))

    print(f"\nYour randomly generated password is {op}\n")


main()
