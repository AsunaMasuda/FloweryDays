# Flowery Days

Ongoing research in the field of botany seems to indicate delightful things about flowers:
- Flowers can help heal the common cold.
- Flowers can help improve mood.
- Flowers improve memory.
- Flowers aid relaxation.
- Flowers increase energy.

[Flowery Days]() is an online flower shop, that offers not only flower bouquets, but also a bunch of individual flowers so that customers can create arrangements by themselves.  
The shop also publishes blog posts about flower arrangements, gardening and flowers/plants, where the site visitors can leave a comment.

<p align="center"><img src = "" width=900></p>

## Table of Contents

1. [UX](#ux)
    - [Project Goals](#goals)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [](#)
        - [](#)
        - [](#)
        - [](#)
        - [](#)
        - [](#)
    - [Features Left to Implement](#features-left-to-implement)
        - [Delete the data after the event date is passed](#delete-the-data-after-the-event-date-is-passed)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#database-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)

6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)


# UX
## Project Goals
### Target Audience
- 

### Visitor / User Goals
-

### Business Goals (Site Owner's Goals)
-

## User Goals
The target audience for this website is:
1. The site owner who wants to open an online shop where customers can purchase products safely
2. People who are interested in buying flowers and gardening products
3. People who are interested in gaining flower decoration and gardening tips and inspirations

The user goal is to have:

## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper     | Easily see what services are offered | Find the service I want to use |  
| Shopper     | All the important services are accesible from nav bar| Don't need to scroll to find important information | 
| Shopper     | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 

<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Easily register for an account | Have a personal account and be able to view my profile and ability to check order history |  
| Site User | Easily recover my password in case I forget it | Recover access to my account | 
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful | 
| Site Owner | Post a blog about flower arrangement and gardening | Give site visitors interesting information of flowers | 
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews | 
| Site User | Add comments to the blog posts | Write down my thoughts to the post | 

<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Search a product with keywords | Find the most appropriate products |  
| Shopper | Order the search results with the prices | Find the most appropriate products for the target price range | 
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing | 
| Shopper | Filter with a specific category of product | Easily find products in a specific category | 
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular by the other customers | 
| Site Owner | Easity add a new product | Make sure the online site has the latest lineups | 

<br/>

- Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product and the quantity |  
| Shopper | Automatically suggest to log in if I did not log in, when proceeding with checkout | Smoothly proceed with my purchase | 
| Shopper | See the purchase steps | Understand what process I am at in the purchase | 

<br/>

## Design
### Wireframes
Wireframes were created with [balsamiq](https://balsamiq.com/).
You can find the wireframes [here](https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/wireframe.md).

### Brand Identity
- Vision: Beautiful life surrounded by natures and flowers with your creativities.
- Mission: Provide a wide range of bouquets and flower arrangements that suit special occasion and moments in life which can be purchased with one click online. Be a wholesaler of individual flower bunches so the customers can enjoy flower arrangements themselves, without hassle to go to a physical shops.
- Values: 1.Happiness - Improve your happiness with the power of natures, 2.Elegance - Appreciate everything around you in everyday life, 3.Nature - Inspired by the natural world and its beauty, 4.Creative - Express your creativity in flower arrangements

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below. 

<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Colorpalette.png" width=900></p>

This pallet collects the earthy tones with luxuary shades, which the shop aims to have their brand image for. The `Twilight Lavender` and `Popster` colors give the site an elegant and vibrant atmosphere with keeping harmonies with the flowers. The `Champagne Pink` fills the gap between white and the other vivid colors, while giving the calm shades.

### Typography
To refrect the flower shop's brand identity, the typeface `Playfair Display` by Claus Eggers Sørensen that falls under serif font family was chosen for the website unless there is any additional specific font setting. `Playfair Display` falls under a classic typography called 'serif' font family which is great to be used when you want your brand to appear trustworthy and traditional. `Playfair Display` font has a mood of Elegance, Vintage, Classy and Stylish which matches the shop's branding. [This article](https://medium.com/@manahabibian/playfair-display-a-typographic-specimen-b311856700bd) by Mana Habibian says “Playfair Display is a classical typeface with a modern feeling that will give designs the elegance they need.”

- Icon: [FontAwesome]() is used for the main icon library accross the site.
- Favicon: I got the favicon by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Brand Logo
Logo design is the cornerstone in your brand identity and logo presents a company's name, product and brand. I used [Canva](https://www.canva.com/en_gb/) to create brand logo file. The font represents the brand value `elegance` and the image of a branch at the top was added to represent `Nature` brand value. 
<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/static/img/home/logo_flowery_days.png"></p>

<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
Flowery Days website is composed of 6 application: `home`, `blog`, `cart`, `checkout`, `products`, `profiles`.

## Landing Page (Home)
Landing Page is designed as a single page website to provide with enough information for the site visitor to understand what the business is about on this site. This page has minimal amount of information to make the site visitors make decisions and take next actions. The page compose of `Navbar`, `Carousel`, `About`, `Why Choose Us?`, `testimonials` and `Contact Form` section. As scrolling down on thie page, the elements are smoothly being placed by [wow.js](https://wowjs.uk/docs) animation effects to give a dynamic and sophisticated experience to the site visitors.

### Navbar
When site visitors landed on the page, the hight of the navbar is set as "165 px". I wanted to make the whole brand logo visible to make it memorable because the first view of the page is important that gives the first impressions of the site to the users. If you scroll down the navbar shrinks to the height of "100 px" and sticks at the top of the view, for easy navigations and wider views of content on the landing page. The brand logo which is placed at the left top also becomes the branch icon. 

Navbar contains a site menu, a `Search Box`, `Login button`, `Sign Up button`, `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `descriotion` field of Product Model, `name` field of Color Model and `name` field of Flower Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "OR" condition not "AND" when searching the keywords, meaning, if the search query was "Tulip Rose", the search result shows the product found using the keyword "Tulip" OR "Rose". Searching with "OR" condition is chosen in order not to limit the possibilities for the products the potential customers want to purchase.


### Carousel
At the top of the landing page, I placed carousels with beautiful photos of the flowers and the messages. This area is called "Above the fold" area and site visitors engage more with the content in "Above the fold".

### About Us & Why Choose Us?
`About Us` section explains what the business is and the history of the shop briefly to the site visitor.
`Why Choose Us?` section showcases three sales points of the shop presenting with icons.
Those two sections use the color of `Popstrat` and `Champagne Pink` from the color pallete for its background color that seamlessly matches the next section's background.

### Testimonial
A customer testimonial section can contribute to building the trust of potential customers and also explain the benefits of your products or services. This section displays different customer's testimonials with smooth carousel auto-animation effects.

### Contact Form
A simple contact form is placed at the end of the landing page. Site visitors fill out (name, email, subject, message) when submitting the form. An email with the inquery from the form will be sent to the admin of the website (handling by django send_mail() functionality).

### Footer
The footer section consists of two parts: 1. General information of the Shop and Quick Link, 2. Social Media icons and credit
1. The first footer section includes the shop address and its opening hours and quick links to the pages within the site.
2. In this milestone project, Social Media icons are linked to my personal social media accounts, but in real settting they should be linked to business pages on social media, such as Facebook, Instragram, Twitter, Pinterest etc, for social media marketing purposes.

## Product Page
### Online Shop Page
By clicking 'Online Shop' on the site menu, you can go to the online shop page. This page is filtered with 'Bouquet' category as a default as the shop owner wants to promote products that fall uner Bouquet category that has higher profit. However, the site visitor can adjust the filter condition very easily.  
- `Filter Function`: There is a filter section at the left side of the online shop page, and you can filter products with `categories`, `color`, `flower` and `occasion/use`. You can also select multiple choices within the filter option same and use several filters to get the results.(e.g. you can choose white and red for the color option and choose tulip and rose for the flower option. In this case, the result will show the products that fall under (white OR red color) AND (tulip OR rose).) I designed the filter to this way in order not to narrow down the products the potential customers are looking for.
- `Product Card`: The products are displayed in cards that have `Product Name`, `Price`, `Unit`, `Add to Card` button and `View Details` button when hoverovering the product image. If the user is logged in as a superuser, Edit / Delete option is also shown on each card. 
- `Pagination Bar`: At the bottom of this online shop page, I've set a pagination bar for easy navigation when there are many results to show. Setting up a pagination bar and limiting the number of the products reduce the loading time and make the site look more organized, which is crutial for a site like online shop which offers many products. 

### Product Detail Page
- `Product Image`: On the left side of the product detail page (single_product.html), the product images are shown. When there are several images for the product , for example, some products have color options such as Carnation, the options will be shown under the main image.
- `Product Information`: On the right side of the product detail page, there is `Product Name`, `Price`, `Description`, `Color` option, `Quantity`, `Add to Cart` button. `Color` option is only visible when the product has the options. Also for superuser, Edit / Delete option will be shown.
- `Product Review Section`: Customers can see the product scores and review messages by the other customers. The users can leave a score from 1 to 5, and the average of the scores by the customers is shown on the product page. To leave product review, the user is asked to log in their account. At the moment, regardless of the history of purchasing the product the user wants to review for, the user is able to leave a review. This is one of the features left to implement to limit only the user who actually purchased the product to be allowed to review.

## Cart Page
### 
### 

## Checkout Page
###
###

## Blog Page
###
###

## Profiles Page
###
###


## Features Left to Implement
### Delete the data after the event date is passed


## Defensive Design
-  
- 


# Information Architecture
## Database Choice
## Data Modeling


# Technologies Used
This application contains key CRUD functionalities and they are used to maximize user's experience in this site. The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Flask.

## Languages 
- HTML, CSS, JavaScript, Python

## Libraries
- Bootstrap (v4.4.1)
- JQuery
- JQuery-UI
- Popper.js
- Font Awesome
- Flask
- Jinja
- PyMongo

## Tools
- Git/GitHub
- Gitpod
- PIP
- MongoDB Atlas

## Databases


# Testing
### Validation Tools
I used these validation tools below for each file.
- HTML: [W3C HTML Validator](https://validator.w3.org/)
- CSS: [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- JavaScript: [JSHint](https://jshint.com/)
- Python: [PEP8 online](http://pep8online.com/)

### Formatter
- HTML: [HTML Formatter](https://webformatter.com/html)
- CSS: [CSS Formatter](https://webformatter.com/css)
- JavaScript: [Online JavaScript Beautifier](https://beautifier.io/)
- Python:[PEP8 online](http://pep8online.com/)

### Manual Testing

### Bugs
#### Python and Database
- 

#### JavaScript
- 

#### Browser Compatibility
- 
# Deployment
## Local Deployment
For local deployment, you need to have an IDE such as Gitpod and you need to install the following in your IDE:
- Git, Python3, PIP3

1. At the top of this repository, click the green button **Clone or download**.
2. In the Clone with HTTPs section, copy the clone URL for the repository. 
3. Open your favourite terminal (cmd, powershell, bash, git bash, etc.)
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type `git clone`, and then paste the URL you copied in Step 2:
   `git clone https://github.com/AsunaMasuda/MilestoneProject3.git`
6. Press Enter. Your local clone will be created.
7. You can either 
    - Create a virtual environment and create environment variables of IP, PORT, MONGO_URI and SECRET_KEY.
    - Or edit the app.py file like the following variables:
        ```
        'IP', '127.0.0.1'
        ```
        ```
        'PORT', '5000'
        ```
        ```
        'SECRET_KEY', '<somethingsecret>'
        ```
        ```
        'MONGO_URI', 'mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority'
        ```
8. Install all required modules from requirements.txt with the command`pip3 install -r requirements.txt`
9. Now you can run the website with the command `python3 app.py`
10. You can now access the website at **http://127.0.0.1:5000**

## Heroku Deployment
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Create a requirements.txt file using the command `pip3 freeze > requirements.txt` in the terminal.
2. Create a Procfile using the commant `echo web: python app.py > Procfile` in the terminal.
3. Commit and push all the changes to the Github repositoty of this project.
4. Go to Heroku and create a new app. Set a name for this app and select the closest region.
5. Choose Deployment method as GitHub in Heroku Dashboard and link the Github repository to the Heroku app.
6. Go to Settings then Reveal Config Vars in Heroku Dashboard and set the values as follows:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `<your_secret_key>`


# Credits

## Content
- All text within this project was written by the developer.

## Media
### Icons
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- Favicon is made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Images
- The favicon for this site is provided by [flaticon](https://www.flaticon.com/)

### UX
- 

### JavaScript
- 

## Acknowledgements
- Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.
