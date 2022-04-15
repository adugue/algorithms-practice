graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[0] == 'j'  # if the person's name ends with an 'm', it is a mango seller

# creation of double-ended queue:
# -> queue: a queue is a data structure that follows the First In First Out rule (FIFO). In this case, elements can only be added to the back of the queue (enqueue), and not at the front. Elements of the queue can only be removed from the front (dequeue).
# -> adding an item in the queue is called "enqueue" and removing from the queue is called "dequeue"
# -> double-ended queue (abbreviated to "deque" and pronounced "deck"): a type of queue where elements can be added to or removed from either the front (head) or back (tail). (often called a "head-tail linked list", though properly this refers to a specific data structure implementation of deque.

from collections import deque

def search(name):
    search_queue = deque()  # create an empty double-ended queue
    search_queue += graph[name] # add all the neighbors of "you" to the search queue
    searched = []
    
    while search_queue:  # while the queue isn't empty
        person = search_queue.popleft()  # grab the first person off the queue
        print(searched)
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")
