# Flowery Days

[![Build Status](https://travis-ci.org/AsunaMasuda/FloweryDays.svg?branch=master)](https://travis-ci.org/AsunaMasuda/FloweryDays)

Link to [Deployed Site](https://flowerydays.herokuapp.com/)

Ongoing research in the field of botany seems to indicate delightful things about flowers:
- Flowers can help heal the common cold.
- Flowers can help improve moods.
- Flowers improve memory.
- Flowers aid relaxation.
- Flowers increase energy.

[Flowery Days](https://flowerydays.herokuapp.com/) is an online flower shop, which offers not only flower bouquets, but also a bunch of individual flowers for flower arrangements so that customers can enjoy arrangements by themselves.  
The shop also publishes blog posts about flower arrangements, gardening and flowers/plants, where the site visitors can leave a comment.

<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/responsive_image.png" width=900></div>

This image is created with [ami.responsivedesign](http://ami.responsivedesign.is/).

## Table of Contents

1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Landing Page](#landing-page)
        - [Product Page](#product-page)
        - [Cart Page](#cart-page)
        - [Checkout Page](#checkout-page)
        - [Blog Page](#blog-page)
        - [Profiles Page](#profiles-page)
        - [Admin Product Managment](#admin-product-managment)
        - [Django allauth features](#django-allauth-features)
    - [Features Left to Implement](#features-left-to-implement)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#data-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Packages](#libraries-and-packages)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment with AWS](#heroku-deployment-with-aws)
    - [Local Deployment](#local-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)


# UX
## Project Goals
### Target Audience
- People who are looking to buy flowers / bouquets
- People who love flowers/botanies
- People who seek for presents for special occasions such as birthdays
- People who want to try to make a flower arrangement and decoration by themselves
- People who want to read interesting blog articles about flowers / botanies / gardening

### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by product reviews / product information
- Gain interesting knowledge about flowers from blog articles and leave a comment on blog articles

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand image
- Expand their business effectively
- Make profit from selling products / services

<div><a href="#table-of-contents">Back to top</a></div>

## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | Easily see what services are offered | Find the service I want to use |  
| Shopper | All the important services are accesible from nav bar| Don't need to scroll to find important information |
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want |

<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Purchase the same product again in the next order |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site Owner | Post a blog about flower arrangement and gardening | Give site visitors interesting information of flowers |
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews |
| Site User | Add comments to the blog posts | Write down my thoughts on the post |

<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Search a product with keywords | Find the most appropriate products |
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing |
| Shopper | Filter by a specific category | Easily find products in a specific category |
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular with other customers |
| Site Owner | Easily add a new product | Make sure the online site has the latest catalogue |

<br/>

- Cart, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily select the quantity and the color (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 

<br/>

<div><a href="#table-of-contents">Back to top</a></div>

## Design
### Wireframes
Wireframes were created with [balsamiq](https://balsamiq.com/) and [moqups](https://moqups.com/).
You can find the wireframes [here](https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/wireframe.md).

### Brand Identity
- Vision: Beautiful life surrounded by nature and flowers with your creativity.
- Mission: Provide a wide range of bouquets and flower arrangements that suit special occasions and moments in life which can be purchased with one click online. Be a wholesaler of individual flower bunches so the customers can enjoy flower arrangements themselves, without the hassle of going to a physical shops.
- Values: 1.Happiness - Improve your happiness with the power of nature, 2.Elegance - Appreciate everything around you in everyday life, 3.Nature - Inspired by the natural world and its beauty, 4.Creative - Express your creativity in flower arrangements

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create a natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below.

<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Colorpalette.png" width=900></p>

This pallet collects the earthy tones with luxury shades, which the shop aims to have as their brand image. The `Twilight Lavender` and `Popster` colors give the site an elegant and vibrant atmosphere while keeping harmony with the flowers. The `Champagne Pink` fills the gap between white and the other vivid colors, while giving calmer shades.

### Typography
To reflect the flower shop's brand identity, the typeface `Playfair Display` by Claus Eggers Sørensen that falls under serif font family was chosen for the website unless there is any additional specific font setting. `Playfair Display` falls under a classic typography called 'serif' font family which is great to use when you want your brand to appear trustworthy and traditional. `Playfair Display` font has a mood of Elegance, Vintage, Classy and Stylish which matches the shop's branding. [This article](https://medium.com/@manahabibian/playfair-display-a-typographic-specimen-b311856700bd) by Mana Habibian says “Playfair Display is a classical typeface with a modern feeling that will give designs the elegance they need.”

- Icon: [FontAwesome](https://fontawesome.com/) is used for the main icon library accross the site.
- Favicon: I got the favicon by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Brand Logo
Logo design is the cornerstone in your brand identity and presents a company's name, product and brand. I used [Canva](https://www.canva.com/en_gb/) to create the brand logo file. The font represents the brand value `elegance` and the image of a branch at the top was added to represent `Nature` brand value.
<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/static/img/home/logo_flowery_days.png"></p>

<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
This website is composed of 6 applications: `home`, `blog`, `cart`, `checkout`, `products`, `profiles`.

## Landing Page
Landing Page is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions. The page compose of `Navbar`, `Carousel`, `About`, `Why Choose Us?`, `testimonials` and `Contact Form` section. As scrolling down on thie page, the elements are smoothly being placed by [Animate.css](https://animate.style/) and [wow.js](https://wowjs.uk/docs) animation effects to give a dynamic and sophisticated experience to the site visitors.

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `Site Menu`, `My Account dropdown` and `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `descriotion` field of Product Model, `name` field of Color Model and `name` field of Flower Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "OR" condition not "AND" when searching the keywords, meaning, if the search query was "Tulip Rose", the search result shows the product found using the keyword "Tulip" OR "Rose". Searching with "OR" condition is chosen in order not to limit the possibilities for the products the potential customers want to purchase.
- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: The number next to the cart icon shows the total of items added to the cart.


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/navbar_large_screen.png" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/navbar_small_screen.png" width=900></div>

Navbar for authenticated users
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/authenticated_navbar.png" width=900></div>

### Carousel
At the top of the landing page, I placed carousels with beautiful photos of the flowers and messages. This area is called the "Above the fold" area and site visitors engage more with the content in "Above the fold".
Three different images and messages are used in the carousel with call-to-action buttons that link to three different services in the site: `Online Shop`, `Blog`  and `Inquery (Contact Form)`. This way, the users can easily access the page they look for and also the business owners can maximize the sales opportunities.

<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/carousel_readme.png" width=700></div>

### About Us & Why Choose Us?
`About Us` section explains what the business is and the brief history of the shop to the site visitor.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/aboutus.png" width=700></div>

`Why Choose Us?` section showcases three sales points of the shop with icons representing each one.
Those two sections use the color of `Popstrat` and `Champagne Pink` from the color pallete for its background color that seamlessly matches the next section's background.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/why_choose_us.png" width=700></div>

### Testimonial
A customer testimonial section can contribute to building the trust of potential customers and also explain the benefits of your products or services. This section displays different customer's testimonials with smooth carousel auto-animation effects.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/testimonial.png" width=700></div>

### Contact Form
A simple contact form is placed at the end of the landing page. The email address field is prefilled if the users are logged into their account. Site visitors will fill out fields `name`, `email`, `subject` and `message` when they submit the form. An email with the inquiry from the form will be sent to the admin of the website (handling by django send_mail() functionality).
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/contactform.png" width=700></div>

### Footer
The footer section consists of two sections: 1. General information of the Shop and Quick Link, 2. Social Media icons.
1. General Info and Quick Links: The first footer section includes the shop address and its opening hours and quick links to the pages within the site.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/footer1.png" width=700></div>

2. Social media icons: In this milestone project, Social Media icons are linked to my personal social media accounts, but in a real settting they should be linked to business pages on social media, such as Facebook, Instragram, Twitter, Pinterest etc, for social media marketing purposes.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/footer2.png" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

## Product Page
### Online Shop Page
By clicking 'Online Shop' on the site menu, you can go to the online shop page. This page is filtered with 'Bouquet' category as a default as the shop owner wants to promote products that fall uner Bouquet category that has higher profit. However, the site visitor can adjust the filter condition very easily.  
- Product Filter: There is a filter section at the left side of the online shop page, and you can filter products with `categories`, `color`, `flower` and `occasion/use`. You can also select multiple choices within the same filter option and use several filters to get the results.(e.g. you can choose white and red for the color option and choose tulip and rose for the flower option. In this case, the result will show the products that fall under (white OR red color) AND (tulip OR rose).) I designed the filter this way in order not to narrow down the products the potential customers are looking for.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/product_filter.png" width=250></div>

- Result Number: It's shown above the product cards. Customers can see how many results were found in total at a glance.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/result_number.png" width=350></div>

- Product Card: The products are displayed in cards that have `Product Name`, `Price`, `Unit`, and `View Details` button when hovering ove the product image. `Add to Cart` button addes the product with 1 quantity to the cart and this button only appears for bouquet category, because the other product categories have color options, so the customers have to access the product detail page. If the user is logged in as a superuser, Edit / Delete option is also shown on each card.

Product Card for Bouquets
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/bouquet_product_card.png" width=500></div>

Product Card for Flowers
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/flower_product_card.png" width=250></div>

- Pagination Bar: At the bottom of this online shop page, I've set a pagination bar for easy navigation when there are many results to show. Setting up a pagination bar and limiting the number of the products reduce the loading time and make the site look more organized, which is crucial for a site like which offers many products for sale.

### Product Detail Page
- Breadcrumb: Breadcrumb navigation is added at the top of the product detail page, which allows customers to keep track of their locations in the online shop.
- Product Image: On the left side of the product detail page (single_product.html), the product images are shown. When there are several images for the product, for example, some products have color options such as Carnation, the options will be shown under the main image.
- Product Information: On the right side of the product detail page, there is a `Product Name`, `Price`, `Description`, `Color` option, `Quantity`, `Add to Cart` button. `Color` option is only visible when the product has the options. Also for superuser, Edit / Delete option will be shown.
- Product Review Section: Customers can see the product scores and review messages by other customers. The users can leave a score from 1 to 5, and the average of the scores of the customer reviews is shown on the product page. To leave a product review, the user is asked to log in to their account. Also, to delete a review, the customer who left the review needs to log in and the delete option will be visible next to the review after logging in. At the moment, regardless of whether they have purchase history or not, the user is able to leave a review. This is one of the features left to implement to limit it so only the user who actually purchased the product will be allowed to review.

<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/product_detail.png" width=700></div>


## Cart Page
- The left side of this cart page shows the products added to the cart. Customers are able to change the quantity or remove the products in this cart page.
- On the right side of this cart page, there is an Order Summary section that shows `Cart Total`, `Delivery` and `Grand Total`. This way, customers are able to check the order summary at first glance even if they have added a lot of products to the shopping cart.

<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/shopping_cart.png" width=700></div>

## Checkout Page
### Checkout Page
- On the checkout page, customers are asked to fill in delivery details. The customer can also select if they want gift wrapping for the product or not. At the moment, this shop does not collect user's billing information within the User Profile model or Order model.(However, the billing data is recorded in Stripe from the billing information added by the customer.) One of the features left to implement is to add the billing details on the Checkout page.
- Though the customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown at the checkout page.

### Checkout Success Page
- A thank you message will be displayed after the checkout process as well as the table that holds the order details.
- `Keep Shopping` button is placed at the end of the page, and if the customer has been logged into their account, `Back to Profile` will be shown.

<div><a href="#table-of-contents">Back to top</a></div>

## Blog Page
### Blog Feed Page
- After clicking `Blog` on the site menu at the top, Blog Feed page is loaded. On this page, blog posts will be displayed in descending order by the posted date. To display the blog posts beautifully, the layout that shows posts in 2-1-2 order was chosen. `Pagination Bar` is also added at the end of the page.
- On the left side of this page, I created categories of blog posts so the site visitors can navigate the blog posts easily. The number of posted blogs in the categories is also shown in brackets.

### Blog Post Detail Page
- `Breadcrumb` navigation is added at the top of the blog post detail page for easy navigation.
- `Leave Comment` function: Site visitors are able to leave comments on blog posts. It requires the visitors to log into their account to do so. Also, after logging in, they can delete comments they left in the past with the delete option shown next to their comment(s).
- If user is logged in as superuser, they can see the choice of edit/delete at the top of the page.

<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/blog_article.png" width=700></div>

### Add/Edit Blog
- If user is logged in as superuser, they can access to Add / Edit Blog post page. This page is combined with two forms `BlogForm` and `BlogImageForm`.

## Profiles Page
`My Profile` page is available for authenticated users and will be shown in the `My Account` Dropdown menu at the navbar which appears when you log into your account.
### My Profile Page
- In Profile Page, authenticated users can 1. edit `Delivery Information` and 2. see `Order History`.

## Admin Product Managment
Only authenticated superusers can access the admin page (1.products/add/, 2. products/edit/, 3. products/delete/, 4. 5. 6. ). If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

## Features Left to Implement
There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.
### 1. Limit the user who can leave product review
At the moment, all the authenticated users can leave reviews to any products if they are logged in. It should be limited to those who actually purchased the product for the validity of the reviews.
### 2. Sort the search/filter results by the prices, or other conditions
This function would be very helpful when there are many products in results. This was not implemented this time due to the time constraints and there are not that many products used in this project.
### 3. Add an option to let the customer add their billing information
With the current checkout process, the user is asked to fill out delivery information. Billing information is required when the customer wants a receipt or when a billing address is different from a delivery address.
### 4. When a color was selected on a product page, the product image also changes accordingly
At the moment, even though the color options and images for each color are shown on its product page, these two are not changed if the other is changed. It would be more ideal if the action of those two elements is synced.
### 5. Social Account Login
This function allows users to sign up / log into their account of the site, using an existing third party account such as Google and Facebook. This is beneficial to users and the site owners. For users, it's hassle free for remembering a password for the site and it gives the users a smooth registration process. For the site owners, there are many benefits gained by social login - such as increasing user sign ups, reducing bounce rate and gaining a user's social account details which is beneficial for marketing purpose.
### 6. Linking a related product page to blog post
To call more customers to purchase a product, it would be effective to link a product page which is related to a blog post theme.
### 7. Social Media Share Icons
For social media marketing purpose, adding a social media icon with a link to share products and blog posts would be effective.
### 8. Order Tracking System
To keep the customers informed with the status of their purchase, it would be nice if the site provides the order status such as shipment information in order history and email notifications.

## Defensive Design
### Error views (404 and 500 error)
If 404 and 500 error occured within the site, a page that has the message of the error and 'Back to Home' button so that the user would not be lost. The templates of 404.html and 500.html are added to [the root template directory](https://docs.djangoproject.com/en/3.1/ref/views/))

### Form Validation
- Django Form Validation

### Product Quantity Counter Validation
- The

<div><a href="#table-of-contents">Back to top</a></div>

# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

## Data Modeling
Following is Entity Relationship Diagram of this project. I created this diagram with [dbdiagram.io](https://dbdiagram.io/home).
When I designed this ERD, I referred to [this article](https://launchschool.com/books/sql/read/table_relationships). 
<p align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/Entity_Relationship_Diagrams.png?raw=true" width=900></p>

I made fixtures for `Product`, `Color` ,`Image` and `Flower` models on Google sheet (.csv file) first, and used [this tool](https://json-csv.com/reverse) to .json file.

### Product App
A bouquet could have several types of flowers and multiple colors. For example, below the product 'Floral Fantasy' has `Delphinium`, `Rose`, `Tulip` and `Tistle` for its flowers and it can be categorized as `Red` and `Orange`. To give customers a better search experience, meaning not to narrow down the search results with the search keyword, I wanted to enable customers to search/filter bouquets with their flower type(name) or their color. For example, if a customer uses a filter `tulip`, bouquets that contains `tulip` (such as the 'Floral Fantasy') and also individual tulip flower product (not bouquet) will be shown. Therefore, separated models `Product`, `Flower`, `Color` are created and connected inbetween. `Image` model is connected to `Product` model because some products could have several product images. Also `Image` model is connected to `Color` model, because each product image should a product that could have mutiple colors. There might have been a better implementation than this scheme, but at the time, this was the best idea I had.
<p align="center"><img src = "https://raw.githubusercontent.com/AsunaMasuda/FloweryDays/master/readme_materials/Product_model.png" width=900></p>

### Order App
`Order` model collects the delivery information, stripe_pid and order information. All the fields except `user_profile` field have `null=false`. The reason why `user_profile` does not have `null=false` is that guest customers (not authenticated users) can also purchase products and complete the checkout process without creating an account. `Order` model is connected to `OrderLineItem` model which collects information of purchased products.

### Blog App
`BlogPost` model has the essential information for blog post, such as a title, author, content, created date. This model is connected to `User`, `BlogImage` and `BlogComment`.

### Profile App
`Profile` is used for my profile page where the authenticated users can see their delivery details and their order history.

<div><a href="#table-of-contents">Back to top</a></div>

# Technologies Used
The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [JQuery-UI](https://jqueryui.com/)
- [Popper.js](https://popper.js.org/)
- [Font Awesome](https://fontawesome.com/)
- [Animate.css](https://animate.style/)
- [Wow.js](https://www.delac.io/wow/)
- [Stripe](https://stripe.com/ie)
- [Google Fonts](https://fonts.google.com/)

## Tools
- Git/GitHub
- Gitpod
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [dbdiagram.io](https://dbdiagram.io/home)
- [AWS S3 bucket](https://aws.amazon.com/)

## Databases
- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.

# Testing
Testing was conducted and recorded in a different file: [Testing.md](https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/testing.md).

<div><a href="#table-of-contents">Back to top</a></div>

# Deployment
## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

* I used [Djecrety](https://djecrety.ir/) to generate Django Secret Key.

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
10. Load the data fixtures(color_table, flower_table, image_table, product_table) into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
13. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
14. Add `'flowerydays.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
15. In Stripe, add Heroku app URL a new webhook endpoint.
16. Update the settings.py with the new Stripe environment variables and email settings.
17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.

### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'flowerydays'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/AsunaMasuda/FloweryDays/blob/master/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

1. In the IDE you are using, copy and paste the following commane into the terminal to clone this repository.
    `git clone https://github.com/AsunaMasuda/FloweryDays.git`
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Load the data fixtures(color_table, flower_table, image_table, product_table) into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`

<div><a href="#table-of-contents">Back to top</a></div>

# Credits

### Content & Code
- I constantly read [Django](https://docs.djangoproject.com/en/3.1/), [Stripe](https://stripe.com/docs) and [Python](https://docs.python.org/3/) documenation and tutorial throughout the development.
- For `Blog` app, I referred to [this tutorial](https://djangocentral.com/building-a-blog-application-with-django/).
- I refered to [this code snippet](https://bootsnipp.com/snippets/k2RdV) for the Testinonial section on the landing page.
- For search product function, I refered to several articles and video. [Stack Overflow 1](https://stackoverflow.com/questions/3171717/django-search-for-strings-containing-spaces), [Stack Overflow 2](https://stackoverflow.com/questions/34831511/django-prefetch-related-failing-to-pass-data-to-template), [Stack Overflow 3](https://stackoverflow.com/questions/3171717/django-search-for-strings-containing-spaces), [Combine 2 Django Querysets from Different Models](https://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/), [Django Queryset:value_list() flat=True](https://amittbhardwj.wordpress.com/2015/10/27/django-querysetvalue_list/).
- For the hover show button on the product card, I refered to this [code snippet](https://codepen.io/philcheng/pen/YWyYwG).
- For multiselect dropdown menu which is used for the product filter function, I referred to these article: [Stack Overflow 1](https://stackoverflow.com/questions/50895806/bootstrap-4-multiselect-dropdown/50897096), [bootstrap-select](https://developer.snapappointments.com/bootstrap-select/).
- For creating custome template tags used in `Blog` and `Product` apps, I refered to [this video](https://www.youtube.com/watch?v=XtbvBlCyfT4).
- This project was developed refering to the Boutique Ado Django mini-project from Code Institute course materials. The codes are customized and modified to fit the purpose of this milestone project.

### Images & Media
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- Favicon is made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).
- The credits for the images used in this site can be found in this [separated file](https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/image_credit.md).
- To compress the image size, I used [tinypng](https://tinypng.com/).

### Acknowledgements
- Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.

### Disclaimer
This website is created for educational purpose only.
