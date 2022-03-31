# def greet(name, time_of_day):
#     words = "Hey"
#     return words
#     #return "Hello " + name + "Time is " + time_of_day

# def greet_two():
#     return words

# name_1 = "Bob "
# time_of_day = "Morning"
# greeting = greet(name_1, time_of_day)
# print(greeting)

# name_2 = "Eric "
# time_of_day_2 = "Afternoon"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)


chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs(list):
    total_eggs = 0
    for banana in list:
        total_eggs += banana["eggs"]

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))

# total_eggs = 0

# for chicken in chickens:
#     total_eggs += chicken["eggs"]
#     chicken["eggs"] = 0 # eggs have been collected

# print(f"{total_eggs} eggs collected")