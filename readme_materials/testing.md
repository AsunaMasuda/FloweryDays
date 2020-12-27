# Testing
## Table of Contents

1. [Manual Testing](#)
    - [Responsiveness](#responsiveness)

2. [Automated Testing](#)
    - [](#)

3. [Validators](#)
    - [](#)

4. [Compatibility and Responsiveness](#)
    - [](#)

5. [Other Testing](#)

6. [Bugs](#)


# Manual Testing
## Responsiveness
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | All the important services are accesible from nav bar| Don't need to scroll to find important information | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 
### Test conducted:
- Access each page in the site with different screen sizes by Google Dev Tool's Emulator and check the layout and format of site elements
### Result:
1. Navbar: I have the search bar to be collapsed for smaller than medium screen size (width < 992px) because search Bar with input field conflicted with other navbar components. 
'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
2. Home page: The image size responsiveness on Carousel at landing(home) page was adjusted by media queries.
### Verdict:
The bug is fixed. Test passed.

## Landing Page
### User Stories Tested:

### Test conducted:

### Result:

### Verdict:


## Navbar
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Footer
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Onlineshop
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Blog
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Cart
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Checkout & Checkout Success Page
### User Stories Tested:
### Test conducted:
- 
### Result:
- Boolean Field with crispy form template (`{{ order_form.is_gift_wrapping | as_crispy_field }}`) just rendered a checkbox and the default value `False`. So I 
### Verdict:

## SignIn/Login, Order History
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Profile, Order History
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Admin Product Management
### User Stories Tested:
### Test conducted:
### Result:
### Verdict: