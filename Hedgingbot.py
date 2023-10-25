import MetaTrader5 as mt 
import pandas as pd  
import plotly.express as px  
from datetime import datetime
import time
import os


mt.initialize()


def start():
    account_info = mt.account_info()
    balance_previous = account_info.balance
    print(balance_previous)
    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": "EURUSDm",
        "volume": 0.1,
        "type": mt.ORDER_TYPE_BUY,
        "price": mt.symbol_info_tick("EURUSDm").ask,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }
     
    # send a trading request
    result = mt.order_send(request)
    print(result)
    print(result.price)
    print(result.order)
    
    modify_request = {
        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
        "symbol": "EURUSDm",
        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
        "sl": result.price-0.00030,  # New stop loss level
        "tp": result.price+0.00050,  # New take profit level
        "position": result.order,
        "magic": 234000,
        "comment": "python script open", # Use the ticket number of the order you want to modify
    }
    
    # Send the trade request to modify SL and TP
    modify_result = mt.order_send(modify_request)
    modify_result
    
    flag=False
    while True:
       num_positions = mt.positions_total()
       num_positions
       
       if num_positions == 0:
           flag=True
           break
       
    sl=0
    tp=0
    num_positions = mt.positions_total()
    num_positions
    if num_positions==0:
        account_info = mt.account_info()
        balance_new = account_info.balance
        print(balance_new)
        if balance_new>balance_previous:
            tp=tp+1   
        else:
            sl=sl+1
            
    
    if flag==True:
            if sl==1:
                request = {
                "action": mt.TRADE_ACTION_DEAL,
                "symbol": "EURUSDm",
                "volume": 0.2,
                "type": mt.ORDER_TYPE_SELL,
                "price": mt.symbol_info_tick("EURUSDm").ask,
                "magic": 234000,
                "comment": "python script open",
                "type_time": mt.ORDER_TIME_GTC,
                "type_filling": mt.ORDER_FILLING_IOC,
                }
             
                result = mt.order_send(request)
                print(result)
                print(result.price)
                print(result.order)
                modify_request = {
                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                "symbol": "EURUSDm",
                "price": mt.symbol_info_tick("EURUSDm").ask,  # Use the current ask price
                "sl": result.price+0.00030,  # New stop loss level
                "tp": result.price-0.00050,  # New take profit level
                "position": result.order,
                "magic": 234000,
                "comment": "python script open", # Use the ticket number of the order you want to modify
                }
                modify_result = mt.order_send(modify_request)
                modify_result


                flag=False
                while True:
                   num_positions = mt.positions_total()
                   num_positions
                   
                   if num_positions == 0:
                       flag=True
                       break
                   
                sl=0
                tp=0
                num_positions = mt.positions_total()
                num_positions
                if num_positions==0:
                    account_info = mt.account_info()
                    balance_new = account_info.balance
                    print(balance_new)
                    if balance_new>balance_previous:
                        tp=tp+1   
                    else:
                        sl=sl+1

                if flag==True:
                    if sl==1:
                        request = {
                        "action": mt.TRADE_ACTION_DEAL,
                        "symbol": "EURUSDm",
                        "volume": 0.3,
                        "type": mt.ORDER_TYPE_BUY,
                        "price": mt.symbol_info_tick("EURUSDm").ask,
                        "magic": 234000,
                        "comment": "python script open",
                        "type_time": mt.ORDER_TIME_GTC,
                        "type_filling": mt.ORDER_FILLING_IOC,
                        }
                     
                        result = mt.order_send(request)
                        print(result)
                        print(result.price)
                        print(result.order)
                        modify_request = {
                        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                        "symbol": "EURUSDm",
                        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                        "sl": result.price-0.00030,  # New stop loss level
                        "tp": result.price+0.00050,  # New take profit level
                        "position": result.order,
                        "magic": 234000,
                        "comment": "python script open", # Use the ticket number of the order you want to modify
                        }
                        modify_result = mt.order_send(modify_request)
                        modify_result

                        flag=False
                        while True:
                           num_positions = mt.positions_total()
                           num_positions
                           
                           if num_positions == 0:
                               flag=True
                               break
                           
                        sl=0
                        tp=0
                        num_positions = mt.positions_total()
                        num_positions
                        if num_positions==0:
                            account_info = mt.account_info()
                            balance_new = account_info.balance
                            print(balance_new)
                            if balance_new>balance_previous:
                                tp=tp+1   
                            else:
                                sl=sl+1

                        if flag==True:
                            if sl==1:
                                request = {
                                "action": mt.TRADE_ACTION_DEAL,
                                "symbol": "EURUSDm",
                                "volume": 0.4,
                                "type": mt.ORDER_TYPE_SELL,
                                "price": mt.symbol_info_tick("EURUSDm").ask,
                                "magic": 234000,
                                "comment": "python script open",
                                "type_time": mt.ORDER_TIME_GTC,
                                "type_filling": mt.ORDER_FILLING_IOC,
                                }
                             
                                result = mt.order_send(request)
                                print(result)
                                print(result.price)
                                print(result.order)
                                modify_request = {
                                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                "symbol": "EURUSDm",
                                "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                "sl": result.price+0.00030,  # New stop loss level
                                "tp": result.price-0.00050,  # New take profit level
                                "position": result.order,
                                "magic": 234000,
                                "comment": "python script open", # Use the ticket number of the order you want to modify
                                }
                                modify_result = mt.order_send(modify_request)
                                modify_result

                                flag=False
                                while True:
                                   num_positions = mt.positions_total()
                                   num_positions
                                   
                                   if num_positions == 0:
                                       flag=True
                                       break
                                   
                                sl=0
                                tp=0
                                num_positions = mt.positions_total()
                                num_positions
                                if num_positions==0:
                                    account_info = mt.account_info()
                                    balance_new = account_info.balance
                                    print(balance_new)
                                    if balance_new>balance_previous:
                                        tp=tp+1   
                                    else:
                                        sl=sl+1
        
                                if flag==True:
                                    if sl==1:
                                        request = {
                                        "action": mt.TRADE_ACTION_DEAL,
                                        "symbol": "EURUSDm",
                                        "volume": 0.7,
                                        "type": mt.ORDER_TYPE_BUY,
                                        "price": mt.symbol_info_tick("EURUSDm").ask,
                                        "magic": 234000,
                                        "comment": "python script open",
                                        "type_time": mt.ORDER_TIME_GTC,
                                        "type_filling": mt.ORDER_FILLING_IOC,
                                        }
                                     
                                        result = mt.order_send(request)
                                        print(result)
                                        print(result.price)
                                        print(result.order)
                                        modify_request = {
                                        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                        "symbol": "EURUSDm",
                                        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                        "sl": result.price-0.00030,  # New stop loss level
                                        "tp": result.price+0.00050,  # New take profit level
                                        "position": result.order,
                                        "magic": 234000,
                                        "comment": "python script open", # Use the ticket number of the order you want to modify
                                        }
                                        modify_result = mt.order_send(modify_request)
                                        modify_result


                                        flag=False
                                        while True:
                                           num_positions = mt.positions_total()
                                           num_positions
                                           
                                           if num_positions == 0:
                                               flag=True
                                               break
                                           
                                        sl=0
                                        tp=0
                                        num_positions = mt.positions_total()
                                        num_positions
                                        if num_positions==0:
                                            account_info = mt.account_info()
                                            balance_new = account_info.balance
                                            print(balance_new)
                                            if balance_new>balance_previous:
                                                tp=tp+1   
                                            else:
                                                sl=sl+1
                
                                        if flag==True:
                                            if sl==1:
                                                request = {
                                                "action": mt.TRADE_ACTION_DEAL,
                                                "symbol": "EURUSDm",
                                                "volume": 1.1,
                                                "type": mt.ORDER_TYPE_SELL,
                                                "price": mt.symbol_info_tick("EURUSDm").ask,
                                                "magic": 234000,
                                                "comment": "python script open",
                                                "type_time": mt.ORDER_TIME_GTC,
                                                "type_filling": mt.ORDER_FILLING_IOC,
                                                }
                                             
                                                result = mt.order_send(request)
                                                print(result)
                                                print(result.price)
                                                print(result.order)
                                                modify_request = {
                                                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                "symbol": "EURUSDm",
                                                "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                "sl": result.price+0.00030,  # New stop loss level
                                                "tp": result.price-0.00050,  # New take profit level
                                                "position": result.order,
                                                "magic": 234000,
                                                "comment": "python script open", # Use the ticket number of the order you want to modify
                                                }
                                                modify_result = mt.order_send(modify_request)
                                                modify_result


                                                flag=False
                                                while True:
                                                   num_positions = mt.positions_total()
                                                   num_positions
                                                   
                                                   if num_positions == 0:
                                                       flag=True
                                                       break
                                                   
                                                sl=0
                                                tp=0
                                                num_positions = mt.positions_total()
                                                num_positions
                                                if num_positions==0:
                                                    account_info = mt.account_info()
                                                    balance_new = account_info.balance
                                                    print(balance_new)
                                                    if balance_new>balance_previous:
                                                        tp=tp+1   
                                                    else:
                                                        sl=sl+1
                        
                                                if flag==True:
                                                    if sl==1:
                                                        request = {
                                                        "action": mt.TRADE_ACTION_DEAL,
                                                        "symbol": "EURUSDm",
                                                        "volume": 1.8,
                                                        "type": mt.ORDER_TYPE_BUY,
                                                        "price": mt.symbol_info_tick("EURUSDm").ask,
                                                        "magic": 234000,
                                                        "comment": "python script open",
                                                        "type_time": mt.ORDER_TIME_GTC,
                                                        "type_filling": mt.ORDER_FILLING_IOC,
                                                        }
                                                     
                                                        result = mt.order_send(request)
                                                        print(result)
                                                        print(result.price)
                                                        print(result.order)
                                                        modify_request = {
                                                        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                        "symbol": "EURUSDm",
                                                        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                        "sl": result.price-0.00030,  # New stop loss level
                                                        "tp": result.price+0.00050,  # New take profit level
                                                        "position": result.order,
                                                        "magic": 234000,
                                                        "comment": "python script open", # Use the ticket number of the order you want to modify
                                                        }
                                                        modify_result = mt.order_send(modify_request)
                                                        modify_result


                                                        flag=False
                                                        while True:
                                                           num_positions = mt.positions_total()
                                                           num_positions
                                                           
                                                           if num_positions == 0:
                                                               flag=True
                                                               break
                                                           
                                                        sl=0
                                                        tp=0
                                                        num_positions = mt.positions_total()
                                                        num_positions
                                                        if num_positions==0:
                                                            account_info = mt.account_info()
                                                            balance_new = account_info.balance
                                                            print(balance_new)
                                                            if balance_new>balance_previous:
                                                                tp=tp+1   
                                                            else:
                                                                sl=sl+1
                                
                                                        if flag==True:
                                                            if sl==1:
                                                                request = {
                                                                "action": mt.TRADE_ACTION_DEAL,
                                                                "symbol": "EURUSDm",
                                                                "volume": 2.9,
                                                                "type": mt.ORDER_TYPE_SELL,
                                                                "price": mt.symbol_info_tick("EURUSDm").ask,
                                                                "magic": 234000,
                                                                "comment": "python script open",
                                                                "type_time": mt.ORDER_TIME_GTC,
                                                                "type_filling": mt.ORDER_FILLING_IOC,
                                                                }
                                                             
                                                                result = mt.order_send(request)
                                                                print(result)
                                                                print(result.price)
                                                                print(result.order)
                                                                modify_request = {
                                                                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                                "symbol": "EURUSDm",
                                                                "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                                "sl": result.price+0.00030,  # New stop loss level
                                                                "tp": result.price-0.00050,  # New take profit level
                                                                "position": result.order,
                                                                "magic": 234000,
                                                                "comment": "python script open", # Use the ticket number of the order you want to modify
                                                                }
                                                                modify_result = mt.order_send(modify_request)
                                                                modify_result


                                                                flag=False
                                                                while True:
                                                                   num_positions = mt.positions_total()
                                                                   num_positions
                                                                   
                                                                   if num_positions == 0:
                                                                       flag=True
                                                                       break
                                                                   
                                                                sl=0
                                                                tp=0
                                                                num_positions = mt.positions_total()
                                                                num_positions
                                                                if num_positions==0:
                                                                    account_info = mt.account_info()
                                                                    balance_new = account_info.balance
                                                                    print(balance_new)
                                                                    if balance_new>balance_previous:
                                                                        tp=tp+1   
                                                                    else:
                                                                        sl=sl+1
                                        
                                                                if flag==True:
                                                                    if sl==1:
                                                                        request = {
                                                                        "action": mt.TRADE_ACTION_DEAL,
                                                                        "symbol": "EURUSDm",
                                                                        "volume": 4.6,
                                                                        "type": mt.ORDER_TYPE_BUY,
                                                                        "price": mt.symbol_info_tick("EURUSDm").ask,
                                                                        "magic": 234000,
                                                                        "comment": "python script open",
                                                                        "type_time": mt.ORDER_TIME_GTC,
                                                                        "type_filling": mt.ORDER_FILLING_IOC,
                                                                        }
                                                                     
                                                                        result = mt.order_send(request)
                                                                        print(result)
                                                                        print(result.price)
                                                                        print(result.order)
                                                                        modify_request = {
                                                                        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                                        "symbol": "EURUSDm",
                                                                        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                                        "sl": result.price-0.00030,  # New stop loss level
                                                                        "tp": result.price+0.00050,  # New take profit level
                                                                        "position": result.order,
                                                                        "magic": 234000,
                                                                        "comment": "python script open", # Use the ticket number of the order you want to modify
                                                                        }
                                                                        modify_result = mt.order_send(modify_request)
                                                                        modify_result


                                                                        flag=False
                                                                        while True:
                                                                           num_positions = mt.positions_total()
                                                                           num_positions
                                                                           
                                                                           if num_positions == 0:
                                                                               flag=True
                                                                               break
                                                                           
                                                                        sl=0
                                                                        tp=0
                                                                        num_positions = mt.positions_total()
                                                                        num_positions
                                                                        if num_positions==0:
                                                                            account_info = mt.account_info()
                                                                            balance_new = account_info.balance
                                                                            print(balance_new)
                                                                            if balance_new>balance_previous:
                                                                                tp=tp+1   
                                                                            else:
                                                                                sl=sl+1
                                                
                                                                        if flag==True:
                                                                            if sl==1:
                                                                                request = {
                                                                                "action": mt.TRADE_ACTION_DEAL,
                                                                                "symbol": "EURUSDm",
                                                                                "volume": 7.4,
                                                                                "type": mt.ORDER_TYPE_SELL,
                                                                                "price": mt.symbol_info_tick("EURUSDm").ask,
                                                                                "magic": 234000,
                                                                                "comment": "python script open",
                                                                                "type_time": mt.ORDER_TIME_GTC,
                                                                                "type_filling": mt.ORDER_FILLING_IOC,
                                                                                }
                                                                             
                                                                                result = mt.order_send(request)
                                                                                print(result)
                                                                                print(result.price)
                                                                                print(result.order)
                                                                                modify_request = {
                                                                                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                                                "symbol": "EURUSDm",
                                                                                "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                                                "sl": result.price+0.00030,  # New stop loss level
                                                                                "tp": result.price-0.00050,  # New take profit level
                                                                                "position": result.order,
                                                                                "magic": 234000,
                                                                                "comment": "python script open", # Use the ticket number of the order you want to modify
                                                                                }
                                                                                modify_result = mt.order_send(modify_request)
                                                                                modify_result

                                                                                flag=False
                                                                                while True:
                                                                                   num_positions = mt.positions_total()
                                                                                   num_positions
                                                                                   
                                                                                   if num_positions == 0:
                                                                                       flag=True
                                                                                       break
                                                                                   
                                                                                sl=0
                                                                                tp=0
                                                                                num_positions = mt.positions_total()
                                                                                num_positions
                                                                                if num_positions==0:
                                                                                    account_info = mt.account_info()
                                                                                    balance_new = account_info.balance
                                                                                    print(balance_new)
                                                                                    if balance_new>balance_previous:
                                                                                        tp=tp+1   
                                                                                    else:
                                                                                        sl=sl+1
                                                        
                                                                                if flag==True:
                                                                                    if sl==1:
                                                                                        request = {
                                                                                        "action": mt.TRADE_ACTION_DEAL,
                                                                                        "symbol": "EURUSDm",
                                                                                        "volume": 11.8,
                                                                                        "type": mt.ORDER_TYPE_BUY,
                                                                                        "price": mt.symbol_info_tick("EURUSDm").ask,
                                                                                        "magic": 234000,
                                                                                        "comment": "python script open",
                                                                                        "type_time": mt.ORDER_TIME_GTC,
                                                                                        "type_filling": mt.ORDER_FILLING_IOC,
                                                                                        }
                                                                                     
                                                                                        result = mt.order_send(request)
                                                                                        print(result)
                                                                                        print(result.price)
                                                                                        print(result.order)
                                                                                        modify_request = {
                                                                                        "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                                                        "symbol": "EURUSDm",
                                                                                        "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                                                        "sl": result.price-0.00030,  # New stop loss level
                                                                                        "tp": result.price+0.00050,  # New take profit level
                                                                                        "position": result.order,
                                                                                        "magic": 234000,
                                                                                        "comment": "python script open", # Use the ticket number of the order you want to modify
                                                                                        }
                                                                                        modify_result = mt.order_send(modify_request)
                                                                                        modify_result

                                                                                        flag=False
                                                                                        while True:
                                                                                           num_positions = mt.positions_total()
                                                                                           num_positions
                                                                                           
                                                                                           if num_positions == 0:
                                                                                               flag=True
                                                                                               break
                                                                                           
                                                                                        sl=0
                                                                                        tp=0
                                                                                        num_positions = mt.positions_total()
                                                                                        num_positions
                                                                                        if num_positions==0:
                                                                                            account_info = mt.account_info()
                                                                                            balance_new = account_info.balance
                                                                                            print(balance_new)
                                                                                            if balance_new>balance_previous:
                                                                                                tp=tp+1   
                                                                                            else:
                                                                                                sl=sl+1
                                                                
                                                                                        if flag==True:
                                                                                            if sl==1:
                                                                                                request = {
                                                                                                "action": mt.TRADE_ACTION_DEAL,
                                                                                                "symbol": "EURUSDm",
                                                                                                "volume": 18.9,
                                                                                                "type": mt.ORDER_TYPE_SELL,
                                                                                                "price": mt.symbol_info_tick("EURUSDm").ask,
                                                                                                "magic": 234000,
                                                                                                "comment": "python script open",
                                                                                                "type_time": mt.ORDER_TIME_GTC,
                                                                                                "type_filling": mt.ORDER_FILLING_IOC,
                                                                                                }
                                                                                             
                                                                                                result = mt.order_send(request)
                                                                                                print(result)
                                                                                                print(result.price)
                                                                                                print(result.order)
                                                                                                modify_request = {
                                                                                                "action": mt.TRADE_ACTION_SLTP,  # Use TRADE_ACTION_SLTP to modify SL and TP
                                                                                                "symbol": "EURUSDm",
                                                                                                "price": mt.symbol_info_tick("EURUSDm").bid,  # Use the current ask price
                                                                                                "sl": result.price+0.00030,  # New stop loss level
                                                                                                "tp": result.price-0.00050,  # New take profit level
                                                                                                "position": result.order,
                                                                                                "magic": 234000,
                                                                                                "comment": "python script open", # Use the ticket number of the order you want to modify
                                                                                                }
                                                                                                modify_result = mt.order_send(modify_request)
                                                                                                modify_result
                                                                                            else:
                                                                                                start()
                                                                                    else:
                                                                                        start()
                                                                            else:
                                                                                start()
                                                                    else:
                                                                        start()
                                                            else:
                                                                start()
                                                    else:
                                                        start()
                                            else:
                                                start()
                                    else:
                                        start()
                            else:
                                start()
                    else:
                        start()
            else:
                start()
        
start()           
           
        
        
    
    


