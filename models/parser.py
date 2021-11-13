# Python class for parsing the csv data into Python data structures

class Parser():
        def __init__(self, file_name="expeditionData.csv"):
                self.temp_file = None
                self.file_name = file_name
                # validate file name is valid
                try:
                        self.temp_file = open(self.file_name , 'r')
                        print(f"File - {self.file_name} is a valid file to read from.")
                # if error, let user know
                except OSError as err:
                        print(f"Error: could not open file - {self.file_name }.\n{err}")
                        return
                # if no error, close the file
                finally:
                        self.temp_file.close()
                self.temp_file = None
                # ***** FIELDS *****
                #  assign file name
                self.exped_i = None
                self.astro_i = None
                self.age_i = None
                self.gend_i = None
                self.nat_i = None
                self.dur_i = None
                self.agen_i = None
                self.agen_org_i = None
                self.temp_file = None
        # assigns column/attribute indexes from the csv file
        def assign_indexes(self):
                with open(self.file_name, 'r') as file:
                        first_line_list = file.readline().strip().split(",")
                        for name, index in enumerate(first_line_list):
                                if name == "Expedition":
                                        self.exped_i = index
                                elif name == "Astronaut":
                                        self.astro_i = index
                                elif name == "Age":
                                        self.age_i = index
                                elif name == "Gender":
                                        self.gend_i = index
                                elif name == "Nationality":
                                        self.nat_i = index
                                elif name == "Duration":
                                        self.dur_i = index
                                elif name == "Agency":
                                        self.agen_i = index
                                elif name == "agencyOrigin":
                                        self.agen_org_i = index
                                else:
                                        pass
        # ***** METHODS *****
        def process_file(self):
                with open(self.file_name, 'r') as file:
                        for curr_line in file:
                                # list of values from csv file
                                curr_line_list = curr_line.strip().split(",")
                                print(curr_line_list)