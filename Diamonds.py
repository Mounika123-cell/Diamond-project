import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
import random 


#Creation of banker class to create Diamond suit of 13 cards
class Banker:
    def __init__(self):
       		pass

    def create_diamond_suit(self):
        suit = "\u2666"
        
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        diamond_cards = [] 
        for value in values:
                diamond_cards.append((suit, value))
        return diamond_cards

#Creation of players class to create three different suit of 13 cards
class Players:
    def __init__(self, suit) :
        self.suit = suit
    
    def creating_suit(self) :
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        cards = [] 
        for value in values:
            cards.append((self.suit, value))
        return cards
        
def Shuffle(cards) :
    
    random.shuffle(cards)
    return cards
        
def Pop_cards(cards) :     
    return cards.pop()
 
#function to award points based on diamond card displayed  
def points_evaluation(card):
    
    value = card[1]
    numbers = [2,3,4,5,6,7,8,9,10]
    royals = ['J','Q','K']    
    if value in numbers:
         points = 3
    elif value in royals:
         points = 10
    else:
         points = 20
    return points


#finding the final winner using this function 
def final_winner(p1,p2,p3): 
    if p1 > p2:
        if p1 > p3:
        	print(Fore.YELLOW +"\n~~ WINNER IS ~~", player_1)
        elif p1 < p3:
        	print(Fore.YELLOW +"\n~~ WINNER IS ~~", player_3)
        else:
        	print(Fore.YELLOW +"\n~ THE GAME IS TIE BETWEEN ", player_1,"AND", player_3)
    elif  p2 > p3:
        if p2 > p1:
        	print(Fore.YELLOW +"\n~~ WINNER IS ~~", player_2)
        elif p2 < p1:
        	print(Fore.YELLOW +"~~ WINNER IS ~~", player_1)
        else:
        	print(Fore.YELLOW + "\n~ THE GAME IS TIE BETWEEN ", player_2 ,"AND", player_1)
    elif  p3 > p1:
        if p3 > p2:
        	print(Fore.YELLOW +"\n~~ WINNER IS ~~", player_3)
        elif p3 < p2:
        	print(Fore.YELLOW +"\n~~ WINNER IS ~~", player_2)
        else:
        	print(Fore.YELLOW +"\n~ THE GAME IS TIE BETWEEN ", player_3 ,"AND", player_2)
        		
    else :
        print(Fore.YELLOW +"\n~~ THE THREE PLAYERS SCORES EQUALLY ~~")
        print(Fore.YELLOW +"\n~~ WINNERS ARE ~~",player_1,player_2,player_3)


#giving scores to the player who won diamond in all rounds and appending their scores  

