import random

import pomace

from . import Script


class Salesflare(Script):

    URL = "https://integrations.salesflare.com/s/tortii"
    SKIP = True

    def run(self, page: pomace.Page) -> pomace.Page:
        pomace.log.info("Launching form")
        page = page.click_request_this_listing(wait=0)
        page.fill_email(pomace.fake.email)
        page.fill_company(pomace.fake.company)

        pomace.log.info("Submitting form")
        return page.click_submit(wait=1)

    def check(self, page: pomace.Page) -> bool:
        success = "Thank you for your request" in page
        page.click_close(wait=0.1)
        return success


class TommyBryant(Script):

    URL = "https://www.cityoftarrant.com/contact"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_email(person.email)
        page.fill_comment(
            random.choice(
                [
                    "Tommy Bryant must resign over his racist comments.",
                    "Tommy Bryant's racism doesn't belong in Alabama.",
                    "Get Tommy Bryant out of our city council.",
                    "Tarrant is better than Tommy Bryant. He must go!",
                    "I'm going to keep email the City of Tarrant until Tommy Bryant resigns.",
                ]
            )
        )
        page.fill_captcha("Blue")
        return page.click_submit()

    def check(self, page: pomace.Page) -> bool:
        return "submission has been received" in page


class PatriotPage(Script):

    URL = "https://patriotpage.org"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page = page.click_create_an_account()
        page.fill_email(person.email)
        page.fill_confirm_email(person.email)
        page.fill_password(person.password)
        page.fill_confirm_password(person.password)
        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_nickname(person.nickname)
        page.fill_country("United States")
        page.fill_selection(
            random.choice(
                [
                    "Precinct delegate",
                    "Poll Watcher",
                    "Poll Challenger",
                    "Election Inspector",
                    "Patriot Approved Candidate",
                    "Grassroots Patriot Leader",
                    "Patriot Volunteer",
                ]
            )
        )
        page.browser.execute_script('document.getElementsByTagName("a")[3].remove()')
        page.browser.execute_script('document.getElementsByTagName("a")[3].remove()')
        page.click_agree(wait=0)

        pomace.log.info("Creating account")
        return page.click_create_account(wait=1)

    def check(self, page: pomace.Page) -> bool:
        return "We’re almost there!" in page


class TheRightStuff(Script):

    URL = "https://www.daterightstuff.com"

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page = page.click_sign_up_for_early_access(wait=0)
        page.fill_name(person.name)
        page.fill_email(person.email)
        page.fill_zip(person.zip)
        return page.click_sign_up()

    def check(self, page: pomace.Page) -> bool:
        return "GOT IT" in page


class HeyHandy(Script):

    URL = "https://heyhandy.xyz"
    SKIP = True

    def run(self, page: pomace.Page) -> pomace.Page:
        person = pomace.fake.person

        pomace.log.info(f"Beginning iteration as {person}")
        page = page.click_handy_makes(wait=1)
        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_email(person.email)

        subject, message = random.choice(
            [
                (
                    "Hello",
                    "I want to learn more about NFTs.",
                ),
                (
                    "Help Me",
                    "Your water bottle is tracking me and I need it to stop.",
                ),
                (
                    "Stop This",
                    "You need to stop scamming people with NFTs.",
                ),
                (
                    "Stop Tracking Me",
                    "I demand you stop tracking me.",
                ),
            ]
        )

        page.fill_subject(subject)
        page.fill_message(message)
        return page.click_submit(wait=1)

    def check(self, page: pomace.Page) -> bool:
        return "Successfully submitted!" in page


class HelmsOptical(Script):

    URL = "https://helmsoptical.com"

    def run(self, page) -> pomace.Page:
        page.click_contact_us()

        person = pomace.fake.person
        page.fill_name(person.name)
        page.fill_email(person.email)
        page.fill_message(
            random.choice(
                [
                    "Barbara said Ivermectin cure my blindness, true?",
                    "Does COVID make my vision better? Dr. Helms said it would.",
                    "Should I get COVID to improve my vision like Helms said?",
                    "Do I still need glasses if I had COVID? Dr. Helms wasn't clear.",
                    "Barbara wasn't wearing a mask. Should I stop wearing glasses with masks?",
                    "Dr. Helms refused to wear a mask.",
                    "Dr. Helms had COVID and didn't wear a mask.",
                    "Dr. Helms is unvacincated and put me at risk.",
                    "Barbara told me she's not going to get vaccinated.",
                    "Do I need glasses if I've taken Ivermectin?",
                    "Does Ivermectin improve my vision?",
                    "Do I still need glasses if I've taken Ivermectin?"
                    "Does Ivermectin cure my poor vision?",
                    "Barbara took Ivermectin, should I?",
                    "No one in the office was wearing a mask!",
                    "I felt unsafe because the doctor was not wearing a mask.",
                ]
            )
        )
        return page.click_send(wait=1)

    def check(self, page) -> bool:
        return "Thank you" in page or "Contact Us" in page
