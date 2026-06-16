from ablist.argument import *

args = parser.parse_args()

# Ill use an array temporary as a outoutput for the generated wordlist
output = ["Avneesh101", "Kumar2024", "AblistIsAwesome", "PythonRocks", "WordlistGenerator", "CustomWordlist", "BruteforceTool", "Cybersecurity", "EthicalHacking", "PenTesting"]



class FileHandler:
    def __init__(self, FileName=None):
        self.File_Name = FileName or "output.txt"

    def save_as_txt(self):
        with open(self.File_Name, 'w') as file:
            for word in output:
                file.write(word + '\n')

