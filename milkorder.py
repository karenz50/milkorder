def get_input(file_name):
    in_file = open(file_name, "r")
    return_cow_data = []

    def process_line(in_file):
        cow_data = in_file.readline().replace("\n", "").split(" ")

        return [int(cow_val) for cow_val in cow_data]

    cow_constraint_list = process_line(in_file)
    return_cow_data.append(cow_constraint_list[0])

    if cow_constraint_list[1] > 0:
        return_cow_data.append(process_line(in_file))
    else:
        return_cow_data.append([])

    for i in range(cow_constraint_list[2]):
        return_cow_data.append(process_line(in_file))

    in_file.close()

    return return_cow_data

def calc_required_cow_order(cow_data):
    total_cows, cow_hiearchy, specific_cow_place = cow_data[0], cow_data[1], cow_data[2:]
    cow_placement = [0] * total_cows

    for cur_single_constraint in specific_cow_place:
        cur_cow_id = cur_single_constraint[0]
        cur_cow_index = cur_single_constraint[1] - 1
        cow_placement[cur_cow_index] = cur_cow_id
        
    return cow_placement, cow_hiearchy

def first_zero_index(cow_list):

    return cow_list.index(0)

def try_cow1_place(test_cow_placement, cow_hiearchy):
    test_cow_placement = test_cow_placement.copy()
    test_cow_placement[first_zero_index(test_cow_placement)] = 1
    cow_1_spot = test_cow_placement.index(1)
    success_flag = True
    
    for i in range(len(cow_hiearchy)):
        cur_cow_id = cow_hiearchy[i]
        if cur_cow_id not in test_cow_placement:
            test_cow_placement[first_zero_index(test_cow_placement)] = cur_cow_id
            if i != len(cow_hiearchy) - 1:
                if test_cow_placement.index(cur_cow_id) > test_cow_placement.index(cow_hiearchy[i + 1]):
                    success_flag = False
                    break

    return cow_1_spot, cur_cow_id, success_flag

def calc_acceptable_cow_order(required_cow_placement, cow_hiearchy):
    exit_flag = False
    while exit_flag == False:
        cow_1_spot, cur_cow_id, success_flag = try_cow1_place(required_cow_placement, cow_hiearchy)
        if success_flag == True:
            exit_flag = True
            break
        else:
            required_cow_placement[cow_1_spot] = cur_cow_id

    return cow_1_spot
        
def write_to_file(file_name, place_value):
    out_file = open(file_name, "w")
    out_file.write("{}\n".format(str(place_value)))
    out_file.close()

if __name__ == "__main__":
    cow_data = get_input("milkorder.in")
    print(cow_data)
    required_cow_placement, cow_hiearchy = calc_required_cow_order(cow_data)
    cow1_spot = calc_acceptable_cow_order(required_cow_placement, cow_hiearchy) + 1
    write_to_file("milkorder.out", cow1_spot)
    print(cow1_spot)