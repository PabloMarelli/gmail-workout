import yagmail
import argparse
import datetime
import workout_program

# argparse setup
parser = argparse.ArgumentParser(description="CLI for the Globo workout application.")
parser.add_argument("--username", type=str, help="The gmail address from which the emails will be sent (xxx@gmail.com)", required=True)
parser.add_argument("--app_password", type=str, help="Your gmail app password to sign into the sender account.", required=True)
parser.add_argument("--recipients", type=str, help="A comma separated list of one or more recipient email addresses.", required=True)


CURRENT_WORKOUT = workout_program.WORKOUT


if __name__ == "__main__":
    # Parse the command line arguments
    args = parser.parse_args()
    
    # Get today as a weekday integer
    today = datetime.datetime.today().weekday()

    # See if today is a workout
    if today in CURRENT_WORKOUT.keys():
        # Get workout
        workout = CURRENT_WORKOUT.get(today)
        subject = f"WORKOUT: {workout.name}"
        # Handle newlines in html (yagmail v0.14.245 see https://github.com/kootenpv/yagmail/issues/116)
        contents = [workout.as_html().replace("\n", "")]
        
        # Send to recipients
        with yagmail.SMTP(user=args.username, password=args.app_password) as yag:
            for recipient in args.recipients.split(','):
                yag.send(to=recipient, subject=subject, contents=contents)
        

# Run command
# pipenv run python runner.py --username ORIGIN_MAIL --app-password $APP_PASSWORD --recipients RECIPIENT_MAIL