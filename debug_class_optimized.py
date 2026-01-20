from dataclasses import dataclass

@dataclass
class CustomerDetails:
    fullname: str
    gender: str

    @property
    def title(self) -> str:
        """Returns the title based on gender."""
        # Dictionary lookup is cleaner than if-else for mapping
        titles = {
            "male": "Mr",
            "female": "Mrs"
        }
        return titles.get(self.gender.lower(), "not disclosed") # Default to Mx if unknown

    def __str__(self):
        return f"{self.title}. {self.fullname}"

# Input
fullname = input("Enter your full name: ") or "John Doe"
gender = input("Enter your gender (male/female): ") or "male"

# Usage
customer = CustomerDetails(fullname, gender)
print(f"Hello, {customer}")
