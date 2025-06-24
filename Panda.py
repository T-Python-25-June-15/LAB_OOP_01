

class Panda:
    
    def __init__(self, name:str, age:int, weight:float, health_status:str, daily_sleep_hour:float):
        self.name = name
        self.age = age
        self.weight = weight
        self.health_status = health_status
        self.daily_sleep_hour = daily_sleep_hour
        
        
    def check_health(self):
        '''
        Checks the panda's health based on its weight.

        Returns:
            str: "sick" if weight < 100kg, otherwise "Good".
        '''
        if self.weight < 100:
            self.health_status = "sick"
            return "sick"
        else:
            self.health_status = "Good"
            return "Good"
        
    def status(self):
        '''
        Returns the full status information of the panda.

        Returns:
            str: A formatted string containing the panda's name, age, weight,
                health status, and daily sleep hours.
        '''
        result = ""
        result += f"name: {self.name} - age: {self.age} - weight: {self.weight}"
        result += f"\nstutus: {self.health_status}\ndaily sleep hour: {self.daily_sleep_hour}"
        return result