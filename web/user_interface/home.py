from screenpy_selenium import Target

URL = "https://realpython.com/"

ENTRY_INPUT = Target.the("entry search field").located_by("//div[@id='navbarSupportedContent']//input[@placeholder]")
