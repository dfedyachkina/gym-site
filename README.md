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

