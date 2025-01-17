# The objective of this code is to ask the user to input 
# characteristics about a rocket in order to compute and 
# obtain information on the rocket (cost, weight, height...)


# Import some math functions helpful for computation (pi, sqrt, e, sin...)
import math

# Here are all the unchanging values
ONE_METER_IN_FEET = 3.28
DENSITY = 1.225
FUEL_ROCKET_MIN = 1360
FUEL_ROCKET_AVG = 2000
FUEL_ROCKET_MAX = 2721
MASS_MIN = 100000
MASS_MAX = 400000
COST_MATERIAL = 5
COST_FUEL = 6.1
TAX_QUEBEC = 115/100 # full price + 15/100 of tax
MAX_STORAGE_WEIGHT = 5/100
MAX_STORAGE_VOLUME = 40/100
MIN_WEIGHT_BOX = 20
MAX_WEIGHT_BOX = 500
VOLUME_BOX_MIN = 0.125
GRAVITATIONAL_ACCELERATION = 9.81


def feet_to_meter(length_in_feet):
    """
    Returns a length in meters when given a length in feet
    Parameters:
        length (float): A positive float value, in feet
    Returns:
        length_in_meters (positive float): The computed length in meters
        
    Examples:
    >>> feet_to_meter(5.0)
    1.52
    >>> feet_to_meter(10.55)
    3.22
    >>> feet_to_meter(9.81)
    2.99
    
    """
    
    # Compute the length (1 meter is equivalent to 3.28 feet)
    length_in_meters = round(length_in_feet * 1 / ONE_METER_IN_FEET, 2)
    
    return length_in_meters


def rocket_volume(radius, height_cone, height_cyl):
    """
    Returns the volume of a rocket with a given radius, the height of 
    a cone and the height of a cylinder
    Parameters:
        radius (float in meters): A positive float value
        height_cone (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
    Returns:
        volume_of_rocket (positive float): the computed volume
        of the rocket
    
    Examples:
    >>> rocket_volume(2.0, 7.0, 3.0)
    67.02
    >>> rocket_volume(4.0, 8.0, 5.0)
    385.37
    >>> rocket_volume(7.6, 15.2, 31.4)
    6617.18
        
    """
    
    # Compute the volume of a cone and a cylinder
    volume_cone = math.pi * radius ** 2 * height_cone / 3
    volume_cylinder = math.pi * radius ** 2 * height_cyl
    
    # The rocket is made of the cylinder and the cone
    volume_of_rocket = round(volume_cone + volume_cylinder, 2)
    
    return volume_of_rocket


def rocket_area(radius, height_cone, height_cyl):
    """
    Returns the area of the rocket with a given radius, the height of 
    a cone and the height of a cylinder
    Parameters:
        radius (float in meters): A positive float value
        height_cone (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
    Returns:
        total_surface_area (positive float in meters squared): This is
        the computed area of the rocket
        
    Examples:
    >>> rocket_area(2.0, 7.0, 3.0)
    96.01
    >>> rocket_area(4.0, 8.0, 5.0)
    288.33
    >>> rocket_area(7.6, 15.2, 31.4)
    2086.63

    """
    
    # Compute the surface area of a cone and a cylinder
    surface_area_cone = math.pi * radius * (radius + 
    math.sqrt(height_cone ** 2 + radius ** 2))
    surface_area_cyl = 2 * math.pi * radius * (height_cyl + radius)
    
    # Compute the area of the rocket, we do not count the shared 
    # circle face of the cone and cylinder
    area_circle = math.pi * radius ** 2
    total_surface_area = round(surface_area_cone + surface_area_cyl - 
    2 * area_circle, 2)
    
    return total_surface_area


def rocket_mass(radius, height_cone, height_cyl):
    """
    Returns the mass of the rocket with a given radius, the height of 
    a cone and the height of a cylinder
    Parameters:
        radius (float in meters): A positive float value
        height_cone (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
    Returns:
        mass_rocket (positive float): The computed mass of the rocket
        
    Examples:
    >>> rocket_mass(2.0, 7.0, 3.0)
    82.1
    >>> rocket_mass(4.0, 8.0, 5.0)
    472.08
    >>> rocket_mass(7.6, 15.2, 31.4)
    8106.05

    """
    
    # Compute the mass of the rocket by using its volume and density
    mass_rocket = round(DENSITY *
    rocket_volume(radius, height_cone, height_cyl), 2)
    
    return mass_rocket


