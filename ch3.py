class Category:
    def __init__(self, category):
        """
        When objects are created, they are passed in the name of
        the category. The class should have an instance variable 
        called ledger that is a list. The class should also contain 
        the following methods:
        """

        self.category = category
        self.ledger = []
    
    def deposit(self, amount, *args):
        """
        Accepts an amount and description. If no description is given, 
        it should default to an empty string. The method should append 
        an object to the ledger list in the form of 
        {"amount": amount, "description": description}
        """

        description = ''
        if args:
            description = args[0]
        
        self.ledger.append({
            'amount': amount, 
            'description': description
        })

    def withdraw(self, amount, *args):
        """
        Similar to the deposit method, but the amount 
        passed in should be stored in the ledger as a negative 
        number. If there are not enough funds, nothing should 
        be added to the ledger. This method should return True 
        if the withdrawal took place, and False otherwise.
        """

        description = ''
        if args:
            description = args[0]

        if self.check_funds(amount):
            # Can be afforded, so add negative amount to ledger
            self.ledger.append({
                'amount': -amount, 
                'description': description
            })
            return True

        else:
            # Could not be afforded, did not take place
            return False

    def get_balance(self):
        """
        Returns the current balance of the budget 
        category based on the deposits and withdrawals 
        that have occurred.
        """

        total = 0
        for ledge in self.ledger:
            total += ledge['amount']
        
        return total
    
    def transfer(self, amount, budget_category):
        """
        Accepts an amount and another budget category as 
        arguments. The method should add a withdrawal with 
        the amount and the description 
        "Transfer to [Destination Budget Category]". The 
        method should then add a deposit to the other budget 
        category with the amount and the description 
        "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be 
        added to either ledgers. This method should return 
        True if the transfer took place, and False otherwise.
        """

        if self.withdraw(amount, f'Transfer to {budget_category.category}'):
            budget_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Accepts an amount as an argument. It returns False 
        if the amount is greater than the balance of the 
        budget category and returns True otherwise. This 
        method should be used by both the withdraw method 
        and transfer method.
        """

        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            # Ie, the amount can be afforded
            return True

    def total_withdrawn(self):
        """Get the total of all withdrawals"""
        tot = 0

        for ledge in self.ledger:
            if ledge['amount'] < 0:
                tot -= ledge['amount']
        
        return tot

    def __str__(self):
        """
        - A title line of 30 characters where the name 
          of the category is centered in a line of * characters.
        - A list of the items in the ledger. Each 
          line should show the description and amount. The 
          first 23 characters of the description should 
          be displayed, then the amount. The amount should be 
          right aligned, contain two decimal places, and 
          display a maximum of 7 characters.
        - A line displaying the category total.
        """

        txt = ''

        txt += self.category.center(30, '*') + '\n'

        for ledge in self.ledger:
            desc = ledge['description'][:23].ljust(23)

            amt = ledge['amount']
            amt = f'{amt:.2f}'
            amt = amt.rjust(7)

            txt += f'{desc}{amt}\n'

        txt += f'Total: {self.get_balance():.2f}'

        return txt

def create_spend_chart(categories):
    """
    Takes a list of categories as an argument. 
    It should return a string that is a bar chart.

    The chart should show the percentage spent in each category 
    passed in to the function. The percentage spent should be 
    calculated only with withdrawals and not with deposits. Down 
    the left side of the chart should be labels 0 - 100. The "bars" 
    in the bar chart should be made out of the "o" character. The 
    height of each bar should be rounded down to the nearest 10. 
    The horizontal line below the bars should go two spaces past the 
    final bar. Each category name should be written 
    vertically below the bar. There should be a title at the 
    top that says "Percentage spent by category".
    """

    # Calculate height of each bar (percentages rounded to nearest 10%)
    totals = [c.total_withdrawn() for c in categories]
    combined_total = sum(totals)
    percentages = [int(tot / combined_total * 10) * 10 for tot in totals]

    # Starting test
    txt = 'Percentage spent by category\n'

    # Bar chart
    for percent_row in range(100, -1, -10):
        line_txt = f'{str(percent_row).rjust(3)}|'

        for p in percentages:
            if percent_row <= p:
                line_txt += ' o '
            else:
                line_txt += ' ' * 3

        txt += line_txt + ' \n'

    # Bottom line
    txt += (' ' * 4) + ('-' * len(percentages) * 3) + '-\n'

    # Vertical labels
    longest_word_len = max([len(c.category) for c in categories])

    for i in range(longest_word_len):
        line_txt = ' ' * 4

        for c in categories:
            if len(c.category) > i:
                char = c.category[i]
                line_txt += f' {char} '
            else:
                line_txt += ' ' * 3

        txt += line_txt + ' '
        if i != longest_word_len - 1:
            txt += '\n'

    return txt

# f = Category('Food')
# f.deposit(1000, 'initial deposit')
# f.withdraw(10.15, 'groceries')

# c = Category('Clothing')
# c.deposit(1000, 'initial deposit')
# c.withdraw(10.15, 'clothes')
# c.withdraw(9.85, 'clothes')

# print(create_spend_chart([f, c, c]))