max_tries=10
no_guesses=0


word = "vishnu"
l=word.lower()
print(l)


while True:
  key=input("guess letter: ")
  if key in word:
    print(word+ " contains "  +key)
    word=word.replace(key,"")
    print(len(word))
    if len(word)==0:
       print("you win")
       break
  else:
    print("wrong") 
    no_guesses=no_guesses+1
    if no_guesses>=max_tries:
       print("you lost") 
       break
    
    
  