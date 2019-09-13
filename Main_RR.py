import hashlib
 
def find_text_file():
    file = open('password_file.txt')
    line = file.readlines()
    return line

def get_password(str):
    all_passwords = []
    
    if not str: 
        return all_passwords
    line_index = str[:1]
    line_str = ''.join(line_index)
    
    password = line_str[line_str.find(','):]
    password = password[1:]
    password = password[password.find(','):]
    password = password[1:]    
    
    all_passwords.append(password)
    all_passwords += get_password(str[1:])    
    return all_passwords

def get_salt(str): 
    all_values = []
    
    if not str: 
        return all_values
    line_index = str[:1]
    line_str = ''.join(line_index)
    
    salt_value = line_str[line_str.find(','):]
    salt_value = salt_value[1:]
    salt_value = salt_value[:salt_value.find(',')]
    
    all_values.append(salt_value)
    all_values += get_salt(str[1:])
    return all_values

def gen(current_list,num_list,min3,max7):
    permutations = []  
    
    if min3 == max7+1:
        permutations.append(current_list)
        return permutations
    
    if len(current_list) == min3: 
        permutations.append(current_list)
        return permutations + gen(current_list,num_list,min3+1,max7)
    
    for item in num_list:    
        new_c = current_list.copy()
        new_c.append(item)
        permutations += gen(new_c,num_list,min3,max7)
    
    return permutations

def to_string(list):
    perm_list = []
    for i in list:
        perm_str = ''    
        
        for j in i:
            perm_str += str(j)
            
        perm_list.append(perm_str)
        
    return perm_list

def find_password(num,salt,passwords):
    index = 0
    for i in salt:
        new_str = ''    
        for j in num:           
            new_str =   j.rstrip() + i.rstrip()
            if((hash_with_sha256(new_str)).rstrip() == passwords[index].rstrip()):
                print("User", index, ": ", j.rstrip())
                #print("Hash Decoded is ", new_str)
                break
        index += 1

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    file = find_text_file()
    passwords = get_password(file)
    salt_list = get_salt(file)

    all_possible_numbers = []
    num_list = [0,1,2,3,4,5,6,7,8,9]
    generate = gen(all_possible_numbers,num_list,3,7)
               
    perm_list = to_string(generate)  
    find_password(perm_list,salt_list,passwords)

main()