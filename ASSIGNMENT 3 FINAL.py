# The goal of this program is to decipher a coded message.

# Unchanging values
MAXIMUM_LENGTH = 10000


def is_not_valid(is_string):
    """
    Returns a boolean when given a string value (to check if the string
    only contains letters or a space)
    Parameters:
        is_string: A string
    Returns:
        True/False: A boolean value
        
    Examples:
    >>> is_not_valid("asfg123 asdf")
    True
    >>> is_not_valid("THIS DEFINITELY is a CRazY String")
    False
    >>> is_not_valid("98")
    True
    """
    
    # Traverse the string
    for i in (is_string):
        
        # Check if every character is a letter or a space
        if not ((i >= "a" and i <= "z") or (i >= "A" and  i <= "Z") \
                or i == " "):
            
            return True
    
    return False


def is_not_square(is_string):
    """
    Returns a boolean when given a string value (to check if the length
    of the string forms a square number)
    Parameters:
        is_string: A string
    Returns:
        True/False: A boolean value
    
    Examples:
    >>> is_not_square("abc")
    True
    >>> is_not_square("four")
    False
    >>> is_not_square("It returns false")
    False
    """
    
    # Check if each index of the string is the square root
    for i in range(1, len(is_string) + 1):
        if i ** 2 == len(is_string):
            
            return False

    return True
    

def string2list(is_string):
    """
    Return a 2D Square list when given a string. If the string is not valid,
    returns an empty list.
    Parameters:
        is_string: A string
    Returns:
        final_list: The computed 2d Square list
        
    Examples:
    >>> string2list("Hello Bye")
    [['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]
    >>> string2list("A")
    [['A']]
    >>> string2list("This is not valid")
    []
    """
    
    # Check if the string is valid by calling the 2 previous functions
    not_valid = is_not_valid(is_string)
    empty_list = []
    not_square = is_not_square(is_string)
    if not_valid or not_square or (len(is_string) > MAXIMUM_LENGTH) or \
        (len(is_string) == 0):
        
        # The string is not valid
        return empty_list
    else:
        # Create empty lists, and create index_list which will be the number
        # of rows and columns of the 2d square list
        final_list = []
        temporary_list = []
        for i in range(len(is_string) + 1):
            if i ** 2 == len(is_string):
                index_list = i
                temporary_list = list(is_string)
        
        # Create each sublist and add it to the final list
        for j in range(0, len(temporary_list), index_list):
            sublist = temporary_list[j:j + index_list]
            final_list.append(sublist)
            
        return final_list                
                               
    
   
def add_space(input_text):
    """
    Returns an output text when given an input text (the new string can
    contain some new spaces)
    Parameters:
        input_text (str): A string, that we can modify
    Returns:
        output_text: The new computed string
    
    Examples:
    >>> add_space("HelloEveryone")
    'Hello Everyone'
    >>> add_space("ThisIsAnExample")
    'This Is An Example'
    >>> add_space("THIsDefinitelyIsAcrazyString")
    'THIs Definitely Is Acrazy String'
    """
    
    # Transform the string into a list since strings are immutable
    my_list = list(input_text)
    
    # Traverse the new list by adding spaces (when an upper case letter is
    # between two lower case letters)
    for i in range(2, len(my_list)):
        if "a" <= my_list[i - 2] <= "z" and "a" <= my_list[i] <= "z" and \
          "A" <= my_list[i -1] <= "Z":
            my_list.insert(i - 1, " ")
            
    # Transform back the list into a string
    output_text = "".join(my_list)
    
    return output_text


def list2string(twoD_list):
    """
    Returns a string that was converted from a 2D List, and calls the previous
    function to add space in the computed string.
    Parameters:
        twoD_list: A 2D List
    Returns:
        final_string: The computed string
        
    Examples:
    >>> list2string([["H", "e", "l"], ["l", "o", "o"], ["B", "y", "e"]])
    'Helloo Bye'
    >>> list2string([["C", "r", "a","z"], ["y", "S"], \
    ["t", "r", "i", "n", "g"]])
    'Crazy String'
    >>> list2string([["a", "T"], ["w", "o", "d", "L"], ["i", "s", "t"]])
    'a Twod List'
    """
    
    final_string = ""
    # Creating a nested loop in order to enter each sublist
    for sublist in twoD_list:
        for temporary_string in sublist:
            temporary_string = "".join(sublist)
        final_string += temporary_string
        
    # Calling the add_space function 
    final_string = add_space(final_string)

    return final_string


