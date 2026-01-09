from project.customer import Customer

from project.trainer import Trainer

from project.equipment import Equipment

from project.exercise_plan import ExercisePlan

from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers:list[Customer]=[]
        self.trainers:list[Trainer] = []
        self.equipment:list[Equipment] = []
        self.plans:list[ExercisePlan] = []
        self.subscriptions:list[Subscription] = []

    def __add_object(self, obj, object_collection):
        if obj not in object_collection:
            object_collection.append(obj)

    def add_customer(self, customer:Customer):
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer:Trainer):
        self.__add_object(trainer,self.trainers)

    def add_equipment(self, equipment:Equipment):
        self.__add_object(equipment,self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id:int):
        sub = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == sub.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == sub.trainer_id), None)
        plan = next((p for p in self.plans if p.id == sub.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

        return '\n'.join([repr(sub), repr(customer), repr(trainer), repr(plan), repr(equipment)])