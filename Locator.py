class Locator(object):
    # Google Search Page
    search_text = "//input[@name='q']"
    submit = "//form[@action]/div/div/div/center/input[@role='button']"
    # //input[@name='Google Search']"
    logo = "//img[@alt='Google' and @srcset]"