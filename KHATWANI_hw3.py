'''
Name: Mohit Khatwani
Campus ID: AJ75499

caluclate_probability(A,B,C,D,E) takes 5 arguments and returns the probability is input query is valid.

'''


def get_query(A,B,C,D,E):
    first_term, sec_term, third_term, fourth_term, fifth_term = [],[],[],[],[]

    #checking valid conditions for query
    #if there is no query variables
    query = [A,B,C,D,E]
    if 2 not in query and 3 not in query:
        return "In-Valid Query!!"
    #generalized enumeration formula consists of 5 terms
    #sumation of these five terms in calculated
    #first term : P(A)
    if A != 4:
        #if A is true
        if  A == 3 or A == 1:
            first_term.append([3,4,4,4,4])
        elif A == 2 or A == 0:
            #if A is false
            first_term.append([2,4,4,4,4])
    elif A == 4:
        first_term.append([3,4,4,4,4])
        first_term.append([2,4,4,4,4])

    if first_term == []:
        return "In-Valid Query!!"

    #second term: P(B)
    if B != 4:
        #if B is true
        if B == 3 or B == 1:
            sec_term.append([4,3,4,4,4])
        elif B == 2 or B == 0:
            sec_term.append([4,2,4,4,4])
    elif B == 4:
        sec_term.append([4,3,4,4,4])
        sec_term.append([4,2,4,4,4])

    if sec_term == []:
        return "In-Valid Query!!"

    #third term: P(C|A,B)
    list_check = [5,5,5,4,4]
    check = []
    if C != 4:
        #if C is true
        check.append("")
        if C == 3 or C == 1:
            list_check[2] = 3
        elif C == 2 or C == 0:
            list_check[2] = 2
    elif C == 4:
        list_check[2] = 4
        check.append('both')
    if A != 4:
        #if A is true
        check.append("")
        if A == 1 or A == 3:
            list_check[0] = 1
        elif A == 0 or A == 2:
            list_check[0] = 0
    elif A == 4:
        list_check[0] = 4
        check.append('both')
    if B != 4:
        #if B is true
        check.append("")
        if B == 1 or B == 3:
            list_check[1] = 1
        elif B == 0 or B == 2:
            list_check[1] = 0
    elif B == 4:
        list_check[1] = 4
        check.append('both')
    #checking In-Valid conditions for A, B and C
    if list_check[0] == 5 or list_check[1] == 5 or list_check[2] == 5:
        return "In-Valid Query!!"
    #putting values in third term
    if check.count('both') == 3:
        third_term.append([1,1,3,4,4])
        third_term.append([1,1,2,4,4])
        third_term.append([1,0,3,4,4])
        third_term.append([0,1,3,4,4])
        third_term.append([1,0,2,4,4])
        third_term.append([0,1,2,4,4])
        third_term.append([0,0,3,4,4])
        third_term.append([0,0,2,4,4])
    elif check.count('both') == 2:
        if check[0] =='both' and check[1] =='both':
            third_term.append([0,list_check[1],2,4,4])
            third_term.append([1,list_check[1],2,4,4])
            third_term.append([0,list_check[1],3,4,4])
            third_term.append([1,list_check[1],3,4,4])
        elif check[1] == 'both' and check[2] == 'both':
            third_term.append([0,0,list_check[2],4,4])
            third_term.append([0,1,list_check[2],4,4])
            third_term.append([1,0,list_check[2],4,4])
            third_term.append([1,1,list_check[2],4,4])
        elif check[0] == 'both' and check[2] == 'both':
            third_term.append([list_check[0],0,2,4,4])
            third_term.append([list_check[0],0,3,4,4])
            third_term.append([list_check[0],1,2,4,4])
            third_term.append([list_check[0],1,3,4,4])
    elif check.count('both') == 1:
        if check[0] == 'both':
            third_term.append([list_check[0],list_check[1],3,4,4])
            third_term.append([list_check[0],list_check[1],2,4,4])
        elif check[1] == 'both':
            third_term.append([0,list_check[1],list_check[2],4,4])
            third_term.append([1,list_check[1],list_check[2],4,4])
        elif check[2] == 'both':
            third_term.append([list_check[0],0,list_check[2],4,4])
            third_term.append([list_check[0],1,list_check[2],4,4])
    elif check.count('both') == 0:
        third_term.append([list_check[0],list_check[1],list_check[2],4,4])


    #fourth term: P(D|C)
    list_check = [4,4,5,5,4]
    check = []

    if C != 4:
        check.append("")
        if C == 1 or C == 3:
            list_check[2] = 1
        elif C == 0 or C == 2:
            list_check[2] = 0
    elif C == 4:
        list_check[2] = 4
        check.append('both')
    if D != 4:
        check.append("")
        if D == 3 or D == 1:
            list_check[3] = 3
        elif D == 2 or D == 0:
            list_check[3] = 2
    else:
        list_check[3] = 4
        check.append('both')
    #checking In-Valid condition for variables C and D
    if list_check[2] == 5 or list_check[3] == 5:
        return "In-Valid Query!!"
    #putting values in fourth term
    if check.count('both') == 2:
        fourth_term.append([4,4,0,2,4])
        fourth_term.append([4,4,0,3,4])
        fourth_term.append([4,4,1,2,4])
        fourth_term.append([4,4,1,3,4])
    elif check.count('both') == 1:
        if check[0] == 'both':
            fourth_term.append([4,4,0,list_check[3],4])
            fourth_term.append([4,4,1,list_check[3],4])
        elif check[1] == 'both':
            fourth_term.append([4,4,list_check[2],3,4])
            fourth_term.append([4,4,list_check[2],2,4])
    elif check.count('both') == 0:
        fourth_term.append([4,4,list_check[2],list_check[3],4])


    #fifth term: P(E|C)
    list_check = [4,4,5,4,5]
    check = []
    if C != 4:
        check.append("")
        if C == 1 or C == 3:
            list_check[2] = 1
        elif C == 0 or C == 2:
            list_check[2] = 0
    elif C == 4:
        list_check[2] = 4
        check.append('both')
    if E != 4:
        check.append("")
        if E == 3 or E == 1:
            list_check[4] = 3
        elif E == 2 or E == 0:
            list_check[4] = 2
    elif E == 4:
        list_check[4] = 4
        check.append('both')
    #checking In-Valid conditions for variables C and E
    if list_check[2] == 5 or list_check[4] == 5:
        return "In-Valid Query!!"
    #putting values in fifth term
    if check.count("both") == 2:
        fifth_term.append([4,4,0,4,2])
        fifth_term.append([4,4,0,4,3])
        fifth_term.append([4,4,1,4,2])
        fifth_term.append([4,4,1,4,3])
    elif check.count('both') == 1:
        if check[0] == 'both':
            fifth_term.append([4,4,0,4,list_check[4]])
            fifth_term.append([4,4,1,4,list_check[4]])
        elif check[1] == 'both':
            fifth_term.append([4,4,list_check[2],4,3])
            fifth_term.append([4,4,list_check[2],4,2])
    elif check.count('both') == 0:
        fifth_term.append([4,4,list_check[2],4,list_check[4]])

    #find maximum of all the lengths so that they can be made equal
    max_len = max(len(first_term),len(sec_term),len(third_term),len(fourth_term),len(fifth_term))
    #duplicate terms for ease of calculations in summation terms
    while(len(first_term) != max_len):
        first_term.extend(first_term)
    while(len(sec_term) != max_len):
        sec_term.extend(sec_term)
    while(len(third_term) != max_len):
        third_term.extend(third_term)
    while(len(fourth_term) != max_len):
        fourth_term.extend(fourth_term)
    while(len(fifth_term)!= max_len):
        fifth_term.extend(fifth_term)
    return first_term, sec_term, third_term, fourth_term, fifth_term

