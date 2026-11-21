# supplier.py
# A Supplier is the company that provides products to the store.
# Supplier and Product have an ASSOCIATION: they work together,
# but neither is part of the other, and both can exist on their own.


class Supplier:

    # Create a supplier with an ID, a name and a contact email
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        # Private attributes (encapsulation), with type hints
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    # Getter: return the supplier ID
    def get_supplier_id(self) -> str:
        return self.__supplier_id

    # Getter: return the supplier name
    def get_name(self) -> str:
        return self.__name

    # Getter: return the contact email
    def get_contact_email(self) -> str:
        return self.__contact_email

    # Print this supplier's details on one line
    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id} | Name: {self.__name} | "
              f"Email: {self.__contact_email}")
