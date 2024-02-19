class Read_Rile():
    """Try to read the given file."""

    def __init__(self,file_name):
        self.file_name = file_name
        
    def read_file(self) -> str:
        """Try to read file ot throw file not found exception """
        file_data = ""
        try:
            f = open(f"SBP-levels/{self.file_name}")
            file_data = f.read()
            f.close()
        except IOError:
             print("File path not found")
             exit(1)
             
        return file_data
