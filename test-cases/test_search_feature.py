from pages.app import App


class Test_search:

    def setup(self):
        self.main_page = App.start()

    def test_enter_notification(self):
        self.main_page.to_notification()

    def test_search(self):

        self.main_page.to_search().search("appium")

    def teardown(self):
        self.main_page = App.quit()
