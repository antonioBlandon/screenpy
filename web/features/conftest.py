from typing import Generator

import pytest
from allure_commons.types import AttachmentType
from screenpy import AnActor
from screenpy.pacing import the_narrator
from screenpy_adapter_allure import AllureAdapter
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import SaveScreenshot

from web.configuration.driver_manager import CustomDriver

the_narrator.adapters.append(AllureAdapter())


@pytest.fixture(scope="function", name="antonio")
def fixture_actor() -> Generator:
    the_actor = AnActor.named("antonio").who_can(BrowseTheWeb.using(CustomDriver.chrome()))
    yield the_actor
    the_actor.attempts_to(
        SaveScreenshot.as_("test.png").and_attach_it(
            name="End of Test Screenshot", attachment_type=AttachmentType.PNG
        ),
    )
    the_actor.exit_stage_left()
