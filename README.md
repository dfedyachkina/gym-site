# [gym-site](https://the-welness-hub-9673efabce1f.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/dfedyachkina/gym-site)](https://www.github.com/dfedyachkina/gym-site/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/dfedyachkina/gym-site)](https://www.github.com/dfedyachkina/gym-site/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/dfedyachkina/gym-site)](https://www.github.com/dfedyachkina/gym-site)


![screenshot](documentation/mockup.png)

source: [gym-site amiresponsive](https://ui.dev/amiresponsive?url=https://the-welness-hub-9673efabce1f.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide gym admins with tools to create, manage, and moderate information on home page, memeberships, contact us form and accounts management.
- Provide gym members with tools to easily register, manage their membership, book appointments with personal trainers, and view/manage upcoming appointments.
- Offer non-member visitors the ability to explore gym services, membership plans, and contact the gym for inquiries.
- Allow seamless user registration and login for personalized access to gym services.
##### Primary User Needs
- Gym admins need seamless tools for managing accounts, managing memberships, changing memberships, changing home page information.
- Gym members need the ability to request a new memebership and to book an appointment with the personal trainer and to manage his apppointments.
- Non-members/registred users need the ability to requset a memebership.
- Guests need the ability to see gym's information, ability to register, see offered meberships and fill up the form in Contact us section.

##### Business Goals
- Improve Member Engagement: Enable gym members to easily manage their memberships and appointment schedules, improving their experience and engagement with the gym
- Increase Membership Sign-Ups: Provide clear information on membership options, benefits, and an easy sign-up process to increase new memberships.
- Streamline Appointment Booking: Offer an intuitive and straightforward process for booking and managing personal training sessions.
- Simplify Administration: Ensure gym admins have the tools to manage appointments, user accounts, and membership data efficiently.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Gym infromation:
    - Details about the gym.
    - Clear breakdown of membership plans, what’s included in each plan, and pricing.
- Membership & Appointment Pages:
    - Information on how to request a membership, available membership plans, and benefits.
    - Pages dedicated to booking and managing personal training sessions, with an easy-to-use interface for selecting times and trainers.
- User Dashboard (For Members):
    - A personalized dashboards for members to manage their membership and appointments.
    - A list view of upcoming personal training appointments.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Memeberships, Book an appointment(for user members), My appointments(for user memebers), Contact Us, Login/Register/Log out.
- **Hierarchy**:
  - Home page contains the information about the gym and reasons why the guest should join their gym.
  - Membership page contains the ifnformation about current memebership's plans, benefits and allow to the registred user to request the desired memebership.
  - Book an appointment page contains the form through which a user memeber can book appointment with a personal trainer.
  - Contact us page containts the gym's contact and the form through which user can request to contact him and leave the question.
- **Footer**:
    - Footer contains Copyright and the information by who this site has been build.
    - Footer contains social media's icons with links to social medias.

##### User Flow
1. Guest users browse home page content → see the carousel and read the gym's information.
2. Guest users browse memebership page → see the current memebership's plans.
3. Guest users request memebership → the page requests the user to log in, because only registred users can request memebership.
4. Guest users browse contact us page → see the contact of the gym and fill up the full form "Contact Us".
5. Guest users submit Contact Us form → receive a massage that form has been sent.
6. Guest users register for an account → log in to request memebership.
7. Registered users(non-members) requests memebership → receive a success message that request has been received successfully.
8. Registered users(members) book an appointment → receive a success message that his appoinment has been done and redirect to his appointment list.
9. Registered users(members) edit or delete appointment → receive the message that his appointment has been updated/deleted successfully. 
10. Gym admin changes content of home page and carousel's images → all changes go to home page immediately.
11. Gym admin changes memebership's plans and benefits → all changes go to memebrship page immediately.
12. Gym admin approves the membership's requests → a memebership assigns to requsted user immediately.
13. Gym admin changes gym's contacts on contact us page → all changes go to contact us page immediately.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme


I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#212529` primary text.
- `#0F6E0A` primary highlights.
- `#212529` secondary text.
- `#0F6E0A` secondary highlights.

![screenshot](documentation/coolors.png)

### Typography

- [Newsreader](https://fonts.google.com/specimen/Newsreader?query=Newsreader) was used for the primary headers and titles.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories


| Target | Expectation | Outcome |
| --- | --- | --- |
| As a gym admin | I would like to change home page's content and change carousel images | so that I can share updated information with the users. |
| As a gym admin | I would like to approve memebership's requests | so that I can manage who owes membership and has additional access to gym's sources and who doesn't. |
| As a gym admin | I would like to change membership's plans | so that I can keep updated memeberships, benefits and prices. |
| As a gym admin | I would like to change gym's contact on contact page | so that I can keep updated contacts of the gym. |
| As a gym admin | I would like to have access to sent contact forms | so that I can contact the users which sent the contact form. |
| As a registered user(members) | I would like to have access to book an appointment page | so that I can book an appointment with a personal trainer |
| As a registered user(members)| I would like to have access to my appointment list | so that I can manage my appointments, edit them or delete. |
| As a registered user(members) | I would like to request another memebership | so that I can change my membership. |
| As a registered user(non-members) | I would like to request a memebership and receive a message that my request has been sent | so that I can be a member of the gym, have access to additional gym's sources and understand my request has been sent to the administrator. |
| As a registered user | I would like to log out | so that I can easily sign out from the site. |
| As a guest user | I would like to see information on home page | so that I can read about the gym and know updated information. |
| As a guest user | I would like to access to memeberships | so that I can see what memeberships are offered by the gym. |
| As a guest user | I would like to send contact us form and recieve a success message | so that I can understand the form has been sent and I would be contacted soon. |
| As a guest user| I would like to register an account | so that I can request memebership and become a member. |
| As a guest user | I would like to log in with exicted account | so that I can log in to my exicted account and have additional access. |

## Wireframes


To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Sign Out | ![screenshot](documentation/wireframes/mobile-sign-out.png) | ![screenshot](documentation/wireframes/tablet-sign-out.png) | ![screenshot](documentation/wireframes/desktop-sign-out.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Membership | ![screenshot](documentation/wireframes/mobile-membership.png) | ![screenshot](documentation/wireframes/tablet-membership.png) | ![screenshot](documentation/wireframes/desktop-membership.png) |
| Book an appointment | ![screenshot](documentation/wireframes/mobile-book-appointment.png) | ![screenshot](documentation/wireframes/tablet-book-appointment.png) | ![screenshot](documentation/wireframes/desktop-book-appointment.png) |
| My appointments | ![screenshot](documentation/wireframes/mobile-my-appointments.png) | ![screenshot](documentation/wireframes/tablet-my-appointments.png) | ![screenshot](documentation/wireframes/desktop-my-appointments.png) |
| Contact Us | ![screenshot](documentation/wireframes/mobile-contact-us.png) | ![screenshot](documentation/wireframes/tablet-contact-us.png) | ![screenshot](documentation/wireframes/desktop-contact-us.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## Features
       
### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Navbar | Users can navigate between pages, log in, register and log out from an account | ![screenshot](documentation/features/navbar.png) |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Home | The homepage displays carousle of images and gym's information. | ![screenshot](documentation/features/home.png) |
| Membership| Users can view all offered memeberships | ![screenshot](documentation/features/membership.png) |
| Request memebership | When user requests memebership he gets the poup with confirmation | ![screenshot](documentation/features/popup-memebership.png) |
| Success message of requested membership | The success message appers when the user requested a mebership | ![screenshot](documentation/features/success-message-membership.png) |
| Book an appointment | Authenticated members users can view this page and book an appointment with a personal trainer | ![screenshot](documentation/features/book-appointment.png) |
| Success message of created appointment | Authenticated mebmers users can see this message when they've created appointment. | ![screenshot](documentation/features/success-message-create-appointment.png) |
| My appointments | Authenticated members users can view this page and mange their appointments | ![screenshot](documentation/features/my_appointments.png) |
| Edit appointment | Authenticated members users can edit their appointment and receive the success message once the appointment is updated | ![screenshot](documentation/features/success-message-update-appointment.png) |
| Delete appointment | Authenticated members users can delete their appointment and receive the success message once the appointment is deleted| ![screenshot](documentation/features/success-message-delete-appointment.png) |
| Contact Us | Visitors and authenticated users can see this page and submit the form | ![screenshot](documentation/features/contact-us.png) |
| Success message of submiting contact form | Visitors and authenticated users can see submit the form and receive success message| ![screenshot](documentation/features/success-message-contact-us-form.png) |
| Footer | Users can see by who this site has been built and the social medias of the gym| ![screenshot](documentation/features/footer.png) |
| Manage carousel | Gym admin can edit, delte and add new images to carousel from Django admin dashboard| ![screenshot](documentation/features/admin-carousel.png) |
| Manage home text | Gym admin can edit, delte or add text to home text from Django admin dashboard | ![screenshot](documentation/features/admin-home-text.png) |
| Manage Memberships  | Gym admin can edit, delete or add memberships from Django admin dashboard| ![screenshot](documentation/features/admin-membership.png) |
| Manage Membership requests  | Gym admin can approve, deny or put on pending membership requests from Django admin dashboard| ![screenshot](documentation/features/admin-membership-requests.png) |
| Manage Benefits  | Gym admin can edit, delete or add benefits from Django admin dashboard| ![screenshot](documentation/features/admin-benefits.png) |
| View submitted contact forms  | Gym admin can view submitted contact forms from Django admin dashboard| ![screenshot](documentation/features/admin-view-contact-forms.png) |
| Manage gym contacts | Gym admin can change gym contacts from Django admin dashboard| ![screenshot](documentation/features/admin-gym-contacts.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features



- **User Profiles**: Create personalized user profiles where authenticated users can view their user's information and edit this information.
- **See the available hours of personal trainer**: Enable users to see the available slots of a personal trainer and book available slots.
- **Email confirmation**: When user edit his account, book an ppointment, delte it or edit - her receives a mail.
- **Online payment**: Enable users to pay memebership via site.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Gym blog**: Provide the user to read articles about how to eat more healthy, workout tips etc.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |


## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)


I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER {
        int id
        string username
        string email
        string first_name
        string last_name
        choices gender
        date date_of_birth
        boolean is_member
    }
    MEMBERSHIP {
        int id
        string membership_type
        date start_date
        date end_date
    }
    MEMBERSHIPREQUEST {
        int id
        dateTime requested_on
        string status
    }
    APPOINTMENT {
        int id
        dateTime appointment_date
        choices gender
        string note
    }
    CONTACTUS {
        int id
        string first_name
        string last_name
        string email
        string phone_number
        text message
        dateTime submitted_on
    }

    USER ||--o| MEMBERSHIP: has
    USER ||--o| MEMBERSHIPREQUEST: requests
    USER ||--o| APPOINTMENT: schedules
    USER ||--o| APPOINTMENT: conducts
    USER ||--o| CONTACTUS: submits
    MEMBERSHIPREQUEST ||--o| USER: belongs_to
    APPOINTMENT ||--o| USER: for_member
    APPOINTMENT ||--o| USER: for_trainer
    CONTACTUS ||--o| USER: for_user
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqNU8luwjAQ_RXLZ_gB3yiNVA4sJeFSRYqceEisxnbqRSoC_r1OEyAQCPjiWd7M88x49jhTDDDBoN85zTUVsUT-bMJgjfaNXB8uLeLsohurucyRM6AlFdBzgKC8vFhTpUqgEnGTCBAp6MZ1bK55MH8L1uHHbPUCZRNvCl4ldld1mBm14EFU26QWbxwgWcfcI14Hn5sgjIb46-iIC0AafhwYCyxRsvc8_wDrzBXLZLVazhbRPFi8lp9WlfJOAfK2kscc0-UimkyjTTjEYOHX-v4ZQ3O4w2tcKrjt1uWTd77D4TAeq0OnaQQV1AwB2q6SU8vugDvNIchkBTBXwjNcpiRz2b105z6QthzzaNJtQB1MUAqlkrlJrOqP7Aq4VfrqBw8CraZcnpCXCfVw9RbVIDzCArTfHOYX8n-OMbYF-PXCxIuM6u8Yx_LocdRZFe5khonVDkZYK5cXmGxpabzmqnqo7UKfrRWVX0qd9OMfJlc3gg)


I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects


[GitHub Projects](https://www.github.com/dfedyachkina/gym-site/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/dfedyachkina/gym-site/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/dfedyachkina/gym-site)](https://www.github.com/dfedyachkina/gym-site/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/dfedyachkina/gym-site)](https://www.github.com/dfedyachkina/gym-site/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://the-welness-hub-9673efabce1f.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.


| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.


Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/dfedyachkina/gym-site).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/dfedyachkina/gym-site.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/dfedyachkina/gym-site)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/dfedyachkina/gym-site).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits


### Content


| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |

### Acknowledgements
- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

