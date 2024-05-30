import calendar

class Entry:
    """
    Represents a single entry in a category.

    Attributes:
        description (str): The description of the entry.
        date (str): The date of the entry.
        value (float): The value of the entry.
    """

    def __init__(self, description: str, date: str, value: float):
        self.description = description
        self.date = date
        self.value = value


class Category:
    """
    Represents a category of entries.

    Attributes:
        title (str): The title of the category.
        entries (list[Entry]): A list of entries in the category.
        total (float): The total value of all entries in the category.
    """

    def __init__(self, title: str):
        self.title = title
        self.entries = []
        self.total = 0

    def add(self, expense: Entry):
        self.entries.append(expense)
        self.total += expense.value
    
    def printExpenses(self):
        print(f"    Category: {self.title}")

        if self.total == 0:
            print("        No entries for this category yet")
        
        else:
            for entry in self.entries:
                print(f"        {entry.description} : {entry.value}")
            
            print(f"    Total: {self.total}")

    def getTotal(self):
        return self.total


class Year:
    """
    Represents a colection of months.

    Attributes:
        number (int): The year.
        months (dict([int][dict[str][Category]]): A dictionary that associates a month to all its categories of expenses.
    """

    def __init__(self, number: int):
        self.number = number
        self.months = dict()

        self.setBasicCategories()

    def addExpense(self, month: int, category: Category, expense: Entry):
        """
        Add an expense to a given category in the month.
        
        If the category does not exist, create it.

        Args:
            month (int): The month of the year.
            category (str): The title of the category of expenses.
            expense (Entry): The expense itself, with description, date and value.
        """

        if month < 1 or month > 13:
            raise ValueError("Invalid month. Month must be between 1 and 12.")

        if category not in self.months[month]:
            self.months[month][category] = Category(category)

        self.months[month][category].add(expense)

    def setBasicCategories(self):
        """
        Initialize, for each month, the most commom types of expenses: \
        health, household, transport, and leisure. 
        """
        categories = ["health", "household", "transport", "leisure"]

        for month in range(1, 13):
            self.months[month] = {}

            for title in categories:
                self.months[month][title] = Category(title)
    
    def listExpenses(self, month : int):
        print(f"Expenses of {calendar.month_name[month]}:")

        for categoryInstance in self.months[month].values():
            categoryInstance.printExpenses()
            print("")


if __name__ == "__main__":
    curr_year = Year(2024)

    expense1 = Entry("Ida ao dermatologista", "2024-05-01", 400)
    expense2 = Entry("Feira", "2024-05-01", 250)
    expense3 = Entry("Dentista", "2024-05-01", 100)
    expense4 = Entry("Viagem a Itália", "2024-05-01", 1000)

    curr_year.addExpense(1, "health", expense1)
    curr_year.addExpense(1, "household", expense2)
    curr_year.addExpense(1, "health", expense3)
    curr_year.addExpense(7, "travel", expense4)

    curr_year.listExpenses(1)
    curr_year.listExpenses(2)
    curr_year.listExpenses(7)
