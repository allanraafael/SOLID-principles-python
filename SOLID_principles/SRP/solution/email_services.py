import yagmail


class EmailServices:
    """Handles only email-related services"""

    @staticmethod
    def is_valid(email: str):
        """
        Check if the email parameter is valid

        :param email:
            String must be in email format to be valid
        """

        return "@" in email

    @staticmethod
    def send(to: str, subject: str, message: list[str], user, password):
        """
        Sends the email

        :param to:
            Email sending destination
        :param subject:
            Summary of what will be informed in the email
        :param message:
            Email body
        :param user:
            replace by your gmail credentials
        :param password:
            replace by your gmail credentials
        """

        # If it fails, activate for less secure app access: https://www.google.com/settings/security/lesssecureapps
        yag = yagmail.SMTP(user=user, password=password)
        yag.send(to, subject, message)
