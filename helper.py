def convert_date(date_str):
    """
    Convert a string into a dictionary, to get the date
    Parameter:
        date_str: A string value
    Returns:
        my_dict: The computed dictionary
        
    Examples:
    >>> convert_date("09/01/2024")
    {'Day': '09', 'Month': '01', 'Year': '2024'}
    
    >>> convert_date("15/2/2007")
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    
    >>> convert_date("15/02/2007/8320")
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    """
    
    # Transform the string into a list with "/" as a separator
    list_str = date_str.split("/")
    
    # Check if the input format is "dd/mm/yyyy", raise an error if not
    if len(list_str) != 3:
        raise ValueError ("Input format incorrect!")
    
    if (len(list_str[0]) != 2) or (len(list_str[1]) != 2) \
       or (len(list_str[2]) != 4):
        raise ValueError ("Input format incorrect!")
    
    # Create a dictionary corresponding to the date
    else:
        Day, Month, Year = list_str
        my_dict = {"Day": Day, "Month": Month, "Year": Year}
        
        return my_dict


def get_data(file_path):
    """
    Returns a nested List of integer when given a string (a file name)
    Parameters:
        file_path: A string, the name of the file
    Returns:
        my_list: The computed nested list of integers
    
    Examples:
    >>> get_data("small_data.txt")
    [[0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1, 1, 0, 0, 1], \
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 1], \
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0], \
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 1], \
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 1, 1, 0, 1]]
    
    >>> get_data("data_but_the_file_contains_other_characters.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    
    >>> get_data("small_data_2.txt")
    [[0, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0]]
    """
    
    # Create an empty list
    my_list = []
    
    # Enter the file and read it
    fobj = open(file_path, "r")
    
    # Check if each line is valid
    for lines in fobj:
        
        # We don't want the "\n" in the final list
        strip_lines = lines.strip("\n")
        for word in strip_lines:
            for char in word:
                
                # Check if the file is only made of 0s and 1s
                if char != "0" and char != "1":
                    raise ValueError ("File should contain only 0s and 1s!")
        
        # Create the 2D list of 0s and 1s
        my_list.append(list(strip_lines))
    
    # The 0s and 1s are string, we want to convert them to integers
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            my_list[i][j] = int(my_list[i][j])
    
    return my_list