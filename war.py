
suits=['hearts','diamonds','spades','clubs']
ranks=['two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen']
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14}

# each car is described by suit and rank

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
import random


class Deck:

    def __init__(self):
        self.all_cards=[]

        for suit in suits:
            for rank in ranks:

                created_card=Card(suit,rank)

                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
         return self.all_cards.pop()


class Player:

    def __init__(self,name):

        self.name=name
        self.player_cards=[]

    def add_card(self,new_card):
        if type(new_card)== type([]):
             self.player_cards.extend(new_card)
        else:
             self.player_cards.append(new_card)


    def remove_card(self):
        return self.player_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'



## Game setup
#creat a deck of 52 cards
new_deck=Deck()

#create a player1 and player2

player_one=Player('one')
player_two=Player('two')

#shuffle the deck of cards
new_deck.shuffle()

#deal the shuffled cards between the two player

for i in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

# drawing the top cards from the deck for each player to play



game_on= True
count=0

while game_on:

    count+=1
    print(f'round{count}!')


    if len(player_one.player_cards)==0:
        print('player_one do not have enough cards!')
        print('player_two Wins!!')
        game_on=False
        break

    if len(player_two.player_cards)==0:
        print('player_two does not have enough cards!')
        print('player_one Wins!!')
        game_on=False
        break


    # drawing cards from each player deck
    player_one_draw=[]
    player_two_draw=[]
    player_one_draw.append(player_one.remove_card())
    player_two_draw.append(player_two.remove_card())

    at_war=True
    while at_war:

        if player_one_draw[-1].value > player_two_draw[-1].value:
           player_one.add_card(player_one_draw)
           player_one.add_card(player_two_draw)
           at_war=False

        elif player_one_draw[-1].value < player_two_draw[-1].value:
            player_two.add_card(player_one_draw)
            player_two.add_card(player_two_draw)
            at_war=False

        else:
            print('war!')

            if len(player_one.player_cards)<5:

                print('player_one unable to declare war,dont have enough cards!')
                print('player_two Wins!!')
                game_on=False
                break


            elif len(player_two.player_cards)<5:
                print('player_two unable to declare war,dont have enough cards!')
                print('player_one Wins!!')
                game_on=False
                break

            else:
                  for i in range(5):
                      player_one_draw.append(player_one.remove_card())
                      player_two_draw.append(player_two.remove_card())
