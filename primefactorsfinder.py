import primechecker
import factorizer
def main(num):
    factorslist = factorizer.factorizer(num)
    factorizationcomplete = False
    while factorizationcomplete == False:
        for hop in range(0, len(factorslist)-1):
            if primechecker.primechecker(factorslist) == False
                factorizer