def get_database():
    database = []
    #for node A
    database.append(([3,4,4,4,4],0.3))
    database.append(([2,4,4,4,4],0.7))

    #for node B
    database.append(([4,3,4,4,4],0.4))
    database.append(([4,2,4,4,4],0.6))

    #for node C
    database.append(([1,1,3,4,4],0.8))
    database.append(([1,0,3,4,4],0.6))
    database.append(([0,1,3,4,4],0.5))
    database.append(([0,0,3,4,4],0.25))
    database.append(([1,1,2,4,4],0.2))
    database.append(([1,0,2,4,4],0.4))
    database.append(([0,1,2,4,4],0.5))
    database.append(([0,0,2,4,4],0.75))

    #for node D
    database.append(([4,4,1,3,4],0.2))
    database.append(([4,4,0,3,4],0.75))
    database.append(([4,4,1,2,4],0.8))
    database.append(([4,4,0,2,4],0.25))

    #for node E
    database.append(([4,4,1,4,3],0.8))
    database.append(([4,4,0,4,3],0.3))
    database.append(([4,4,1,4,2],0.2))
    database.append(([4,4,0,4,2],0.7))

    return database

def calculate_probability(A,B,C,D,E):
    #get all possible probability from CPT
    database = get_database()
    query = [A,B,C,D,E]
    #get query in different general term using enumeration method
    if(get_query(A,B,C,D,E) == 'In-Valid Query!!'):
        return "In-Valid Query!!"
    else:
        first,sec,third,fourth,fifth = get_query(A,B,C,D,E)


    sum_p = 0
    for l in range(len(first)):
        p1 = [tuple for tuple in database if tuple[0] == first[l]][0][1]
        p2 = [tuple for tuple in database if tuple[0] == sec[l]][0][1]
        p3 = [tuple for tuple in database if tuple[0] == third[l]][0][1]
        p4 = [tuple for tuple in database if tuple[0] == fourth[l]][0][1]
        p5 = [tuple for tuple in database if tuple[0] == fifth[l]][0][1]
        sum_p += p1*p2*p3*p4*p5
    for i in range(len(query)):
        if query[i] == 2:
            query[i] = 3
        elif query[i] == 3:
            query[i] = 2

    first,sec,third,fourth,fifth = get_query(query[0],query[1],query[2],query[3],query[4])

    sum_n = 0
    for l in range(len(first)):
        p1 = [tuple for tuple in database if tuple[0] == first[l]][0][1]
        p2 = [tuple for tuple in database if tuple[0] == sec[l]][0][1]
        p3 = [tuple for tuple in database if tuple[0] == third[l]][0][1]
        p4 = [tuple for tuple in database if tuple[0] == fourth[l]][0][1]
        p5 = [tuple for tuple in database if tuple[0] == fifth[l]][0][1]
        sum_n += p1*p2*p3*p4*p5
    print("checking float values",sum_p / (sum_p + sum_n))
    suma = round(sum_p / (sum_p + sum_n),1)
    return suma


if __name__ == "__main__":
    print(calculate_probability(3,4,4,4,4))
    print(calculate_probability(2,4,3,4,4))
    print(calculate_probability(3,4,2,1,4))
    print(calculate_probability(2,1,0,3,4))
    print(calculate_probability(2,3,4,4,0))
    print("chekcing")
    print(calculate_probability(1,1,4,4,3))
    print(calculate_probability(3,3,3,3,3))
    print(calculate_probability(3,3,4,4,4))
