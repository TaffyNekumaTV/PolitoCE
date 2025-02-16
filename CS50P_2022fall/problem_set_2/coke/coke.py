def main():
    amount_due = 50
    owed_change = 0
    accepted_coins = [5,10,25]
    while amount_due>0:
        insert_coin = int(input(f'Amount Due: {amount_due}\nInsert_coin: '))
        if insert_coin not in accepted_coins:
            continue
        amount_due -= insert_coin
    owed_change = - amount_due
    print(f'Change Owed: {owed_change}')

if __name__=='__main__':
    main()
