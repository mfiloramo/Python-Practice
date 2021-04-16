def show_list(items_list):
    """This function simply prints the items on a list, along with an intro."""
    for items in items_list:
        print(f"This item is named {items}.")


def make_new(items_list):
    """This function uses only one parameter to both transfer and print items on
    a list."""
    while items_list:
        transferred_item = items_list.pop()
        print(f"The item that's being transferred is {transferred_item}.")
        new_items.append(transferred_item)
    for items in new_items:
        print(f"Behold, this new item, which is {items}!")


def make_new_2(its, new_its):
    """This function takes on a different approach to transferring list items.
    Not only does it take a slice [:] from the original list, but it also
    takes two different parameters, both lists."""
    while its:
        examined = "The new " + its.pop()
        new_its.append(examined)
    print(f"The new items are now {new_its}.")
    print(f"But don't worry! They all started as {items}.")


items = ["Moe", "Larry", "Curly"]
new_items = []

#  You can toggle on/off the function calls below to play with the listed functions, respectively.

# show_list(items)
# make_new(sorted(items))
# make_new_2(items[:], sorted(new_items))

#  Notice I slice the items list in the third call to maintain the original for reference.
