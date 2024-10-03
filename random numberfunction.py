import random
# choice() function
print("random number from range(100) :",random.choice(range(100)))

list=[1,5,8,3,7]
print("random element from list :",random.choice(list))

str="vishnu"
print("random charcter from string :",random.choice(str))


#randrange() function
print("randrange(100) :",random.randrange(100))
print("randrange(1,50,2) :",random.randrange(1,50,2))

#random() function
# first random number
print("random() :",random.random())

# second random number
print("random() :",random.random())


#seed() function
random.seed()
print("random number with default seed",random.random())

random.seed(50)
print("random number with int seed",random.random())

random.seed("vishnu",3)
print("random number with string seed",random.random())


#shuffle() function
list=[1,53,35,73,97,8,32,46]
random.shuffle(list)
print("shuffled list is : ",list)

random.shuffle(list)
print("Reshuffled list is : ",list)


#uniform() function
print("random float uniform : ",random.uniform(1,15))
print("random float uniform : ",random.uniform(20,50))