def player_scores():
    p1_score = 0
    p2_score = 0
    p3_score = 0
    for turn in range(1,14):
        print(Back.RED+'\n*| ROUND |*')
        print("*",turn,"*")
        print("\n")
        Shuffle(diamonds_list)
        diamond_card = Pop_cards(diamonds_list)
        print(Fore.CYAN + "|DISPLAYED DIAMOND CARD| : ", diamond_card)
        Shuffle(player1_list1)
        Shuffle(player2_list2)
        Shuffle(player3_list3)
     
        card1 = Pop_cards(player1_list1)
        card2 = Pop_cards(player2_list2)
        card3 = Pop_cards(player3_list3)
    
        print("\n*",player_1)
        input("Press any key to select your card : ")
        print("\n   %s card  : %s"%(player_1,card1))
        print("\n*",player_2)
        input("Press any key to select your card : ")
        print("\n   %s card  : %s"%(player_2,card2))
        print("\n*",player_3)
        input("Press any key to select your card : ")
        print("\n   %s card  : %s"%(player_3,card3))
        input("\n* Press ENTER to know the scores *")
   
        points = points_evaluation(diamond_card)
    
        player1 = []
        player2 = []
        player3 = []
        winners = card1   
        winner = card1[1]
    
        if winner < card2[1]:
            if card3[1] < card2[1]:
               winners = card2
               player2.append(points)
               print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~ ",player_2,winners)
               print(player_2,"Wins and get points",player2)
           
            
            elif card2[1] == card3[1]:
               winner1 = card2
               winner2 = card3
               player2.append(points//2)
               player3.append(points//2)
               print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_2,winner1,player_3,winner2)
               print(player_2 ,"and", player_3 ,"Wins and get points",player2,player3)
            else:
               winners = card3
               player3.append(points)
               print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_3,winners)
               print(player_3,"Wins and get points",player3)
         
        elif winner < card3[1]:
            winners = card3
            player3.append(points)
            print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_3,winners)
            print(player_3 ,"Wins and get points",player3)
    
        elif winner == card2[1]:
            if card2[1] < card3[1]:
                 winners = card3
                 player3 = player3.append(points)
                 print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_3,winners)
                 print(player_3,"Wins and get points",player3)
       
            winner1 = card1
            winner2 = card2
            player1.append(points//2)
            player2.append(points//2)
          
            print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_1,winner1,player_2,winner2)
            print(player_1 ,"and", player_2 ,"Wins and get points",player1,player2)
        
    
        elif winner == card3[1]:
            
             winner1 = card1
             winner2 = card3
             player1.append(points//2)
             player3.append(points//2)
             print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_1,winner1,player_3,winner2)
             print(player_1,"and",player_3,"Wins and get points",player1,player3)
        
    
        elif winner == card2[1] == card3[1]:
             winner1 = card1
             winner2 = card2
             winner3 = card3
             player1.append(points//3)
             player2.append(points//3)
             player3.append(points//3)
             print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_1,winner1,player_2,winner2,player_3,winner3)
             print(player_1,",",player_2,"and",player_3 ,"Wins and get points",player1,player2,player3)
        
        else:
      
             player1.append(points)
             print(Fore.CYAN + "\n~~ DIAMOND CARD WON BY ~~",player_1,winners)
             print(player_1 ,"Wins and get points",player1)
    
        p1_score = p1_score + sum(player1)
        p2_score = p2_score + sum(player2)
        p3_score = p3_score + sum(player3)
    
        print(Fore.GREEN + "\n\nAFTER ROUND %d THE PLAYERS SCORES : \n%s : %d\n%s : %d\n%s : %d"%(turn,player_1,p1_score,player_2,p2_score,player_3,p3_score)) 
        key = input("\nPress any key to enter next round (or) To stop enter \'quit\' : ")
        if key == 'quit':
            break        
    final_winner(p1_score,p2_score,p3_score)
    
print(Fore.YELLOW+"\n **WELCOME TO DIAMONDS CARD GAME**")
print(Fore.CYAN+"\n       *PLAYER  DETAILS*\n")
player_1 = (Fore.MAGENTA + str(input("ENTER PLAYER 1 NAME : ")))
player_2 = (Fore.MAGENTA + str(input("ENTER PLAYER 2 NAME : ")))
player_3 = (Fore.MAGENTA + str(input("ENTER PLAYER 3 NAME : ")))

banker = Banker()
diamonds_list = banker.create_diamond_suit()

player1 = Players("\u2660")
player1_list1 = player1.creating_suit()

player2 = Players("\u2665")
player2_list2 = player2.creating_suit()

player3 = Players("\u2663")
player3_list3 = player3.creating_suit()

player_scores()

while (True):
    result = input("\nDO YOU WANT TO PLAY THIS GAME AGAIN yes/no : ")

    if result == 'yes':
        print(Fore.YELLOW+"\n**WELCOME TO DIAMONDS CARD GAME**")
        print(Fore.CYAN+"\n       *PLAYER  DETAILS*\n")
        player_1 = (Fore.MAGENTA + str(input("ENTER PLAYER 1 NAME : ")))
        player_2 = (Fore.MAGENTA + str(input("ENTER PLAYER 2 NAME : ")))
        player_3 = (Fore.MAGENTA + str(input("ENTER PLAYER 3 NAME : ")))

        banker = Banker()
        diamonds_list = banker.create_diamond_suit()

        player1 = Players("\u2660")
        player1_list1 = player1.creating_suit()

        player2 = Players("\u2665")
        player2_list2 = player2.creating_suit()

        player3 = Players("\u2663")
        player3_list3 = player3.creating_suit()

        player_scores()
    else :
        break