def rocket_fuel(radius, height_cone, height_cyl, velocity_e,
velocity_i, time):
    """
    Returns the mass of fuel needed by the rocket with a given radius,
    the height of a cone, the height of a cylinder, two velocities
    (exhaust and initial) and a time
    Parameters:
        radius (float in meters): A positive float value
        height_cone (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
        velocity_e (float in m/s): A positive float value
        velocity_i (float in m/s): A positive float value
        time (float in s): A positive float value
    Returns:
        total_fuel (positive float): The computed total amount of fuel
        
    Examples:
    rocket_fuel(50.0, 100.0, 800.0, 700.0, 300.0, 120.0)
    4616444.53
    >>> rocket_fuel(4.0, 8.0, 5.0, 800.0, 400.0, 140.0)
    190706.25
    >>> rocket_fuel(7.6, 15.2, 31.4, 1200.6, 350.9, 100.5)
    139431.72
    
    """
    
    # Compute the mass of fuel needed to launch
    mass_fuel_launch = (rocket_mass(radius, height_cone, height_cyl)
    * (math.e ** (velocity_i / velocity_e) - 1))
    
    # Depending on the mass of the rocket, the amount of fuel burned
    # per second is not the same
    if rocket_mass(radius, height_cone, height_cyl) < MASS_MIN:
        trip_fuel = FUEL_ROCKET_MIN * time
    elif rocket_mass(radius, height_cone, height_cyl) < MASS_MAX:
        trip_fuel = FUEL_ROCKET_AVG * time
    else:
        trip_fuel = FUEL_ROCKET_MAX * time
        
    # Compute the total amount of fuel (the launch and the trip)
    total_fuel = round(mass_fuel_launch + trip_fuel, 2)
    
    return total_fuel


def calculate_cost(radius, height_cone, height_cyl, velocity_e,
velocity_i, time, tax):
    """
    Returns the cost of building and launching a rocket with a given
    radius, the height of a cone, the height of a cylinder, two
    velocities, a time and a tax percentage (0 or 15/100)
    Parameters:
        radius (float in meters): A positive float value
        height_cone (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
        velocity_e (float in m/s): A positive float value
        velocity_i (float in m/s): A positive float value
        time (float in s): A positive float value
        tax (boolean): True or False
    Returns:
        total_cost (positive float): The computed cost of the whole
        project
        
    Examples:
    >>> calculate_cost(50.0, 100.0, 800.0, 700.0, 300.0, 120.0, False)
    29544028.78
    >>> calculate_cost(4.0, 8.0, 5.0, 800.0, 400.0, 140.0, True)
    1339462.24
    >>> calculate_cost(51.5, 134.5, 65.8, 787.5, 398.4, 121.1, False)
    6810547.7

    """

    # Compute the cost of materials and the cost of fuel
    material_cost = COST_MATERIAL * rocket_area(radius,
    height_cone,height_cyl)
    fuel_cost = COST_FUEL * rocket_fuel(radius, height_cone, height_cyl,
    velocity_e, velocity_i, time)
    
    # Depending on if we consider taxes, the computation is different
    if tax:
        total_cost = round((material_cost + fuel_cost) * TAX_QUEBEC, 2)
    else:
        total_cost = round(material_cost + fuel_cost, 2)
    
    return total_cost


def compute_storage_space(radius, height_cyl):
    """
    Returns the storage space's width, length and height with a given
    raidus and the height of a cylinder
    Parameters:
        radius (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
    Returns:
        width_storage (positive float): The computed width of the
        storage space
        length_storage (positive float): The computed length of the
        storage space
        height_storage (positive float): The computed height of the
        storage space
        
    Examples:
    >>> compute_storage_space(5.0, 10.0)
    (7.07, 7.07, 5.0)  
    >>> compute_storage_space(4.0, 5.0)
    (5.66, 5.66, 2.5)
    >>> compute_storage_space(9.6, 4.8)
    (13.58, 13.58, 2.4)

    """
    
    # Compute the length, height and width of the storage space
    length_storage = width_storage = round(math.sqrt(2) * radius, 2)
    height_storage = round(height_cyl / 2, 2)
    
    return width_storage, length_storage, height_storage


