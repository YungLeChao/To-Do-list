from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layoyut_and_styling(self):
        # 伊迪絲訪問首頁
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到輸入框完美地居中顯示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)
