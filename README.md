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



