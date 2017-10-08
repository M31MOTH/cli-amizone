"""Authenticate Module."""

import sys
import requests
from Common import Common


class Authenticate(Common):
    """
    Authenticate class.

    This class performs user login (authentication), and
    returns the session object.
    This session object is further used to get other details.
    """

    def __init__(self):
        """Initialisations."""
        Common.__init__(self)
        self.url = "https://amizone.net"
        self.login_url = "https://amizone.net/amizone/Index.aspx"
        self.session = requests.Session()
        self.payload = {}
        self.soup = self.get_html(self.session, self.url)

    def set_payload(self, username, password):
        """
        set_payload method.

        `payload` is the data to be sent to perform login.
        `payload` includes hidden form data, username, password.
        `payload` here is a dictationary [{"key":"value"}]
        """
        # Get `hidden` form data
        for i in self.soup.find_all("input", {'type':'hidden'}):
            self.payload[i['name']] = i['value']

        """
        Amizone has multiple username/password input fields and
        selects any one at random. The field being used is detected,
        and used to perform login.

        Eg:
        <input name="mifrd3qj3rca5o3dw243he" type="text" id="mifrd3qj3rca5o3dw243he" style="display:none;">
        <input name="nyrfgj2kn4cf51c4onujcb" type="text" id="nyrfgj2kn4cf51c4onujcb" style="display:none;">
        <input name="yx3llru2bl2kd4jzoi5djf" type="text" id="yx3llru2bl2kd4jzoi5djf">

        The field in use is one with no `style` attribute.
        """
        uname_fields = self.soup.find_all('div', class_='form-elements')[1].find_all('input')
        password_fields = self.soup.find_all('div', class_='form-elements')[2].find_all('input')
        for uname_id in uname_fields:
            if not uname_id.has_attr('style'):
                self.payload[uname_id['id']] = username
            else:
                self.payload[uname_id['id']] = ""

        for password_id in password_fields:
            if not password_id.has_attr('style'):
                self.payload[password_id['id']] = password
            else:
                self.payload[password_id['id']] = ""

        """
        ImgBttn_Login is the login button on amizone.net.
        It's .x and .y values are the co-ordinate positions of mouse-pointer
        where button is clicked.
        Setting it to 0 means `enter` key is pressed.
        """
        self.payload["ImgBttn_Login.x"] = 0
        self.payload["ImgBttn_Login.y"] = 0

        # Other misc. data required to be sent to perform login
        self.payload['__EVENTTARGET'] = ""
        self.payload['__EVENTARGUMENT'] = ""

    def login(self, username, password):
        """
        Once payload is set, we perform login.

        session.post(url, data, headers)
        """
        self.set_payload(username, password)
        print("Logging in...")
        a = self.session.post(self.login_url, data=self.payload, headers={'Referer': self.login_url})
        if a.history == []:
            print("Incorrect Username/Password! Try Again.\n")
            sys.exit(2)
        return self.session


if __name__ == "__main__":
    print("It's a module!")
