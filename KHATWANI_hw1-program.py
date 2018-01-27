import random
# random is a pre-defined module which contains various functions for randomizing inputs

# This function is used to randomize content of string 'HelloW World!' and return in string format
def world_shuffle():
	input_str = "Hello World!"
	input_list = []    #list to extract characters from string
	for char in input_str:
		input_list.append(char)
	random.shuffle(input_list)
	input_str = ""
	for char in input_list:
		input_str = input_str + char
	return input_str   #returns randomized string


# This function is to convey use of 'set' data structure in python
# SET data structure is beneficial while extracting unique elements
def shuffle_anyset():
	unique_set = set() #declaration of set
	input_str = "Hello World!"
	unique_set = set(input_str)
	input_str = ""
	for char in unique_set:
		input_str = input_str + char
	return input_str


# This function is used for creating a list of tuples in (x,y) coordinate format
def make_map():
    output_list = []
    for first_no in range(1,6):
        for sec_no in range(1,6):
            output_list.append((first_no,sec_no))    #loop for creating tuple combination

    for i in range(1,len(output_list)+1):      # loop for printing list
        print(output_list[i-1],end=','), # while creating the list I appended from 0 that's why print starts from 'index-1'
        if i%5 == 0:
            print()

# This function creates a dictionary which contains the tuples as values and key from 'A1'.. to 'E5'
def map_dict():
	dict = {}
	key_char = ['A','B','C','D','E']
	key_no = ['1','2','3','4','5']
	for char in range(0,5):
		for no in range(0,5):
			key = key_char[char] + key_no[no]
			dict[key] = (char+1,no+1)    #although index starts from 0 in 'for' loops the values start from 1 that's why (char+1,no+1)
	return dict

# this function is responsible for calculating manhattan distance
def manhattan_dist(label_x,label_y):
    # here above function is called for code reusablity
    dict = map_dict()
# 0 is returned if key doesn't exist
    tuple_x = dict.get(label_x,0)
    tuple_y = dict.get(label_y,0)
    if(tuple_y == 0 or tuple_x == 0):
        print('Invalid Coordinates:',label_x,',',label_y)
        return "Enter valid co-ordinates please !!"
    m_dist_x = abs(tuple_x[0] - tuple_y[0])
    m_dist_y = abs(tuple_x[1] - tuple_y[1])
    m_dist = m_dist_x + m_dist_y
    return "Manhattan Distance is "+str(m_dist)

# Main function
def main():
    print('Problem 1(b):')
    print('For input String "Hello World!"')
    print('Shuffled string is',world_shuffle())

    print()

    print('Problem 1(c):')
    print('For input String "Hello World!"')
    print('Contents of set',shuffle_anyset())

    print()

    print('Problem 1(d):')
    print('List containing 25 tuples from (1,1),(1,2)..to ..(5,5)')
    make_map()

    print()

    print('Problem 2(a)')
    print('Dictionary containing key/value pairs')
    print(map_dict())

    print()

    print('Problem 2(b)')
    print('Manhattan Distance for different test cases')
    print('Manhattan Distance between (A1,D4):',manhattan_dist('A1','D4'))
    print('Manhattan Distance between (C3,E5):',manhattan_dist('C3','E5'))
    print()
    print('Manhattan Distance for invalid values')
    print('Manhattan Distance between (Z1,F3)')
    print(manhattan_dist('Z1','F3'))
    print('Manhattan Distance between (A1,F3)')
    print(manhattan_dist('A1','F3'))

if __name__ == '__main__':
    main()
