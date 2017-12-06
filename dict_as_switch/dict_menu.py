#/usr/bin/env python

"""
dispatch dict example
"""


def menu_selection(prompt, dispatch_dict):

    while True:  # loop forever until they quit.
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


def fun1():
    print("You selected the first Option!")


def fun2():
    print("You selected the second Option!")


def fun3():
    print("You selected the third Option!")


def fun4():
    print("You selected the fourth Option!")

def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    print("Quitting this menu now")
    return "exit menu"



main_prompt = ("\nYou are in the main menu now!!!\n"
               "What do you want to do?\n"
               "Type 1,2,3,4 or 5 to get a submenu.\n"
               " or q to exit >> "
               )
main_dispatch = {"1": fun1,
                 "2": fun2,
                 "3": fun3,
                 "4": fun4,
                 "5": sub_menu,
                 "q": quit,
                 }

sub_prompt = ("\nYou are in a sub-menu now!!!\n"
              "What do you want to do?\n"
              "Type 1,2,3, or 4. or q to exit >> "
              )
sub_dispatch = {"1": fun1,
                "2": fun2,
                "3": fun2,
                "4": fun2,
                "q": quit,
                }


if __name__ == "__main__":

    # let's try a couple menu selections:
    menu_selection(main_prompt, main_dispatch)


