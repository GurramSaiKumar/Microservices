from abc import ABC, abstractmethod


class DataAccessInterface(ABC):
    @abstractmethod
    def fetch_data(self):
        pass


class BusinessLogic:
    def __init__(self, data_service: DataAccessInterface):
        self.data_service = data_service

    def perform_business_logic(self):
        data = self.data_service.fetch_data()
        if data is not None:
            print("Received Data")
        else:
            print("No data received")

        print(f"Data after manipulation {data + 10}")


class DataAccessFromMongoImplementation(DataAccessInterface):

    def fetch_data(self):
        # get Data from DB
        return 60


class DataAccessFromPostgresImplementation(DataAccessInterface):

    def fetch_data(self):
        # get Data from DB
        return 10


# client code.
# So if anything changes in DataAccessService, NO need to change in BusinessLogic class.
# This is because BusinessLogic is depending on concrete classes abstract classes not on concrete classes..
if __name__ == '__main__':
    data_access_service = DataAccessFromMongoImplementation()
    business_logic = BusinessLogic(data_access_service)
    business_logic.perform_business_logic()
