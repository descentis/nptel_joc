# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:49:52 2018

Rock Paper Scissor
@author: Descentis
"""

'''
Player 1's information
'''
# 0 is for Rock
# 1 is for Paper
# 2 is for Scissor
player_one = {0:'Rock',1:'Paper',2:'Scissor'}
done=False
while(done):
	bit1=int(input('Player1! Enter your position : 1 for 1st digit, 2 for 2nd digit, 3 for 3rd digit'))
	if bit1>0 and bit1<4:
		bit1=bit1-1
	bit2=int(input('Player2! Enter your position : 1 for 1st digit, 2 for 2nd digit, 3 for 3rd digit'))
	if bit2>0 and bit2<4:
		bit2=bit2-1
		if bit1==bit2:
			print('Please give another choice')
			continue
		done=True
#bit1 = 2 
#bit1 = 2 
# bit from the left. Assuming that the leftmost bit is 0th bit

'''
Player 2's information
'''
# 2 is for Rock
# 0 is for Paper
# 1 is for Scissor
player_two = {0:'Paper',1:'Scissor',2:'Rock'}
#bit2 = 1 
# bit from the left. Assuming that the leftmost bit is 0th bit

def rock_paper_scissor(num1,num2):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("!!Draw!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("!!Player One Wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("!!Player Two Wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("!!Player One Wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("!!Player Two Wins!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("!!Player One Wins!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("!!Player Two Wins!!")

while(True):
	num1 = input("Player One, enter your choice: ")
	num2 = input("Player Two, enter your choice: ")
	rock_paper_scissor(num1,num2)
	ch = input("Do you want to continue? (y/n)")
	if(ch=='n'):
		break;

