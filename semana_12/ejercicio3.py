from abc import ABC, abstractmethod

# For this exercise I investigated uses for multiple inheritance on a realistic environment. Which include simplyfiying code: helping the dev to have modular portions of code instead of duplicates when needed, mixin of atributes or methods that can apply to different instances. For my example, a employee data base could hold information for each employee that perform different duties, have their own key responsabilities

class Employee(ABC):
    @abstractmethod
    def daily_duties(self):
        pass

class Leader:
    responsabilities = {
        'key_responsability':'guide your team',
        'direct-reports-to':'Upper Management',
        'can-assign-tasks?':'yes'        
    }

    bonus = 1500

class Associate:
    responsabilities = {
        'key_responsability':'production',
        'direct-reports-to':'Team Leader',
        'can-assign-tasks?':'no'        
    }

    bonus = 750

class Manager(Employee,Leader):
    
    def daily_duties(self):
        print('Manager daily duties include supervising, assingning tasks and reporting to higher management')

class Tier1Associate(Employee,Associate):
    def daily_duties(self):
        print('Tier 1 daily duties include Calling Clients, resolving simple tasks and escalate to Tier 2 when necesary')

class Tier2Associate(Employee,Associate):
    def daily_duties(self):
        print('Tier 2 daily duties include Taking escalation calls, creation of tickets to the dev team')


manager_1 = Manager()

manager_1.daily_duties()
print(f'This person has a bonus of: ${manager_1.bonus}')

tier_1_associate_1 = Tier1Associate()
tier_1_associate_1.daily_duties()
print(f'This person has a bonus of: ${tier_1_associate_1.bonus}')

tier_2_associate_1 = Tier2Associate()
tier_2_associate_1.daily_duties()
print(f'This person has a bonus of: ${tier_2_associate_1.bonus}')

