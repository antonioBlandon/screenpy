from screenpy import AnActor, given, when, then
from screenpy.actions import See
from screenpy.resolutions import ContainTheText
from screenpy_selenium.actions import Open
from screenpy_selenium.questions import Text

from web.tasks.Search import Search
from web.user_interface.home import URL
from web.user_interface.search_result import RESULT_TEXT


def test_wait_for_text(antonio: AnActor) -> None:
    test_text = "python"
    given(antonio).was_able_to(Open.their_browser_on(URL))
    when(antonio).attempts_to(Search(test_text))
    then(antonio).should(See.the(Text.of_the(RESULT_TEXT), ContainTheText(test_text)))
