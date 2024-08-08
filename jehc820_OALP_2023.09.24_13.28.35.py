import sys

input_content = sys.stdin.read().split('\n')
#file = open("test.txt", "r")
#input_content = file.read().split('\n')

def create_hash_table():
    hash_table = [''] * 1000
    for i in range(1000):
        hash_table[i] = "0" 

    return hash_table

def mid_square_hash_value(degree_seq):

    
    while (len(degree_seq) < 3) or (len(degree_seq) % 2 == 0):
        degree_seq += "0"

    #Let d equal the integer obtained from the three middle digits of DS

    d = str(degree_seq[int(len(degree_seq)//2 - 1):int(len(degree_seq)//2 + 2)])

    #Hash value is the integer denoted by the three middle digits of d 
    d_square = str(int(d) ** 2)  

    while (len(d_square)  < 3) or (len(d_square)  % 2 == 0):
        d_square += "0"
        
    hash_value = int(d_square[int(len(d_square)//2 - 1):int(len(d_square)//2 + 2)])

    return hash_value
    
def hashing_ms(order_position, order_of_graph, hash_table):
    while order_of_graph != 0:
        degree_seq = []
        
        for i in range(order_position + 1, order_position + order_of_graph + 1):
            #print(input_content[i].split())
            degree_seq.append(len(input_content[i].split()))
            
        degree_seq = sorted(degree_seq, reverse=True)
        #print(degree_seq)
        degree_seq = ''.join([str(degree_seq[j]) for j in range(len(degree_seq))])
        #print(degree_seq)

        hash_value = mid_square_hash_value(degree_seq)

        if hash_table[hash_value] == "0":
            hash_table[hash_value] = "1"
            
        else:
            while hash_table[hash_value] == "1":
                hash_value += 1
                if hash_value >= 1000:
                    hash_value = hash_value % 1000
                
            hash_table[hash_value] = "1"

        order_position += order_of_graph + 1
        order_of_graph = int(input_content[order_position])

    return hash_table

def main(input_content):
    hash_table = create_hash_table()
    
    order_position = 0
    order_of_graph = int(input_content[order_position])

    return hashing_ms(order_position, order_of_graph, hash_table)

hash_table_list = main(input_content)
for i in range(len(hash_table_list)):
    print(hash_table_list[i])
