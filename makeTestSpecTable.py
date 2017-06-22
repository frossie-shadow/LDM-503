#!/bin/env python
# Take list file with and make a tex table
from __future__ import print_function


def processFile(fin, tout):
    "Read the tree file and ocntrcut a tree structure"
    count = 0
    for line in fin:
        if line.startswith(",,,,") or line.startswith("Component"):
                continue
        count = count + 1
        line = line.replace("\"", "")
        line = line.rstrip('\r\n')
        line = line.replace("???", "TBD")
        part = line.split(",")  # comp,req.des.tesspec.ad,on.user,tut.Rcolo

        if (part[7] != ""):
            print(r"\rowcolor{{{}}}".format(part[7]), file=tout)
        print(r"{p[0]} & {p[3]} \\ \hline".format(p=part), file=tout)

    print("{} test spec lines".format(count))
    return


def fixTex(text):
    ret = text.replace("_", "\\_")
    ret = ret.replace("/", "/ ")
    return ret


def doFile(inFile):
    """This processes a csv and produces a  tex longtable."""
    f = inFile
    nt = "TopLevelTestSpecs.tex"
    print("Processing {} --> (table){}".format(f, nt))
    fin = open(f, 'r')

    tout = open(nt, 'w')

    theader(tout)

    processFile(fin, tout)

    tfooter(tout)
    tout.close()
    fin.close()

    return
# End DoFile


def theader(tout):
    print("""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Test Spec table generated by {} do not modify.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""".format(__file__), file=tout)
    print(r"""\begin{longtable}{|p{0.4\textwidth}|p{0.2\textwidth}|}\hline
\textbf{Component} & \textbf{Testing Spec}\\ \hline""", file=tout)
    return


def tfooter(tout):
    print(r"\end{longtable}", file=tout)
    return


# MAIN
doFile("TopLevelTestSpecs.csv")
