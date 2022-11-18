import json

from screenpy import Actor, then, when, and_
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ContainTheItem
from api.questions.the_value_of_the_item import Value
from screenpy_requests.actions import SendGETRequest
from screenpy_requests.questions import StatusCodeOfTheLastResponse, BodyOfTheLastResponse


def test_get_single_user(antonio: Actor) -> None:
    id_: int = 2
    url: str = "https://reqres.in/"
    path = f"api/users/{id_}"
    when(antonio).attempts_to(SendGETRequest.to(f"{url}{path}"))
    then(antonio).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse(), ContainTheItem("data")),
        See.the(Value.of_the_key("id"), IsEqualTo(id_))
    )
