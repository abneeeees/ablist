from ablist.argument import *
from ablist.file import *

args = parser.parse_args()

def filehandling():
    args = parser.parse_args()
    if len(args.output) == 1:
        args.output.append("output.txt")

    if(len(args.output) > 2):
        print("Invalid number of arguments for output option.")
        return
    
    if(len(args.output) == 0):
        print("No output option provided. Defaulting to terminal output.")
        args.output = ['D', None]

    if(args.output[0] not in ['B', 'D', 'T']):
        print("Invalid output type. Please choose 'B', 'D', or 'T'.")
        return
    
    if(args.output[0] in ['B', 'T'] and args.output[1] is None):
        print("Please provide a filename for the output.")
        return
    
    if(args.output[0] == 'D' and args.output[1] is not None):
        print("Filename is not required for terminal output. Ignoring the filename.")
        args.output[1] = None

    mode = args.output[0]
    filename = args.output[1]

    obj = FileHandler(filename)
    if(mode == 'T'):
        obj.save_as_txt()
    elif (mode == 'D'):
        for word in output:
            print(word)
    elif (mode  == 'B'):
        obj.save_as_txt()
        for word in output:
            print(word)
    else:
        print("Invalid output type. Please choose 'T', 'D', or 'B'.")

def main():
    filehandling()


if __name__ == "__main__":
    main()
