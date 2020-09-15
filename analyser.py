import sys
from analyse import CreateDataFrame, HaveEmptyCells, HaveDuplicates

def GetReport(inputfile, outputfile):
    f = CreateDataFrame(inputfile)
    with open(outputfile, 'w') as outputf:
        outputf.write("Empty Cells:"+  HaveEmptyCells(f))
        outputf.write("Duplicates"+ HaveDuplicates(f))
        
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
    elif not filename.endswith(".mps"):
        print("Input file needs to be .mps file")
        sys.exit(1)
    else:
        print("Output file needs to be .txt file")
        sys.exit(1)

if __name__ == '__main__':
   main()