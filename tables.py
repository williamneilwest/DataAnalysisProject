customers = []


class Customer:
    last_customer_id = 0

    def __init__(self, customer_name, address, city, zip_code, email, phone_number):
        self.customer_number = Customer.generate_customer_id()
        self.customer_name = customer_name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.email = email
        self.phone_number = phone_number
        # Class variable to track the id of each entry incrementally

    @classmethod
    def generate_customer_id(cls):
        cls.last_customer_id += 1
        return cls.last_customer_id

    def add_data(self):
        customers.append(self)

    def __str__(self):
        return f"Customer Number={self.customer_number}, Customer Name={self.customer_name}, " \
               f"Address={self.address}, City={self.city},ZIP={self.zip_code},Contact={self.email},Phone={self.phone_number}"


class Contract:
    def __init__(self, contract_number, customer_number, contract_start_date, contract_end_date, contract_value,
                 contract_type):
        self.contract_number = contract_number
        self.customer_number = customer_number
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date
        self.contract_value = contract_value
        self.contract_type = contract_type


class Equipment:
    def __init__(self, equipment_id, equipment_type, contract_number, manufacture, age):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.contract_number = contract_number
        self.manufacture = manufacture
        self.age = age


class ServiceCallSchedule:
    def __init__(self, service_call_number, service_call_description, scheduled_date, contract_number):
        self.service_call_number = service_call_number
        self.service_call_description = service_call_description
        self.scheduled_date = scheduled_date
        self.contract_number = contract_number
