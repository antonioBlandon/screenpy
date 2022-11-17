from screenpy import Actor, then, when
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo
from screenpy_requests.actions import SendGETRequest
from screenpy_requests.questions import StatusCodeOfTheLastResponse


def test_get_single_user(antonio: Actor) -> None:
    when(antonio).attempts_to(SendGETRequest.to("https://reqres.in/api/users/2"))
    then(antonio).should(See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)))
