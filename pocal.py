#dependencies
import math

op_list = ['0','9']

def dig_check(x):
    
    if x in op_list:
        return x
    else:
        return False

def card_check(x):

    y = create_deck()
    
    if x in y:
        return x
    else:
        return False

def create_deck():
    
    ranks = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
    suits = ['c','d','h','s']

    deck = [ rank + suit for rank in ranks for suit in suits]

    return deck

def main():

    u_in = input("please choose an option by typing the corresponding number\n----------------------------------------------------------\n0) calculate pre-flop odds\n9) exit the poker probability calc\n")

    while dig_check(u_in) == False:
        u_in = input("invalid input, please try again\n")

    if dig_check(u_in) == '9':
        exit()

    if dig_check(u_in) == '0':
        
        c_1 = input("please enter a card in the form <value><suite> with lowercase letters\n")

        while card_check(c_1) == False:
            c_1 = input("invalid input, please try again\n")

        c_2 = input("please enter another card in the form <value><suite> with lowercase letters\n")

        while card_check(c_2) == False:
            c_2 = input("invalid input, please try again\n")

        #logic about odds goes here

        #odds of getting various hands on the flop

        flop_perm = math.comb(50,3)

        if c_1[0] == c_2[0]:
            
            flop_atl_pair = 1


            
            flop_no3kind = math.comb(48,3)
            flop_3kind_amt = flop_perm - flop_no3kind
            flop_atl_3kind = flop_3kind_amt/flop_perm

            flop_atl_4kind = 49/flop_perm

        else:
            
            flop_nopair = math.comb(44,3)
            flop_pair_amt = flop_perm - flop_nopair
            flop_atl_pair = flop_pair_amt/flop_perm

        print(f"pair: {flop_atl_pair}, 3 of a kind: {flop_atl_3kind}, 4 of a kind: {flop_atl_4kind}")

        #odds of getting various hands after the river
        #odds of getting various hands after the turn

        

        u_yn = input("would you like to do anything else? please enter 'y' or 'n'\n")

        while u_yn not in {'y','n'}:
            u_yn = input("invalid input, please try again\n")

        else:
            if u_yn == 'y':
                main()
            else:
                exit()

    else:
        print("check why program got here")
        exit()

if __name__ == '__main__':
    main()