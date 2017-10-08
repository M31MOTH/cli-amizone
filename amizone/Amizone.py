"""Main Amizone class"""

from Authenticate import Authenticate


class Amizone(Authenticate):
    """
    Main Amizone class.

    This class starts the main execution.
    """

    def __init__(self, username, password):
        """Initialisations."""
        Authenticate.__init__(self)
        # login() is defined in Authenticate module - returns session obj
        self.session = self.login(username, password)
        self.home = "https://amizone.net/amizone/WebForms/Home.aspx"

    def homepage(self):
        """
        To get User's homepage and the required data fields.

        :: My Courses
        :: TimeTable
        """
        soup = self.get_html(self.session, self.home)
        name = soup.find("span", id="ctl00_lblUser").string
        print("\nWelcome, {}".format(name))

    def mycourses(self):
        """Get `My Courses` data."""
        from My_Courses import My_Courses
        cs = My_Courses(self.session)
        cs.get_courses()

    def timetable(self):
        """Get TimeTable."""
        print("WIP")
        pass


def main():
    """ Execution begins here"""
    username = int(input("Username: "))
    password = input("Password: ")
    amz = Amizone(username, password)
    amz.homepage()
    print("1. My Courses")
    print("2. TimeTable")
    option = int(input("\nOption > "))
    print()
    if option == 1:
        amz.mycourses()
    elif option == 2:
        amz.timetable()


if __name__ == '__main__':
    main()
