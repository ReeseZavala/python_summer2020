# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:29:19 2020

@author: rzava
"""

import random as ra
import time

#define class Portfolio
class Portfolio():

    
    
    def __init__(self, cash = 0.00, stocks = {}, mf = {}): #initialize Portfolio, setting cash default to 0
        #setting definitions of instances
        self.cash = cash
        self.stocks = stocks
        self.mf = mf      
        self.disHis = []
       
    #def __repr__(self): #setting value for repr, even though I shouldn't have to, but it's not working with just str
        #return "Cash: " + str(self.cash) + "\n" + "Stocks: " + str(self.stocks) + "\n" + "Mutual Funds: " + str(self.mf) 
        
    def __str__(self):#initializing print value
        return "Cash: " + str(self.cash) + "\n" + "Stocks: " + str(self.stocks) + "\n" + "Mutual Funds: " + str(self.mf)
    
    def addcash(self, newFunds): 
        #adding funds to cash, then replacing 
        self.cash += newFunds
        return self

    def withdrawcash(self, newFunds): 
        #subtracting funds from cash, then replacing
        if newFunds > self.cash:
            print("In your dreams buddy.")
        else:
            self.cash -= newFunds
            return self
    
    def buystock(self, howMuch, witchStock):
        if howMuch * witchStock.price > self.cash: #prevent overdrafting
            print("You broke, broke dummy, you cannot purchase.")
        elif witchStock.name in self.stocks.keys(): #updating entry if already stock in portfolio
            self.withdrawcash(howMuch * witchStock.price)
            self.stocks[witchStock.name] += howMuch 
            #taking stocks dict entry and updating it by new purchase 
            self.disHis.append("Bought " + str(howMuch) + "shares of " + str(witchStock.name) + " " + time.asctime())
            #Adding transaction to history
            return self
        else:   #adding new stock
            self.withdrawcash(howMuch * witchStock.price)
            self.stocks[witchStock.name] = howMuch
            self.disHis.append("Bought " + str(howMuch) + "shares of " + str(witchStock.name) + " " + time.asctime())
            #Adding transaction to history
            return self
    
    def buymutualfund(self, howMuch, witchFund):
        if howMuch * witchFund.price > self.cash: #preventing overdraft 
            print("You poor, broke dummy, you cannot purchase.  Sad.")
        elif witchFund.name in self.mf.keys():
            #withdrawing funds, then updating number of funds in mf dict
            self.withdrawcash(howMuch * witchFund.price)            
            self.mf[witchFund.name] += howMuch     
            self.disHis.append("Bought " + str(howMuch) + "shares of " + str(witchFund.name) + " " + time.asctime())
            #Adding transaction to history
            return self
        else: #adding new fund
            self.withdrawcash(howMuch * witchFund.price)
            self.mf[witchFund.name] = howMuch
            self.disHis.append("Bought " + str(howMuch) + "shares of " + str(witchFund.name) + " " + time.asctime())
            #Adding transaction to history
            return self
    
    def sellmutualfund(self, howMuch, witchFund):
        price = round(ra.uniform(.9,1.2), 2) #define price in unif dist
        if howMuch > self.mf[witchFund.name]: #prevent selling too much stock
            print("You want so much, but have so little...")
        elif self.mf[witchFund.name] == howMuch:#deleting fund when all sold
            self.addcash(howMuch * price)#updating cash 
            del self.mf[witchFund.name]
            self.disHis.append("Sold " + str(howMuch) + "shares of " + str(witchFund.name) + " " + time.asctime())
            #Adding transaction to history
        else:#standard transaction
            self.addcash(howMuch * price)
            self.mf[witchFund.name] -= howMuch
            self.disHis.append("Sold " + str(howMuch) + "shares of " + str(witchFund.name) + " " + time.asctime())
            #Adding transaction to history
    
    def sellStock(self, howMuch, witchStock):
        #define price in range of unif dist
        price = round(ra.uniform(witchStock.price * .5, witchStock.price * 1.5), 2)
        if howMuch > self.stocks[witchStock.name]: #preventing selling stock you don't have
            print("Capitalism does not favor the poor.")
        elif self.stocks[witchStock.name] == howMuch: #Deleting entry when all stocks sold
           self.addcash(howMuch * price) #update cash value
           del self.stocks[witchStock.name]
           self.disHis.append("Sold " + str(howMuch) + "shares of " + str(witchStock.name) + " " + time.asctime())
            #Adding transaction to history
        else:
            self.addcash(howMuch * price) #simple transaction
            self.stocks[witchStock.name] -= howMuch    
            self.disHis.append("Sold " + str(howMuch) + "shares of " + str(witchStock.name) + " " + time.asctime())
            #Adding transaction to history
    
    def history(self):
        print(*self.disHis, sep="\n")
        
        
        
class Stock():
    #defining class Stock() with attributes price and name
    def __init__(self, price, name):
        self.price = price
        self.name = name

class mutualFund():
    #defining class mutualFund() with attributes price and name
    def __init__(self, name):
        self.price = 1.0
        self.name = name


#create portfolio
OhBoy = Portfolio(cash = 1000)

#money infusion
OhBoy.addcash(500)
OhBoy.withdrawcash(5000000)#return error
OhBoy.withdrawcash(500)
print(OhBoy)

#generate stocks and funds
F = Stock(10, "Ford")
KO = Stock(5, "Coke")
BBB = mutualFund("Funerd")
BBA = mutualFund("Fund")

#buying functions
OhBoy.buymutualfund(500, BBA)
OhBoy.buymutualfund(100, BBB)
OhBoy.buystock(20, KO)
OhBoy.buystock(20, F)
OhBoy.buymutualfund(10000, BBB) #error message
OhBoy.buystock(100000, F) #error essage

#print to check progress
print(OhBoy) #print full portfolio

#selling functions
OhBoy.sellStock(5000, KO) #error message
OhBoy.sellmutualfund(500000, BBB) #error message
OhBoy.sellStock(10, KO)
OhBoy.sellStock(20, F)#clear this stock
OhBoy.sellmutualfund(200, BBA)
OhBoy.sellmutualfund(100, BBB) #clear this fund

#printing
OhBoy.history() #print transactions
print(OhBoy)#view updated portfolio
