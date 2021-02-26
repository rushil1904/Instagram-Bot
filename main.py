from selenium import webdriver
from time import sleep


class InstaUnfollowers:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com")
        sleep(2)
        # instagram login
        username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_type.send_keys(password)
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        submit.click()
        sleep(8)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
        sleep(5)

    def get_unfollowers(self):
        Following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        following = self.get_people()
        Followers = self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
        Followers.click()
        followers = self.get_people()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def get_people(self):
        sleep(7)
        scroll_box = self.driver.find_element_by_css_selector(".isgrP")
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            sleep(3)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        close = self.driver.find_element_by_css_selector("div.WaOAr:nth-child(3) > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)")
        close.click()
        return names

username = ''
password = ''
my_bot = InstaUnfollowers(username, password)
my_bot.get_unfollowers()
try:
    my_bot.driver.close()
except:
    print("Fail")
    my_bot.driver.close()
