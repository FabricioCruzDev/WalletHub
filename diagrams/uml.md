classDiagram
    class User {
        +int id
        +string name
        +string last_name
        +string email
        +timestamp updated_at
        +bool synced
        +bool is_deleted
    }
    class Account {
        +int id
        +string name
        +float balance
        +timestamp updated_at
        +bool synced
        +bool is_deleted
        +updateBalance(amount)
    }
    class CreditCard {
        +int id
        +string name
        +float limit
        +float available_limit
        +int closing_day
        +int due_day
        +timestamp updated_at
        +bool synced
        +bool is_deleted
        +updateLimit(amount)
    }
    class Transaction {
        +int id
        +string description
        +float value
        +datetime date
        +string type (DEBIT/CREDIT)
        +timestamp updated_at
        +bool synced
        +bool is_deleted
    }
    class Category {
        +int id
        +string name
        +string operator
        +timestamp updated_at
        +bool synced
        +bool is_deleted
    }
    class FixedExpense {
        +int id
        +string description
        +float value
        +int due_day
        +timestamp updated_at
        +bool synced
        +bool is_deleted
    }
    class Invoice {
        +int id
        +date month_ref
        +float total_value
        +bool is_paid
        +timestamp updated_at
        +bool synced
        +bool is_deleted
    }

    User "1" --> "*" Account
    User "1" --> "*" CreditCard
    User "1" --> "*" FixedExpense
    Account "1" -- "*" Transaction : registers
    CreditCard "1" -- "*" Transaction : registers
    CreditCard "1" -- "*" Invoice : generates
    Transaction "*" -- "1" Category : belongs to
    Invoice --|> Transaction : acts as complex transaction