class FileHandler:
    def __init__(self, FileName=None, final_word_list: list = []):
        self.File_Name = FileName or "output.txt"
        self.final_word_list = final_word_list

    def save_as_txt(self):
        with open(self.File_Name, "w") as file:
            for word in self.final_word_list:
                file.write(word + "\n")
