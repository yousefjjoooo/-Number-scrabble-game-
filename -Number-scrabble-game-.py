# File : CS112_A1_T2_Game2_20230491
"""
# Purpose : The game is played with the list of numbers between 1 and 9. Each player takes 
turns picking a number from the list. Once a number has been picked, it cannot be picked 
again. If a player has picked three numbers that add up to 15, that player wins the game. 
However, if all the numbers are used and no player gets exactly 15, the game is a draw.
"""
# Author : Youssef Hossam Morsy Abdo
# ID : 20230491


valid_numbers=[1,2,3,4,5,6,7,8,9]
def is_there_a_string(value):
      while True:
            if(value.isdigit() ) and int(value) in valid_numbers:
                return value
                
            else:
                  value= input("Please, enter a positive intger number!")

# Welcoming message for players
print("Hello! Welcome to Number scrabble game!")

# Asking the players for their names
first_player_name= str(input("Enter a name for first player"))
second_player_name= str(input("Enter a name for second player"))
valid_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(" 1, 2, 3, 4, 5, 6, 7, 8 and 9 are the valid numbers!")

# This loop is important to ensure that the program will print a draw message if it is not broken before line 228
while True:
     
     # This loop ensures that the number which the player entered is valid
     while True:
        A = int(is_there_a_string(input(first_player_name +", please, choose your first number ")))
        
        # Asking the player to try again
        if A not in valid_numbers:
             print("Please enter a valid number") 
        
        # Printing the number that the player has
        if A in valid_numbers:
             print("Now, ", first_player_name, " has ", A)
             break
     
     # This loop ensures that the number which the player entered is valid and that the number is not choosen before
     while True:    
        B = int(is_there_a_string(input(second_player_name +", please, choose your first number ")))
        
        # Asking the player to try again
        if B not in valid_numbers:
             print("Please enter a valid number") 
        if B==A :
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the number that the player has
        if B in valid_numbers and B!=A:
             print("Now, ", second_player_name, " has ", B)
             break
     

     # This loop ensures that the number which the player entered is valid and that the number is not choosen before
     while True:
        C = int(is_there_a_string(input(first_player_name +", please, choose your second number ")))
        
        # Asking the player to try again
        if C not in valid_numbers:
             print("Please enter a valid number") 
        if C==A or C==B :
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if C in valid_numbers and C!=A and C!=B:
             print("Now, ", first_player_name, " has ", C ," and ",A)
             break
     

     # This loop ensures that the number which the player entered is valid and that the number is not choosen before
     while True:    
        D = int(is_there_a_string(input(second_player_name +", please, choose your second number ")))
        
        # Asking the player to try again
        if D not in valid_numbers:
             print("Please enter a valid number") 
        if D==A or D==B or D==C:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if D in valid_numbers and D!=A and D!=B and D!=C:
             print("Now, ", second_player_name, " has ", D, " and ", B)
             break


     # This loop ensures that the number which the player entered is valid and that the number is not choosen before 
     while True:    
        E = int(is_there_a_string(input(first_player_name +", please, choose your third number ")))
        
        # Asking the player to try again
        if E not in valid_numbers:
             print("Please enter a valid number") 
        if E==A or E==B or E==C or E==D:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if E in valid_numbers and E!=A and E!=B and E!=C and E!=D:
             print("Now, ", first_player_name, " has ", C ,", ",A, " and ", E)
             break
     
     # Now, if the first player entered 3 numbers of sum 15, then wins
     if A +C +E ==15:
            print(first_player_name, "is the winner!")
            break
       
     # This loop ensures that the number which the player entered is valid and that the number is not choosen before       
     while True:  
        F = int(is_there_a_string(input(second_player_name +", please, choose your third number ")))
        
        # Asking the player to try again
        if F not in valid_numbers:
             print("Please enter a valid number") 
        if F==A or F==B or F==C or F==D or F==E:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if F in valid_numbers and F!=A and F!=B and F!=C and F!=D and F!=E:
             print("Now, ", second_player_name, " has ", D, ", ", B, " and ", F)
             break


     # Now, if the second player entered 3 numbers of sum 15 before the the first does, then wins   
     if B + D + F ==15:
            print(second_player_name, "is the winner!")
            break


     # This loop ensures that the number which the player entered is valid and that the number is not choosen before           
     while True:   
        G = int(is_there_a_string(input(first_player_name +", please, choose your fourth number ")))
        
        # Asking the player to try again
        if G not in valid_numbers:
             print("Please enter a valid number") 
        if G==A or G==B or G==C or G==D or G==E or G==F:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if G in valid_numbers and G!=A and G!=B and G!=C and G!=D and G!=E and G!=F:
             print("Now, ", first_player_name, " has ", C ,", ",A, ", ", E, " and ", G)
             break


     # Now, the first one added 4 number. If any 3 of the 4 can be added to reach 15, then the first wins 
     if A +C+G==15:
             print(first_player_name, "is the winner!")
             break
     if C+E+G==15:
             print(first_player_name, "is the winner!")
             break
     if A+E+G==15:
             print(first_player_name, "is the winner!")
             break
     

     # This loop ensures that the number which the player entered is valid and that the number is not choosen before
     while True:
        H = int(is_there_a_string(input(second_player_name +", please, choose your fourth number ")))
        
        # Asking the player to try again
        if H not in valid_numbers:
             print("Please enter a valid number") 
        if H==A or H==B or H==C or H==D or H==E or H==F or H==G:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if H in valid_numbers and H!=A and H!=B and H!=C and H!=D and H!=E and H!=F and H!=G:
             print("Now, ", second_player_name, " has ", D, ", ", B, ", ", F, " and ", H)
             break
        
     
     # Now, the second one added 4 number. If any 3 of the 4 can be added to reach 15, then the second wins
     if F +D+H==15:
             print(second_player_name, "is the winner!")
             break
     if B+D+H==15:
             print(second_player_name, "is the winner!")
             break
     if B+F+H==15:
             print(second_player_name, "is the winner!")
             break      
     

     # This loop ensures that the number which the player entered is valid and that the number is not choosen before
     while True:  
        I = int(is_there_a_string(input(first_player_name +", please, choose your fifth number ")))
        
        # Asking the player to try again
        if I not in valid_numbers:
             print("Please enter a valid number") 
        if I==A or I==B or I==C or I==D or I==E or I==F or I==G or I==H:
             print("This number is already choosen! Please, select another one")
        
        
        # Printing the numbers that the player has
        if I in valid_numbers and I!=A and I!=B and I!=C and I!=F and I!=G and I!=H and I!=E and I!=D:
             print("Now, ", first_player_name, " has ", C ,", ",A, ", ", E, ", ", G, " and ", I)
             break


     # Now, the first one added 5 number. If any 3 of the 5 can be added to reach 15, then the first wins.   
     if I +C+G==15:
             print(first_player_name, "is the winner!")
             break
     if I+E+G==15:
             print(first_player_name, "is the winner!")
             break
     if A+E+I==15:
             print(first_player_name, "is the winner!")
             break
     if A +I+G==15:
             print(first_player_name, "is the winner!")
             break
     if C+E+I==15:
             print(first_player_name, "is the winner!")
             break
     if A+I+C==15:
             print(first_player_name, "is the winner!")
             break
     
     # If none of them reached 15, then the game is a draw
     print("The game is a draw!")
     break