from screenpy_selenium import Target

RESULT_TEXT = Target.the("result text").located_by("//span[@class='text-muted']")
