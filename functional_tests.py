from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    # def check_for_row_in_list_table(self, row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retreive_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('To-Do', header_text)

        # # She is invited to enter a to-do item straight away
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # # She types buy peacock feathers into a text box
        # inputbox.send_keys('Buy peacock feathers')

        # # When she hits enter, the page updates, and now the
        # # page lists "1: Buy peacock feathers" as ann item in a to-do list table
        # inputbox.send_keys(Keys.ENTER)

        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacock feathers to make a fly')

        # self.check_for_row_in_list_table('1: Buy peacock feathers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        
        
        #self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
