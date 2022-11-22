from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait
from selenium.webdriver import Keys

from web.user_interface.home import ENTRY_INPUT
from web.user_interface.search_result import RESULT_TEXT


class Search:

    @beat('{} searches Real Python for "{search_query}"')
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Enter.the_text(self.search_query).into_the(ENTRY_INPUT).then_hit(Keys.RETURN),
            Wait(2).seconds_for_the(RESULT_TEXT),
        )

    def __init__(self, search_query: str) -> None:
        self.search_query: str = search_query