def horizontal_flip(square_list):
    """
    Takes a 2D Square list and modifies it by flipping it horizontally, does
    not return anything.
    Parameters:
        square_list: A 2D List
    Returns:
        None
    
    Examples:
    >>> input_list = [["1", "2"], ["3", "4"]]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['2', '1'], ['4', '3']]
    
    >>> input_list = [["This", "is"], ["a", "list"]]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['is', 'This'], ['list', 'a']]
    
    >>> input_list = [["This", "is", "a"], ["3", "times", "three"], \
    ["super", "cool", "matrix"]]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['a', 'is', 'This'], ['three', 'times', '3'], ['matrix', 'cool', 'super']]
    """

    # Use nested loops to enter each sublist
    for sublist in square_list:
        # Define two parameters for each sublist, the length and
        # an index counter, in order to flip everything
        length_sub = len(sublist)
        counter = 1
        
        for j in range(length_sub // 2):
            sublist[j], sublist[length_sub - counter] = sublist[length_sub - counter], sublist[j]
            counter += 1


def transpose(square_list):
    """
    Takes a 2D Square list and modifies it by flipping it over its diagonal,
    does not return anything.
    Parameters:
        square_list: A 2D List (list of lists)
    Returns:
        None    
    
    Examples:
    >>> input_list = [["h", "I", "B"], ["e", "o", "y"], ["l", " ", "e"]]
    >>> transpose(input_list)
    >>> input_list
    [['h', 'e', 'l'], ['I', 'o', ' '], ['B', 'y', 'e']]
    
    >>> input_list = [["A", "2"], ["times", "two"]]
    >>> transpose(input_list)
    >>> input_list
    [['A', 'times'], ['2', 'two']]
    
    >>> input_list = [["This", "is", "a"], ["simple", "but", "pretty"], \
    ["function", "to", "transpose"]]
    >>> transpose(input_list)
    >>> input_list
    [['This', 'simple', 'function'], ['is', 'but', 'to'], \
    ['a', 'pretty', 'transpose']]
    """
    
    # Use nested loops to enter each element of each row and column
    for sublist in range(len(square_list)):
        for i in range(sublist, len(square_list)):
            
            # Exchange rows and columns
            square_list[sublist][i], square_list[i][sublist] = \
            square_list[i][sublist], square_list[sublist][i]


def flip_list(square_list):
    """
    Takes a 2D Square list and modifies it by flipping it horizontally, then
    flipping it over its diagonal, does not return anything.
    Parameters:
        square_list: A 2D List
    Returns:
        None
    
    Examples:
    >>> input_list = [["B", "I", "H"], ["y", "o", "e"], ["e", " ", "l"]]
    >>> flip_list(input_list)
    >>> input_list
    [['H', 'e', 'l'], ['I', 'o', ' '], ['B', 'y', 'e']]
    
    >>> input_list = [["F", "o"], ["u", "r"]]
    >>> flip_list(input_list)
    >>> input_list
    [['o', 'r'], ['F', 'u']]
    
    >>> input_list = [["Th", "is", "is", "a"], ["crazy", "four", "b", "y"], \
    ["4", "Ma", "t", "r"], [" ", "i", "x", " "]]
    >>> flip_list(input_list)
    >>> input_list
    [['a', 'y', 'r', ' '], ['is', 'b', 't', 'x'], ['is', 'four', 'Ma', 'i'], \
    ['Th', 'crazy', '4', ' ']]

    """
    
    # Call the two previous functions to modify the list (horizontally and
    # diagonally)
    horizontal_flip(square_list)
    transpose(square_list)


def decipher_code(is_string):
    """
    Returns a computed string when given an initial string
    Parameters:
        is_string: A string
    Returns:
        deciphered_sentences: The computed new string
        
    Examples:
    >>> decipher_code("ttuoYrAtwoinLAundibKgSson.roelf ad \
    YfImPAoitmr ucIeoGAisrgoraO")
    'You Know About List And String It Is Official You Are A Good Programmer'
    
    >>> decipher_code("This is not valid.Four")
    'or Fu'
    
    >>> decipher_code(" ")
    ' '
    """
    # Check if there are multiple sentences in the string
    long_string = is_string.split(".")
    
    # Create an empty string
    deciphered_sentences = ""
    
    # Make sure that each sentence is valid
    for short_string in long_string:
        if not is_not_valid(short_string):
                
            # Decipher each sentence then add it in the final string
            sentence_list = string2list(short_string)
            flip_list(sentence_list)
            deciphered_sentences += list2string(sentence_list)
            
    return deciphered_sentences
