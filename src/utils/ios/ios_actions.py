
class IOSAction:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_text_element(self, text):
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": f"name == '{text}'"
        })

    def long_press(self, element, duration):
        self.driver.execute_script("mobile: touchAndHold", {
            "element": element,
            "duration": duration
        })

    def swipe(self, element, direction):
        self.driver.execute_script("mobile: swipe", {
            "direction": direction,
            "percent": 0.2
        })
