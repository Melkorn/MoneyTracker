import tkinter as tk

class BudgetYearMonthMenu:
    def __init__(self, root, budzety):
        self.root = root
        self.root.title("Budget Year Month Menu")
        self.budzety = budzety

        self.budget_label = tk.Label(root, text="Select Budget:")
        self.budget_label.pack()

        self.budget_var = tk.StringVar(root)
        self.budget_var.set(self.budzety[0].name)
        self.budget_var.trace("w", self.update_years)
        self.budget_dropdown = tk.OptionMenu(root, self.budget_var, *[b.name for b in self.budzety])
        self.budget_dropdown.pack()


        self.year_label = tk.Label(root, text="Select Year:")
        self.year_label.pack()

        self.year_var = tk.StringVar(root)
        self.year_var.set("Select Year")
        self.year_dropdown = tk.OptionMenu(root, self.year_var, [])
        self.year_dropdown.pack()

        self.month_label = tk.Label(root, text="Select Month:")
        self.month_label.pack()

        self.month_var = tk.StringVar(root)
        self.month_var.set("Select Month")
        self.month_dropdown = tk.OptionMenu(root, self.month_var, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        self.month_dropdown.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def update_years(self, *args):
        selected_budget = next((b for b in self.budzety if b.name == self.budget_var.get()), None)
        if selected_budget is not None:
            self.year_var.set("Select Year")
            self.year_dropdown["menu"].delete(0, "end")
            self.year_options = selected_budget.list_years()
            for rok in self.year_options:
                self.year_dropdown["menu"].add_command(label=rok, command=tk._setit(self.year_var, rok))

    def submit(self):
        selected_budget = self.budget_var.get()
        selected_year = self.year_var.get()
        selected_month = self.month_var.get()
        print(f"Selected Budget: {selected_budget}")
        print(f"Selected Year: {selected_year}")
        print(f"Selected Month: {selected_month}")