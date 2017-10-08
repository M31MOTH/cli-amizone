"""My Courses module."""

from Common import Common

class My_Courses(Common):
    """
    Class to display info about `My Courses`.
    """
    def __init__(self, session):
        Common.__init__(self)
        self.session = session
        self.url = "https://amizone.net/Amizone/WebForms/Academics/MyCourses.aspx"
        pass

    def get_courses(self):
        """
        get_courses method.

        This method fetches student's courses
        :: Course Code
        :: Course Name
        :: Course Type
        :: Attendance
        """
        soup = self.get_html(self.session, self.url)
        req_table = soup.find("table", id="ctl00_ContentPlaceHolder1_GridCourses")
        rows = req_table.findAll('tr')
        index = 0
        for row in rows:
            if not row.has_attr('bgcolor'):
                index += 1
                data = row.findAll('td')
                course_code = "".join(data[1].string.split())
                course_name = data[2].string
                course_type = "({})".format(data[3].string)
                attendance = "[{}]".format(data[7].a.string)
                print(index, course_code, course_name, course_type, attendance)

    def get_course_details():
        """
        WIP
        """
        pass
