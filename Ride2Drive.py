# playwright_button_clicks.py

from playwright.sync_api import sync_playwright

import time

def run():
    with sync_playwright() as p:
        # Launch browser (headless=False to see it in action)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
  # Maximize the browser window
        page.context.new_cdp_session(page).send("Browser.setWindowBounds", {
            "windowId": page.context.new_cdp_session(page).send("Browser.getWindowForTarget")["windowId"],
            "bounds": {"windowState": "maximized"}
        })
        # Go to the website
        url = "https://r2d-au-dev.vercel.app/"
        page.goto(url)

        # Wait for the page to load
        page.wait_for_load_state("networkidle")
        # Click the "How it works" button
        how_it_works_button = page.query_selector('header div:nth-child(2) a:nth-child(1)').click()
        # Click the "About us" button
        about_us_button = page.query_selector("//a[normalize-space()='About Us']").click()
       #Click "FAQ" bugtton 
        page.query_selector("//a[normalize-space()='FAQ']").click()
       #Click the "Refer" button
        #page.query_selector("//a[normalize-space()='Refer']").click()
       #Click "Check Eligibility" button
        page.query_selector("//a[normalize-space()='Check Eligibility']").click()
       #Click the "Article" button
        page.query_selector("//a[normalize-space()='Articles']").click()
       #Click the "Apply Now" button
        page.query_selector("//a[normalize-space()='Apply Now']").click()
        time.sleep(2)
       


       # #1st Page(Your Details)
       # #First Name:
        page.fill("input#firstName", "Rafiul")
        time.sleep(1)
        #Last Name:
        page.fill("input#lastName", "Turjo")
        time.sleep(1)
        #Email:
        import random
        import string

        # Generate a random email without any number at the start
        def generate_random_email():
            # Ensure the first character is a letter
            first_char = random.choice(string.ascii_lowercase)
            rest = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
            username = first_char + rest
            domain = ''.join(random.choices(string.ascii_lowercase, k=5))
            return f"{username}@{domain}.com"
        random_email = generate_random_email()
        page.fill("input#email", random_email)
        time.sleep(1)
        #page.fill("input#email", "test@example.com")
        #Phone Number:
        page.fill("input#phone", "0415789585")
        time.sleep(1)
        #State:
        # Input State
        page.select_option("select#state", "NSW")
        time.sleep(1)
        #Accident Date:
        # Input Accident Date
        page.fill("input#accidentDate", "28/08/2025")
        time.sleep(1)
        #How Did the Collision Occur?
        page.fill("textarea#collision", "Some collision description")
        time.sleep(1)
        #When Do You Need the Car? 
        page.fill("input#carNeedDate", "30/11/2025")
        time.sleep(1)
        #How Did You Hear About Us?
        page.select_option("select#hear", "Google")
        time.sleep(1)
        #Checkbox:
        page.check("input#newsletter")
        time.sleep(1)
        #Submit:
        page.click("#submitBtn")
        time.sleep(1)
        #Click Submit Btn again:
        # Click Submit
        page.click("#submitBtn")
        # Wait explicitly for an element from Page 2 to appear
        page.wait_for_selector("input#dob", timeout=20000)
        # After clicking submit, there may be a popup reCaptcha.
        # Wait for potential reCaptcha frame and try to solve if it appears
        
        # Attempt to wait for a reCaptcha iframe (commonly named 'iframe[title="reCAPTCHA"]')
        try:
            # Wait 4 seconds to see if a captcha pops up visually
            time.sleep(4)
            # Look for any iframe containing 'recaptcha' in its title or src
            recaptcha_frame = None
            frames = page.query_selector_all("iframe")
            for frame in frames:
                src = frame.get_attribute("src") or ""
                title = frame.get_attribute("title") or ""
                if "recaptcha" in src.lower() or "recaptcha" in title.lower():
                    recaptcha_frame = frame
                    break
            if recaptcha_frame:
                # Switch to the recaptcha iframe and attempt to click checkbox, if rendered
                frame_element = recaptcha_frame
                # Find the bounding box & coordinate center for the checkbox
                checkbox = page.frame_locator("iframe[title*='reCAPTCHA']").locator(".recaptcha-checkbox-border")
                checkbox.click(timeout=10000)
                time.sleep(4)
                # Optionally, wait for the captcha to validate (adjust as needed)
        except Exception as e:
            # If no recaptcha appears, just continue
            pass



        #Page 2(Vehicle & Insurance):
        #Date Of Birth:
        page.fill("input#dob", "01/01/1990")
        time.sleep(1)
        #Address:
        # Input Address
        page.fill("input#address", "123 Main Street")
        time.sleep(1)
        # Wait for the address dropdown options to appear
        page.wait_for_selector(".px-3.py-2.cursor-pointer.hover\\:bg-gray-100", timeout=5000)
        # Optionally, click the first dropdown option if required
        page.click(".px-3.py-2.cursor-pointer.hover\\:bg-gray-100")
        time.sleep(3)
        #Your Vehicle Rego State
        # Click the dropdown for Vehicle Rego State and select NSW
        page.click("#regoState")
        time.sleep(0.5)
        page.select_option("#regoState", "NSW")
        time.sleep(1)
        #Vehicle Registration Number:
        page.fill("input#registrationNumber", "DK36KT")
        time.sleep(1)
        #Check Vehicle Btn:
        # Click the Check Vehicle button
        page.click("#checkVehicle")
        time.sleep(1)
        #Insurance Details
        # Click the "Yes" option for Insurance Details where ID is vehicleInsuranceIsInsuredYes
        page.click("#vehicleInsuranceIsInsuredYes")
        time.sleep(1)
        #Insurer:
        # Click the Insurer field to open the dropdown
        page.click("#vehicleInsuranceInsurer")
        time.sleep(1)
        # Select the first option in the dropdown
        page.keyboard.press("ArrowDown")
        time.sleep(0.5)
        page.keyboard.press("Enter")
        time.sleep(1)
        # Click the first option in the dropdown
        #Claim Number:
        page.fill("#vehicleInsurancePolicyNumber", "111111")
        time.sleep(1)
        # Click the "Save and Continue" button
        page.click("#vehicleInsuranceSubmitBtn")
        time.sleep(2)



        #Page 3 Other Party Details:
        #First Name
        page.fill("input#otherPartyFirstName", "Johny")
        time.sleep(1)
        #Last Name
        page.fill("input#otherPartyLastName", "Johny")
        time.sleep(1)
        #Phone
        page.fill("#otherPartyPhone", "0412345678")
        time.sleep(1)
        #Insurance Details
        #Is At Fault Car Insured?
        # Click the "Yes" option if available
        page.click("#isInsuredYes")
        time.sleep(1)
        #Insurer
        # Click the Insurer field for the other party to open the dropdown
        page.click("#otherPartyInsurer")
        time.sleep(1)
        # Select the first option in the dropdown
        page.keyboard.press("ArrowDown")
        time.sleep(0.5)
        page.keyboard.press("Enter")
        time.sleep(1)
        #Claim Number
        # Input Claim Number where ID is otherPartyPolicyNumber
        page.fill("input#otherPartyPolicyNumber", "222222")
        time.sleep(1)
        #Vehicle Rego State
        page.select_option("#otherPartyRegoState", "NSW")
        time.sleep(1)
        #Vehicle Registration Number
        # Input Vehicle Registration Number where ID is otherPartyRegistrationNumber
        page.fill("#otherPartyRegistrationNumber", "DK36KT")
        time.sleep(1)
        #Click Check Vehicle:
        # Click the "Check Vehicle" button where the ID is checkVehicle
        page.click("#checkVehicle")
        time.sleep(1)
        #Address
        # Input Other Party Address where ID is otherPartyAddress
        page.fill("#otherPartyAddress", "SYDNEY, 16 GEMMA GLD, LABRADOR QLD 4215")
        time.sleep(2)
        # Wait for the address dropdown options to appear
        # Wait for the dropdown options to appear and click the first option
        page.wait_for_selector(".px-3.py-2.cursor-pointer.hover\\:bg-gray-100", timeout=5000)
        page.click(".px-3.py-2.cursor-pointer.hover\\:bg-gray-100")
        time.sleep(3)
        #Street Address
        #page.fill("input[name='otherPartyStreetAddress']", "16 GEMMA GLD")
        #time.sleep(1)
        #Suberb
        #page.fill("input[name='otherPartySuburb']", "LABRADOR")
        #time.sleep(1)
        #Postcode
        #page.fill("input[name='otherPartyPostcode']", "4215")
        #time.sleep(1)
        #Country
        #page.fill("input[name='otherPartyCountry']", "Australia")
        #time.sleep(1)
        #State
        #page.select_option("select[name='otherPartyState']", "QLD")
        #time.sleep(1)
        #Click and Continue Btn:
        # Click the Submit button for the Other Party section
        page.click("#otherPartySubmitBtn")
        time.sleep(2)



        #Page 4(Additional Information):
        #Have you already scheduled repairs for your damaged car?
        # Click the "No" button for "Have you already scheduled repairs for your damaged car?"
        # Adjust the selector if needed depending on the actual locator for "No"
        #page.click("button:has-text('No')")
        #time.sleep(1)
        #Click Yes Button
        # Click the "Yes" button for "Have you already scheduled repairs for your damaged car?"
        page.click("#repairsScheduledYes")
        time.sleep(1)
        #Who is the repairer?
        # Input the repairer name where its ID is 'repairer'
        page.fill("#repairer", "Smash Repair Shop")
        time.sleep(1)
        #What is the repair start date?
        page.fill("#repairStartDate", "12-12-2025")
        time.sleep(1)
        #Do You Require Any Vehicle Accessories or Have Any Special Requirements?
        page.click("#accessoriesOrRequirements")
        # Click on the checkbox with ID 'accessoriesOrRequirementsCheckbox
        page.click("#accessoriesOrRequirementsCheckbox")
        # Click the Enter button
        page.keyboard.press("Enter")
        # Driving license(Front Side) 
        #page.click("#frontLicense")
        #time.sleep(1)
        # Upload Driving License (Front Side) - update selector and file path as appropriate
        #page.set_input_files("input[type='file'][name='drivingLicenseFront']", "path/to/driving_license_front.jpg")
        # Click the Driving License (Back Side)
        #page.click("#backLicense")
        #time.sleep(1)
        # Upload Driving License (Back Side) - update selector and file path as appropriate      
        #page.set_input_files("input[type='file'][name='drivingLicenseBack']", "path/to/driving_license_back.jpg")
        #time.sleep(2)
        # Click Your Damaged Vehicle Photo ID: vehiclePhotoUpload
        #page.click("#vehiclePhotoUpload")
        # Upload Damaged Vehicle Photo - update selector and file path as appropriate
        #page.set_input_files("input[type='file'][id='vehiclePhotoUpload']", "path/to/damaged_vehicle_photo.jpg")
        #time.sleep(1)
        #Additional Supporting Document
        # Click the Additional Supporting Document dropdown
        #dropdown = page.locator("#additionalDocumentType")
        #dropdown.click()
        #time.sleep(1)
        # Select the first option in the dropdown
        #dropdown.press("ArrowDown")
        #time.sleep(0.5)
        #dropdown.press("Enter")
        #time.sleep(1)
        # Press the down arrow key to move selection
        #dropdown.press("ArrowDown")
        #time.sleep(0.5)
        # Press Enter to select the highlighted option
        #dropdown.press("Enter")
        #time.sleep(1)
        # Click on the choose file input with ID 'additionalDocumentChooseFile'
        #page.click("#additionalDocumentChooseFile")
        # Upload a photo ID for the 'additionalDocumentChooseFile' input
        # Update the file path as appropriate
        # Example file path: "path/to/photo_id.jpg"
        #page.set_input_files("#additionalDocumentChooseFile", "path/to/photo_id.jpg")
        #time.sleep(1)
        # Click the Review and Submit button
        page.click("#additionalInformationSubmitBtn")
        time.sleep(2)
        # Wait for "Your Claim ID" text to appear on the page
        page.wait_for_selector("text=Your Claim ID", timeout=30000)



        #Page 5(Application Overview):
        #Click Copy of the ID:

        #CLick Submit My Application button:
        page.click("#submitBtn")
        # Wait for the next page to appear after submitting the application
        # This waits for a selector/text expected on the next page (update as needed)
        page.wait_for_selector("text=Application Submitted", timeout=30000)



        #Thank You Page:
        # Click the Copy button for Claim ID
        page.click("#claimIdCopyButton")
        #Click Know Your Right Button
        # Click Know Your Right Button
        page.click("#knowYourRightsButton")
        # Wait for the URL to change to the target "your-rights" page
        page.wait_for_url("https://r2d-au-dev.vercel.app/your-rights", timeout=30000)



        #Your Right:
        # Click on "How It Works"
        page.click("text=How It Works")
        # Click About US
        page.click("text=About US")
        # Click FAQ
        page.click("text=FAQ")
        # Click Refer
        #page.click("text=Refer")
        # Click Check Eligibility
        page.click("text=Check Eligibility")
        # Click Articles
        page.click("text=Articles")


        browser.close()


if __name__ == "__main__":
    run()
