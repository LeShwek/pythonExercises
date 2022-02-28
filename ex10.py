def get_card():

    is_passed = False

    while not is_passed:
        card = input("Enter a card: ")
        if card.isnumeric() == False:
            continue
        elif int(card) < 1 or int(card) > 13 and int(card) != 999:
            continue
        else:
            is_passed = True

    return card


def turn():

    sums = 0
    card1 = get_card()
    card1 = int(card1)
        
    while card1 != 999:

        sums += card1
        print(sums)
        if sums > 21:
            return sums
        
        card1 = get_card()
        card1 = int(card1)

    return sums
        
        
        



def main():

    won = "0"
    sum1 = 0
    sum2 = 0
    
    while won == "0":

        print("player 1's turn")
        sum1 = turn()

        if sum1 > 21:
            print("player 2 wins")
            break

        print("player 2's turn")
        sum2 = turn()

        if sum2 > 21:
            print("player 1 wins")
            break

        if sum1 > sum2:
            print("player 1 wins")
            won = "1"
        elif sum2 > sum1:
            print("player 2 wins")
            won = "2"
        else:
            print("its a tie!")

    print("good game")
        
        

            
            
            
    
if __name__ == "__main__":
    main()
