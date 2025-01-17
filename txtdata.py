# import statements
from copy import deepcopy
from helper import get_data


class TxtData:
    """
    Represents an object of the class TxtData:
    Attributes:
        data (list): a nested list of integers
        rows (int): an integer (number of rows in data)
        cols (int): an integer (number of columns in data)
    """
        
    def __init__(self, my_data):
        """
        The constructor of the class TxtData:
        Parameters:
            my_data (list: a nested list of integers
        Returns:
            None, creates an object
            
        Examples:
            >>> my_list_simple = [[2,3, 9],[7,5,8]]
            >>> my_txt = TxtData(my_list_simple)
            >>> my_txt.rows
            2
            >>> my_txt.cols
            3
        
            >>> my_list_simple = [[84,3, 9],[7,42,8]]
            >>> my_txt = TxtData(my_list_simple)
            >>> my_txt.data
            [[84, 3, 9], [7, 42, 8]]
            
            >>> my_list = get_data("small_data.txt")
            >>> my_txt = TxtData(my_list)
            >>> my_txt.cols
            10
            >>> my_txt.rows
            10
        """
        
        # Create a deep copy of the data
        self.data = deepcopy(my_data)
        
        # Compute the number of rows and columns of data
        self.rows = len(self.data)
        self.cols = len(self.data[0])
 
 
    def __str__(self):
        """
        Creates a str method that returns a string
        Arguments:
            None
        Returns:
            (str): The computed string
            
        Examples:
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_txt = TxtData(my_list)
        >>> print(my_txt)
        This TxtData object has 2 rows and 3 columns.
        
        >>> my_list = [ [1, 2], [4, 5] ]
        >>> my_txt = TxtData(my_list)
        >>> print(my_txt)
        This TxtData object has 2 rows and 2 columns.
        
        >>> my_list = [ [729, 93, 837392], [41, 53, 392729], \
        [837229, 291719, 927191] ]
        >>> my_txt = TxtData(my_list)
        >>> print(my_txt)
        This TxtData object has 3 rows and 3 columns.
        """
        
        return "This TxtData object has "+ str(self.rows)+ " rows and "+ \
               str(self.cols)+ " columns."
    
    
    def get_pixels(self):
        """
        Returns an integer: the total number of pixels in data
        Arguments:
            None
        Returns:
            self.pixels (int): The computed number of pixels
            
        Examples:
            >>> my_list_simple = [[84,3, 9],[7,42,8]]
            >>> my_txt = TxtData(my_list_simple)
            >>> my_txt.get_pixels()
            6
            
            >>> my_list_simple = [[1,2],[4,6]]
            >>> my_txt = TxtData(my_list_simple)
            >>> my_txt.get_pixels()
            4
            
            >>> my_list_simple = [[84,3, 9],[7,42,8], [874, 928, 39]]
            >>> my_txt = TxtData(my_list_simple)
            >>> my_txt.get_pixels()
            9            
        """
        
        # The number of pixels is the number of rows x the number of columns
        self.pixels = self.rows * self.cols
        return self.pixels
    
    
    def get_data_at(self, row, col):
        """
        Returns the value in data at a given position (determined by \
        the arguments row and col)
        Arguments:
            row (int) = the row of the value
            col (int) = the column of the value
        Returns:
            value (int): the value in data at the given position
            
        Examples:
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_txt = TxtData(my_list)
        >>> my_txt.get_data_at(1, 2)
        6
        
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_txt = TxtData(my_list)
        >>> my_txt.get_data_at(1, 1)
        5
        
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_txt = TxtData(my_list)
        >>> my_txt.get_data_at(2, 2)
        Traceback (most recent call last):
        ValueError: Index out of bound!        
        """
        
        # Raise a value Error if there is no value at the given indices
        if row >= len(self.data) or col >= len(self.data[row]):
            raise ValueError ("Index out of bound!")
        
        # Find the value at the given row and column
        value = self.data[row][col]
        
        return value
    
    
    def pretty_save(self, file_name):
        """
        Converts the data into a prettier form to create a qr code
        Arguments:
            file_name (str): A string, the file that will be modified
        Returns:
            None
        
        Examples:
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_pretty.txt")
        
        >>> my_data = get_data("qrcode_binary_error.txt")
        Traceback (most recent call last):
        ValueError: File should contain only 0s and 1s!
        
        >>> my_list = get_data("small_data.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_new.txt") 

        """
        
        # Enter each value of the nested list
        for row in range(len(self.data)):
            for i in range(len(self.data[row])):
                
                # Transform each character (two spaces or 2 blocks)
                if self.data[row][i] == 1:
                    self.data[row][i] = "\u2588" * 2
                else:
                    self.data[row][i] = "  "
        
        # Enter the file and overwrite the 1 and 0s with the qr code 
        fobj = open(file_name, "w")
        for j in range(len(self.data)):
            for k in range(len(self.data[j])):
                fobj.write(self.data[j][k])
            fobj.write("\n")
            
        # Close the file
        fobj.close()
        

    def equals(self, another_data):
        """
        Returns a boolean to check if both objects are equal (if the data \
        attribute is the same)
        Arguments:
            another_data (TxtData): the data we want to compare to self.data
        Returns:
            True or False (bool): if both objects are equal
            
        Examples:
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ] 
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list)
        >>> my_txt_1.equals(my_txt_2)
        True
        
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ] 
        >>> my_list_2 = [ [1, 2, 3], [4, 5, 7] ] 
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list_2)
        >>> my_txt_1.equals(my_txt_2)
        False
        
        >>> my_list = [ [4, 5, 6], [6, 8, 6] ] 
        >>> my_list_2 = [ [4, 5, 6], [6, 8, 6] ] 
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list_2)
        >>> my_txt_1.equals(my_txt_2)
        True
        
        """
        
        # Check if both objects are equal
        return another_data.data == self.data
    
    
    def approximately_equals(self, another_data, precision):
        """
        Returns a boolean to check if both objects are approximately equal \
        (if the inconsistent rate of the two data attributes is not greater \
        than the input precision)
        Arguments:
            another_data (TxtData): the data we want to compare to self.data
            precision (non-negative float): the precision we want to have
        Returns:
            True or False (bool): if both objects are approximately equal
            
        Examples:
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_list_2 = [ [1, 2, 3], [7, 8, 9] ]
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list_2)
        >>> my_txt_1.approximately_equals(my_txt_2, 0.5)
        True
        
        >>> my_list = [ [7, 2, 3], [4, 5, 6] ]
        >>> my_list_2 = [ [1, 2, 3], [7, 8, 9] ]
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list_2)
        >>> my_txt_1.approximately_equals(my_txt_2, 0.5)
        False
        
        >>> my_list = [ [1, 2, 3], [4, 5, 6] ]
        >>> my_list_2 = [ [1, 2, 3], [7, 8, 9] ]
        >>> my_txt_1 = TxtData(my_list)
        >>> my_txt_2 = TxtData(my_list_2)
        >>> my_txt_1.approximately_equals(my_txt_2, 0.2)
        False

        """
        
        # Set the counter of different values and the number of values to 0
        counter = 0
        number_values = 0
        
        # Enter each value and compare the values for both objects
        for i in range(len(another_data.data)):
            for j in range(len(another_data.data[i])):
                number_values +=1
                
                # Check if the values are not the same
                if another_data.data[i][j] != self.data[i][j]:
                    counter += 1
                    
            # Compute the inconsistent rate
            inconsistent_rate = counter/number_values
            
        return inconsistent_rate <= precision