def load_rocket(initial_weight, radius, height_cyl):
    """
    Returns the updated weight of the rocket with a given initial weight,
    radius and the height of a cylinder.
    Parameters:
        initial_weight (float in kg): A positive float
        radius (float in meters): A positive float value
        height_cyl (float in meters): A positive float value
    Returns:
        current_weight (positive float): The computed updated weight
        of the rocket
        
    Examples:
    >>> load_rocket(399.0, 100.0, 1000.0)
    No more items can be added
    399.0

    >>> load_rocket(10000.5, 123.3, 1037.4)
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): 614.2
    Enter item width: 2.0
    Enter item length: 2.0
    Enter item height: 2.0
    Item could not be added... please try again...
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): 100.1
    Enter item width: 3.1
    Enter item length: 3.2
    Enter item height: 3.3
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): Done
    No more items can be added
    10100.6

    >>> load_rocket(13589.57, 1.0, 1.0)
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): 24.8
    Enter item width: 1.0
    Enter item length: 0.3
    Enter item height: 1
    No more items can be added
    13614.37
    
    """
    
    # Compute the volume of the storage space by calling
    # the function compute_storage_spice
    width, length, height = compute_storage_space(radius, height_cyl)
    volume_storage = width * length * height
    
    # Define the maximum weight and volume of the items added 
    max_weight_items = initial_weight * MAX_STORAGE_WEIGHT
    max_volume_items = volume_storage * MAX_STORAGE_VOLUME
    current_weight = initial_weight
    
    # Check if the storage space is available for at least one small box
    if (max_weight_items < MIN_WEIGHT_BOX) or \
       (max_volume_items < VOLUME_BOX_MIN):
        print("No more items can be added")
        return round(current_weight, 2)
    
    else:
        # Ask user to input as many items as necessary and possible
        current_weight_items, current_volume_items = 0, 0
        new_item_weight = input("Please enter the weight of the next item \
(type \"Done\" when you are done filling the rocket): ")
        
        while new_item_weight != "Done":
            new_item_weight = float(new_item_weight)
            item_width = float(input("Enter item width: "))
            item_length = float(input("Enter item length: "))
            item_height = float(input("Enter item height: "))
            
            
            # Check if we can still add some items
            current_weight_items += new_item_weight
            new_item_volume = item_width * item_length * item_height
            current_volume_items += new_item_volume

    
            # First, check the contraints for the mass
            if (current_weight_items > max_weight_items) or \
            (MIN_WEIGHT_BOX > new_item_weight) or \
            (new_item_weight > MAX_WEIGHT_BOX):
                print("Item could not be added... please try again...")
                # The items could not be added so we substract mass and volume
                current_weight_items -= new_item_weight
                current_volume_items -= new_item_volume
                new_item_weight = input("Please enter the weight of the next \
item (type \"Done\" when you are done filling the rocket): ")

            
            # Then, check if the volume is correct
            elif (current_volume_items > max_volume_items) or \
            (VOLUME_BOX_MIN > new_item_volume):
                print("Item could not be added... please try again...")
                current_weight_items -= new_item_weight
                current_volume_items -= new_item_volume
                new_item_weight = input("Please enter the weight of the \
next item (type \"Done\" when you are done filling the rocket): ")

            # Finish boarding by checking the last contraints
            elif (current_weight_items > max_weight_items - MIN_WEIGHT_BOX) \
            or (current_volume_items > max_volume_items - VOLUME_BOX_MIN):
                print("No more items can be added")
                new_item_weight = "Done"
            
            else:
                new_item_weight = input("Please enter the weight \
of the next item (type \"Done\" when you are done filling the rocket): ")
        

        current_weight += current_weight_items
        return round(current_weight, 2)


