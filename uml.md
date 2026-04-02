classDiagram
    class User {
        +int id
        +string name
        +STRING last_name
        +string email
    }
    class Account {
        +int id
        +string name
        +float balance
        +updateBalance(amount)
    }
    class CreditCard {
        +int id
        +string name
        +float limit
        +float available_limit
        +int closing_day
        +int due_day
        +updateLimit(amount)
    }
    class Transaction {
        +int id
        +string description
        +float value
        +datetime date
        +string type (DEBIT/CREDIT)
    }
    class Category {
        +int id
        +string name
        +string icon
    }
    class FixedExpense {
        +int id
        +string description
        +float value
        +int due_day
    }
    class Invoice {
        +int id
        +date month_ref
        +float total_value
        +bool is_paid
    }

    User "1" --> "*" Account
    User "1" --> "*" CreditCard
    User "1" --> "*" FixedExpense
    Account "1" -- "*" Transaction : registers
    CreditCard "1" -- "*" Transaction : registers
    CreditCard "1" -- "*" Invoice : generates
    Transaction "*" -- "1" Category : belongs to
    Invoice --|> Transaction : acts as complex transaction