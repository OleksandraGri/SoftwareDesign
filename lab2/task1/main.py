from abc import ABC, abstractmethod

# Базовий клас підписки
class Subscription(ABC):
    def __init__(self, price, min_period, channels):
        self.price = price
        self.min_period = min_period
        self.channels = channels

    @abstractmethod
    def get_subscription_details(self):
        pass

# Конкретні підписки
class DomesticSubscription(Subscription):
    def get_subscription_details(self):
        return f"Domestic Subscription: Price: {self.price}, Min period: {self.min_period} months, Channels: {', '.join(self.channels)}"

class EducationalSubscription(Subscription):
    def get_subscription_details(self):
        return f"Educational Subscription: Price: {self.price}, Min period: {self.min_period} months, Channels: {', '.join(self.channels)}"

class PremiumSubscription(Subscription):
    def get_subscription_details(self):
        return f"Premium Subscription: Price: {self.price}, Min period: {self.min_period} months, Channels: {', '.join(self.channels)}"

# Створення підписки через різні класи
class WebSite:
    def create_subscription(self, sub_type):
        if sub_type == "Domestic":
            return DomesticSubscription(15, 1, ["News", "Sports"])
        elif sub_type == "Educational":
            return EducationalSubscription(10, 3, ["Learning", "Tutorials"])
        elif sub_type == "Premium":
            return PremiumSubscription(25, 6, ["All Channels"])
        else:
            raise ValueError("Unknown subscription type")

class MobileApp:
    def create_subscription(self, sub_type):
        if sub_type == "Domestic":
            return DomesticSubscription(12, 1, ["Movies", "Music"])
        elif sub_type == "Educational":
            return EducationalSubscription(8, 2, ["Courses", "Science"])
        elif sub_type == "Premium":
            return PremiumSubscription(20, 12, ["Exclusive Content", "Movies"])
        else:
            raise ValueError("Unknown subscription type")

class ManagerCall:
    def create_subscription(self, sub_type):
        if sub_type == "Domestic":
            return DomesticSubscription(18, 2, ["Lifestyle", "Talk Shows"])
        elif sub_type == "Educational":
            return EducationalSubscription(15, 6, ["Math", "Physics"])
        elif sub_type == "Premium":
            return PremiumSubscription(30, 12, ["Full Access", "Special Features"])
        else:
            raise ValueError("Unknown subscription type")

def main():
    website = WebSite()
    subscription = website.create_subscription("Premium")
    print(subscription.get_subscription_details())

if __name__ == "__main__":
    main()