def projectile_sim(simulation_time, interval, velocity_i, angle):
    """
    Prints the height of the rocket at different time intervals, with a given
    simulation time, interval duration, initial velocity and angle
    Parameters:
        simulation_time (float in seconds): A positive float value
        interval (int in seconds): A positive integer
        initial velocity (float in m/s): A positive float value
        angle (float in radians): A positive float value
    Returns:
        None
        
    Example:
    >>> projectile_sim(10, 2, 100.0, 0.79)
    0
    122.45
    205.66
    249.63
    254.36
    219.85
    >>> projectile_sim(10, 3, 150.0, 1.43)
    0
    401.4
    714.51
    939.34
    >>> projectile_sim(10, 1, 45, 0.86)
    0
    29.2
    48.59
    58.16
    57.93
    47.89
    28.04
    
    """
    
    # Print the height at time = 0s
    time = 0
    height_rocket = 0
    print(height_rocket)
    
    # Print the height for each time interval
    for time in range (0, simulation_time + 1, interval):
        height_rocket = - (1/2 * GRAVITATIONAL_ACCELERATION * time ** 2) + \
        velocity_i * math.sin(angle) * time
        
        # We do not want any more zero or non-positive heights
        if height_rocket > 0:
            print(round(height_rocket, 2))
            time = time + interval
            
        else:
            time = time + interval


def rocket_main():
    """
    Prints the cost of the trip, its weight and its height, by calling
    previous functions.
    Parameters:
        None
    Returns:
        None

    Example:
    >>> rocket_main()
    Welcome to the Rocket Simulation!
    Enter the rocket radius in feet: 50.0
    Enter the rocket cone height in feet: 100.0
    Enter the rocket cylinder height in feet: 200.0
    Enter the exhaust velocity for the upcoming trip : 700.0
    Enter the initial velocity for the upcoming trip : 300.0
    Enter the angle of launch for the upcoming trip : 0.8
    Enter the length of the upcoming trip : 1000.0
    Would you like to factor in tax? 1 for yes,  0 for no: 1
    This trip will cost $9826238.52
    Now loading the rocket:
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): 100.0
    Enter item width: 5.0
    Enter item length: 5.0
    Enter item height: 5.0
    Please enter the weight of the next item (type "Done" when you \
    are done filling the rocket): Done
    The rocket and its equipment will weigh 63690.19 kg
    Enter the simulation total time: 8
    Enter the simulation interval: 2
    Now simulating the rocket trajectory:
    0
    410.79
    782.35
    1114.66
    1407.73
    
    """

    print("Welcome to the Rocket Simulation!")

    # Calculate the cost by converting everything in meters
    radius_feet = float(input("Enter the rocket radius in feet: "))
    radius = feet_to_meter(radius_feet)
    height_cone_feet = float(input("Enter the rocket cone height in \
    feet: "))
    height_cone = feet_to_meter(height_cone_feet)
    height_cyl_feet = float(input("Enter the rocket cylinder height in \
    feet: "))
    height_cyl = feet_to_meter(height_cyl_feet)
    velocity_e = float(input("Enter the exhaust velocity for the \
    upcoming trip : "))
    velocity_i = float(input("Enter the initial velocity for the \
    upcoming trip : "))
    angle = float(input("Enter the angle of launch for the \
    upcoming trip : "))
    time = float(input("Enter the length of the upcoming trip : "))
    tax = int(input("Would you like to factor in tax? 1 for yes,  0 for no: "))
    if tax == 1:
        tax = True
    else:
        tax = False
    print("This trip will cost $"+str(calculate_cost(radius, height_cone,
    height_cyl, velocity_e, velocity_i, time, tax)))

    # Compute the weight by using rocket_mass and load_rocket
    print("Now loading the rocket:")
    initial_weight = rocket_mass(radius, height_cone, height_cyl)
    print("The rocket and its equipment will weigh",
    load_rocket(initial_weight, radius, height_cyl), "kg")

    # Print the height of the rocket at different intervals
    simulation_time = int(input("Enter the simulation total time: "))
    interval = int(input("Enter the simulation interval: "))
    print("Now simulating the rocket trajectory:")
    projectile_sim(simulation_time, interval, velocity_i, angle)
