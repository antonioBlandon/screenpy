import json

from screenpy import AnActor
from screenpy.pacing import beat
from screenpy_requests.abilities import MakeAPIRequests


class Value:

    @staticmethod
    def of_the_key(key_: str) -> "Value":
        return Value(key_)

    @beat("{} checks the value of {key_}")
    def answered_by(self, the_actor: AnActor) -> str:
        response = json.loads(the_actor.uses_ability_to(MakeAPIRequests).responses[-1].text)
        return response["data"].get(self.key_)

    def __init__(self, key_: str) -> None:
        self.key_: str = key_
