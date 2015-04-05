def main(biglist, littlelist):
    messylist = biglist
    for hop in range(0, len(littlelist)-1):
        match = False
        for jump in range(0, len(messylist)-1):
            if messylist[jump] == littlelist[hop]:
                if match == False:
                    messylist.pop(jump)
                match = True
        if match == False:
            biglist.append(littlelist[hop])
return biglist