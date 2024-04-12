from abc import abstractmethod
from .defs import State, Bid, EnergyAction, Reward
from .network_entity import NetworkEntity

class MarketEntity():
    def __init__(self, name, network_entity:NetworkEntity):
        self.name = name
        self.network_entity = network_entity

    @abstractmethod
    def get_bid(self, bid_type:str, state:State, args)-> Bid:
        pass

    def step(self, action: EnergyAction) -> [State,Reward]:
        return self.network_entity.step(action)

    def predict(self, action: EnergyAction, state: State) -> [State,Reward]:
        return self.network_entity.predict(action, state)


class MarketProducer(MarketEntity):

    def __init__(self, name: str, network_entity:NetworkEntity):
        super().__init__(name, network_entity=NetworkEntity)

class MarketConsumer(MarketEntity):

    def __init__(self, name: str, network_entity:NetworkEntity):
        super().__init__(name, network_entity=NetworkEntity)



