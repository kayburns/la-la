import enum

# Google Sign-in related constants
GOOGLE_REDIRECT_URI = "/oauth2callback"
GOOGLE_OAUTH_URL = "https://www.googleapis.com/oauth2/v1/userinfo"

# The number of sections in each semester
NUMBER_OF_SECTIONS = 15


class AccessLevel(enum.Enum):
    """ Different privilege levels for the application. """

    ASSISTANT = "lab assistant"
    STAFF = "course staff"
    ADMIN = "administrator"


class SectionType(enum.Enum):
    """ The types of sections assistants can assist. """

    LAB = "lab"
    OFFICE_HOUR = "office hour"
