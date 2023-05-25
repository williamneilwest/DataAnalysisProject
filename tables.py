customers = []
contracts = []
equipment = []
service_call_schedule = []


class Customer:
    # Counter variable to track the customer number
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

    # Add the customer object to the customers list
    def add_data(self):
        customers.append(self)

    # Override the print method to print the details of the object in a readable format
    def __str__(self):
        return f"Customer Number={self.customer_number}, Customer Name={self.customer_name}, " \
               f"Address={self.address}, City={self.city},ZIP={self.zip_code},Contact={self.email},Phone={self.phone_number}"


class Contract:
    last_contract_id = 0

    def __init__(self,  customer_number, contract_start_date, contract_end_date, contract_value,
                 contract_type):
        self.contract_number = Contract.generate_contract_id()
        self.customer_number = customer_number
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date
        self.contract_value = contract_value
        self.contract_type = contract_type

    @classmethod
    def generate_contract_id(cls):
        cls.last_contract_id += 1
        return cls.last_contract_id

    # Add the contract object to the customers list
    def add_data(self):
        contracts.append(self)

    # Override the print method to print the details of the object in a readable format
    def __str__(self):
        return f"Contract Number={self.contract_number}, Customer Number={self.customer_number}, Contract Start Date={self.contract_start_date}, " \
               f"Contract End Date={self.contract_end_date}, Value={self.contract_value},Type={self.contract_type}"


class Equipment:
    last_equipment_id = 0

    def __init__(self, equipment_type, contract_number, manufacture, age):
        self.equipment_id = Equipment.generate_equipment_id()
        self.equipment_type = equipment_type
        self.contract_number = contract_number
        self.manufacture = manufacture
        self.age = age

    @classmethod
    def generate_equipment_id(cls):
        cls.last_equipment_id += 1
        return cls.last_equipment_id

    # Add the contract object to the customers list
    def add_data(self):
        equipment.append(self)

    # Override the print method to print the details of the object in a readable format
    def __str__(self):
        return f"Equipment ID={self.equipment_id}, Equipment Type={self.equipment_type}, " \
               f"Contract Number={self.contract_number}, Manufacture={self.manufacture},Age={self.age}"


class ServiceCallSchedule:
    last_service_call_id = 0

    def __init__(self, service_call_description, scheduled_date, contract_number):
        self.service_call_number = ServiceCallSchedule.generate_service_call_id()
        self.service_call_description = service_call_description
        self.scheduled_date = scheduled_date
        self.contract_number = contract_number

    @classmethod
    def generate_service_call_id(cls):
        cls.last_service_call_id += 1
        return cls.last_service_call_id

    # Add the contract object to the service_call_schedule list
    def add_data(self):
        service_call_schedule.append(self)

    # Override the print method to print the details of the object in a readable format
    def __str__(self):
        return f"Service Call ID={self.service_call_number}, Description={self.service_call_description}, " \
               f"Contract Number={self.contract_number}, Scheduled Date={self.scheduled_date}"
