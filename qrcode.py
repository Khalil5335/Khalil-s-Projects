# Import statements
from helper import *
from txtdata import *

class QRCode:
    """
    Represents an object of the class QRCode:
    Attributes:
        last_update_date (Dict): a dictionary with ”Day”, ”Month”, and ”Year” \
        as keys
        owner:  a string representing the owner of the QR code.
        data (TxtData): object representing the QR code itself
        error_correction:  a float indicating the error correction capability
    """
    
    
    def __init__(self, file_path, last_update_date = "00/00/0000", \
                 owner = "Default Owner", error_correction = 0.0):
        """
        The constructor of the class QRCode:
        Parameters:
            file_path (str): A string
            last_update_date (str): A string
            owner (str):  a string representing the owner of the QR code.
            error_correction (float): A float value
        Returns:
            None, creates an object
            
        Examples:
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2024", "Vivian", \
            0.1)
            >>> my_qrcode.last_update_date["Day"]
            '01'
            >>> my_qrcode.last_update_date["Month"]
            '09'
            >>> my_qrcode.last_update_date["Year"]
            '2024'
            >>> my_qrcode.owner
            'Vivian'
            >>> my_qrcode.error_correction
            0.1
            
            >>> my_qrcode_2 = QRCode("small_data.txt")
            >>> my_qrcode_2.last_update_date["Day"]
            '00'
            >>> my_qrcode_2.last_update_date["Month"]
            '00'
            >>> my_qrcode_2.last_update_date["Year"]
            '0000'
            >>> my_qrcode_2.owner
            'Default Owner'
            >>> my_qrcode_2.error_correction
            0.0
            
            >>> my_qrcode = QRCode("small_data.txt", "1/9/2024", "Vivian", 0.1)
            Traceback (most recent call last):
            ValueError: Input format incorrect!
        """
        
        self.data = TxtData(get_data(file_path))
        
        # Call the convert_date function from the helper.py file
        self.last_update_date = convert_date(last_update_date)
        self.owner = owner
        self.error_correction = error_correction
       
       
    def __str__(self):
        """
        Creates a str method that returns a string
        Arguments:
            None
        Returns:
            message (str): The computed string
            
        Examples:
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2024", "Vivian", \
            0.1)
            >>> print(my_qrcode)
            The QR code was created by Vivian and last updated in 2024.
            The details regarding the QR code file are as follows:
            This TxtData object has 10 rows and 10 columns.
            
            >>> my_qrcode = QRCode("small_data_2.txt", "01/09/2024", \
            "William", 0.1)
            >>> print(my_qrcode)
            The QR code was created by William and last updated in 2024.
            The details regarding the QR code file are as follows:
            This TxtData object has 4 rows and 4 columns.
            
            >>> my_qrcode = QRCode( \
            "data_but_the_file_contains_other_characters.txt", "01/09/2024", \
            "William", 0.1)
            Traceback (most recent call last):
            ValueError: File should contain only 0s and 1s!
            
        """
        
        # Write the message by using the attributes then return it
        message = "The QR code was created by " + self.owner + \
        " and last updated in " + self.last_update_date["Year"] + ".\n" \
        "The details regarding the QR code file are as follows:\n" \
        + str(self.data)
        
        return message
    
    
    def equals(self, another_qrcode):
        """
        Returns a boolean when giving a QRCode object indicating whether \
        the two QRCodes are the same (if the data and the error_correction \
        attributes are the same)
        Arguments:
            another_qrcode (QRCode): A QRCode object
        Returns:
            True or False (bool): are the two objects equal?
            
        Examples:
            >>> my_qrcode_copy = QRCode("small_data.txt", "01/09/2022",\
            "Xuanpu", 0.1)
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2024", "Vivian", \
            0.1)
            >>> my_qrcode.equals(my_qrcode_copy)
            True
            
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2022", \
            "Xuanpu", 0.1)
            >>> my_qrcode_copy = QRCode("small_data_2.txt", "01/09/2022", \
            "Xuanpu", 0.1)
            >>> my_qrcode.equals(my_qrcode_copy)
            False
            
            >>> my_qrcode_copy = QRCode("small_data.txt", "01/09/2022", \
            "Xuanpu", 0.1)
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2024", "Vivian", \
            0.5)
            >>> my_qrcode.equals(my_qrcode_copy)
            False
        """
        
        # Check if both the data and the error_correction \
        # attributes are the same)
        return self.data.equals(another_qrcode.data) and \
               self.error_correction == another_qrcode.error_correction
    
    def is_corrupted(self, precise_qrcode):
        """
        Returns a boolean to check if the object is corrupted by comparing it \
        to a precise QR code
        Arguments:
            precise_qrcode (QRCode): A QRCode object
        Returns:
            True or False (bool): is the object corrupted?
            
        Examples:
            >>> my_qrcode_copy = QRCode("small_data_2.txt", "01/09/2022", \
            "Xuanpu", 0.9)
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2022", "Xuanpu", \
            0.9)
            >>> my_qrcode.is_corrupted(my_qrcode_copy)
            False
            
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2022", "Xuanpu",\
            0.9)
            >>> my_qrcode_copy = QRCode(\
            "data_but_the_file_contains_other_characters.txt", "01/09/2022", \
            "Xuanpu", 0.9)
            Traceback (most recent call last):
            ValueError: File should contain only 0s and 1s!
            
            >>> my_qrcode_copy = QRCode("almost_empty_file.txt", "01/09/2022", \
            "Vivian", 0.9)
            >>> my_qrcode = QRCode("small_data.txt", "01/09/2022", "Xuanpu",\
            0.9)
            >>> my_qrcode.is_corrupted(my_qrcode_copy)
            True           
        """
        
        # Returns True or False depending on if the QRCode is corrupted
        return not (self.data.approximately_equals(precise_qrcode.data, \
                                                   self.error_correction))
        