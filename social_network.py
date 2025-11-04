class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(name, friends):
        name.name = friends
        name.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(people):
        people.names = {}

    def add_person(people, name):
        if name not in people.names:
            people.names[name] = Person(name)
        else:
            print(f"{name} already exists!")


    def add_friendship(people, person1_name, person2_name):
        if person1_name in people.names and person2_name in people.names:
            person1 = people.names[person1_name]
            person2 = people.names[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print(f"Error: One or both people don't exist!!")

    def print_network(people):
        for person_name, person_obj in people.names.items():
            friendship_names = [p.name for p in person_obj.friends]
            connected_names = ", ".join(friendship_names)
            print(f"{person_name} is friends with: {connected_names}")

# Test your code here

# test class
jack = Person("Jack")
print(jack.name)
huck = Person("Huck")
jack.add_friend(huck)
print(jack.friends[0].name)
 
# test network
network = SocialNetwork()
network.add_person("Steven")
network.add_person("Carol")
network.add_person("Marv")
network.add_person("Justin")
network.add_person("Max")
network.add_person("Alex")


network.add_friendship("Steven", "Marv")
network.add_friendship("Carol", "Marv")
network.add_friendship("Alex", "Justin")
network.add_friendship("Alex", "Marv")
network.add_friendship("Steven", "Max")
network.add_friendship("Max", "Carol")
network.add_friendship("Justin", "Alex")
network.add_friendship("Justin", "Max")
network.add_friendship("Steven", "DNE") # Error message
network.add_friendship("Marv", "Max")

network.add_person("Carol") # Carol already exists

network.print_network()


'''
Design memo:
Why is a graph the right structure to represent a social network?
Why wouldn’t a list or tree work as well for this?
What performance or structural trade-offs did you notice when adding friends or printing the network?

A graph is the ideal structure for a social network because it is a natural
representation of a social network, for instance, people would be nodes
and friendships as edges. This is beneficial for many to many relationships
where in a social network this would be the case and highlights mutual connections
Graphs also allow bidirectional relationships between friends, which shows
the mutual connections. A list would take too long to locate someones friends as
it would have to scan an entire friendship list, and due to the social networks 
complexity, it would be difficult for a tist to traverse the network.
A tree would impose a hierarchy that does not exist in a social network
they only allow one path between nodes also known as eople, where a social network
should have multiple connections. Trees cannot show bidirectional relationships needed
to be represented in a social network.
Performance and sturctural trade-offs I noticed when adding friends and 
printing the network were space and time issues, my approach is faster
at bidirectional lookups because it stores friendships twice. The duplicate prevention
had to be added in at the end and I considered a set but the friends are not hashable
the scalability issue would come from the list becoming more expensive as it would require
more elements to be scanned
'''