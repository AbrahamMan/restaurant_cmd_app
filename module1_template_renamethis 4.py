# Module 1 Assignment: San Tayo Kakain App
# by: [Your Last Name], [First Name]
import random

def open_file_and_get_content(filename):
    content = open(filename, 'r') #"TODO: Fill in to get content string from file"
    content = file.readlines(content)
    return content


def convert_string_to_restaurant_list(content):
    restaurant_list = []
    for i in content: 
        restaurant = {}
        value = i.replace('\n','').split(',');
        restaurant["restaurant"] = str(value[0].strip('"'))
        restaurant["visited"] = "Y" in value[1]
        restaurant_list.append(restaurant )#{"retaurant": "TODO: fill in to append all restaurants", "visited": False})
    return restaurant_list


def pick_random_resto(restaurant_obj_list):
    filtered_restaurant = [rest for rest in restaurant_obj_list if not rest['visited']]
    selected = random.choice(filtered_restaurant)
    print("Restaurant pick: " + selected["restaurant"] )
    #print("TODO: Fill in to pick a random restaurant you haven't visited")


def show_restaurants(restaurant_obj_list):
    sortedRest = sorted(restaurant_obj_list, key = lambda s:  s['restaurant'].lower())
    for i, rest in enumerate(sortedRest): 
        visited = " (Visited)" if rest["visited"] else " (Not Yet Visited)" 
        print str(i + 1) + ". " +  rest["restaurant"] + str(visited)
    # print("TODO: Fill in show restaurants in proper output format in the instructions")


def mark_restaurant_visited(restaurant_obj_list):
    try:
        sortedRest = sorted(restaurant_obj_list, key = lambda s:  s['restaurant'].lower())
        choice = raw_input("Enter the restaurant number: ")
        sortedRest[int(choice)]["visited"] = True
        #print("TODO: Fill in to mark the choice", choice, "visited")
    except:
        print "Invalid restaurant number."


def press_key_to_continue():
    raw_input("Press enter key to continue..")


def main():
    file_content = open_file_and_get_content('sample_resto_input.txt')
    print("File are: ", file_content)
    restaurant_obj_list = convert_string_to_restaurant_list(file_content)

    while True:
        print("""
=======================
  San Tayo Kakain App
=======================

(1) Pick a Random Restaurant You Haven't Visited
(2) Show All Restaurants
(3) Mark Restaurant as Visited
(4) Exit
""")

        choice = raw_input("Enter choice: ")
        choice = str(choice)

        if choice == "4":
            print("Thank you for using the app, you beautiful person you! Have a nice day!")
            break
        elif choice == "3":
            mark_restaurant_visited(restaurant_obj_list)
            press_key_to_continue()
        elif choice == "2":
            show_restaurants(restaurant_obj_list)
            press_key_to_continue()
        elif choice == "1":
            pick_random_resto(restaurant_obj_list)
            press_key_to_continue()
        else:
            print("Invalid choice")
            press_key_to_continue()
        # end if choice
    # end while True


main()
