import sys
from analyse import createdataframe, haveemptycells, haveduplicates, getshape, getindex, count_empty, count_duplicates
from analyse import getcolnames, getcoltypes, percent_missing

def GetReport(inputfile, outputfile):
    f = createdataframe(inputfile)
    with open(outputfile, 'w') as outputf:
        outputf.write("Column Names: "+ str(getcolnames(f)))
        outputf.write("\nColumn Data Types: "+ str(getcoltypes(f)))
        outputf.write("\nEmpty Cells: " +  haveemptycells(f))
        outputf.write("\nPercentage of missing values Per column: "+ str(percent_missing(f)))
        outputf.write("\nDuplicates: "+ haveduplicates(f))
        outputf.write("\nShape: "+ str(getshape(f)))
        outputf.write("\nIndex: "+ str(getindex(f)))
        outputf.write("\nNumber of empty values: "+str(count_empty(f)))
        outputf.write("\nNumber of duplicates: " +  str(count_duplicates(f)))

        
def main():
    if len(sys.argv) < 3:
        print("The arguments should be the script name , a .csv file as an input file and a .txt file as an output file")
        sys.exit(1)
    else:
        script = sys.argv[0]
        filename = sys.argv[1]
        outputfile = sys.argv[2]
    if filename.endswith(".csv") and outputfile.endswith(".txt"):
        GetReport(filename, outputfile)
    elif not filename.endswith(".csv"):
        print("Input file needs to be .csv file")
        sys.exit(1)
    else:
        print("Output file needs to be .txt file")
        sys.exit(1)

if __name__ == '__main__':
   main()