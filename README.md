# Polling Magic

Polling Magic is a website desgined to gather and display information about the Magic: The Gathering fanbase. The purpose of this site for the user is to be able to like/dislike and discuss current rotating sets as part of the standard game mode in Magic: The Gathering.

## User Stories

- As a site user I can view the current opinions of other users on the latest Magic set posts so that I can select and view one.
- As a user I can register an account so that I can comment and like/dislike set posts.
- As a user I can see the like/dislike ratio of each set post on the site.
- As a user I can register a unique account so I can comment and like on each set.
- As a user I can like or dislike a set post so that I can contribute to the opinion of the fan base on the site.
- As a user I can leave comments on a post so that I can be involved in the conversation.

## UX

Polling Magic was created as a space for the Magic community to have a resonable discourse about Magic: The Gathering sets. Its secondary function is to illustrate to the marketing, creative and all other relavant departments at Magic: The Gathering how thier products and services are being received by their target audience. In the future, sourcing consumer satisfication could be made a whole lot easier and streamlined thanks to sites such as this.

### Colour Scheme

The `#ff8800` orange colour was utilised as it is similar to the colour of the orginal Magic: The Gathering logo font. This original logo served as inspiration for the colour scheme. This colour was used in headings, menu bar, footer and in the logo.

A white colour `#ffffff` was used for most of the text on the site, primarily for the `<p>` sections. It was also used in the footer for social media icons and to highlight the form link.

The black colour `#f0f0f0` was used as a background colour primarily. It is found in the header and footer as a background colour and serves as an excellent contrast for the orange `#ff8800` colour. 

### Typography

The eczar font looks similar to the belern font used in Magic: The Gathering products and logos. Since the belern is a copyrighted font and cannot be used outside of Magic: The Gathering products, eczar was the font selected as most appropriate.

[Eczar](https://fonts.google.com/specimen/Eczar)

Rubik was the other font used throughout the site, in the main body of each section. It's simple and elegant structure was what made it suitable to use as a font, and was important when implementing a simplistic design for the site.

### Lucid Charts

- Main Page Lucid Chart
![Lucid Chart Main Page](documents/lucid-charts/poll_magic.png)

- Poll Page Lucid Chart
![Lucid Chart Poll Page](documents/lucid-charts/post_magic.png)

## Features

### Existing Features

- __Polls__

- Polls are the primary feature of this site. Their purpose is to portray to the user the popularity of any given Magic: The Gathering set.
- They are showen in list form to the user, and illustrate the amount of likes, comments, lore and release date of any given set on the site.

- __Likes/Dislikes__

- Likes are showen on each poll to show how popular sets are amoungst the users of the site.
- Dislikes are showen on each poll to show how unpopular sets are amoungst the users of the site.

- __Comments__

- Each poll features its own comments section. Approved comments are published below each poll and allow a dialogue between users. 
- It allows users to say how they felt about a particular set.
- Conversely it allows user to voice their concern or displeasure at a particular set.
- The comments feature allows the Magic: The Gathering community to deliberate on any given set and give Magics parent company (Wizards of the Coast) an opportunity to see how their latest set is going down with consumers. 

- __Navbar__

- Allows the user to navigate the site.
- Features a registration button to allow new users to join the site.
- A login button, so that memebers can sign in.
- A logout button to allow the user to logout from their account. 

### Features left to Implement

- Allow any user to upload a new set poll, not just an administrator. 
- Include more Magic: The Gathering products in polls thast aren't polls such as secret lair drops and Magic video game releases.
- Add more lore friendly liking and disliking buttons. Also to add in total number of views to each post.
- Better visualisation of the new cards in the set, rather than just noting how many new cards are out with each set.
- Remove the need for approval on every comment and in the future possibly leave it up to moderaters of the site to approve comments rather than one administrator.


## Technologies

- Django was used as the web framework for this project. [Django](https://www.djangoproject.com/)
- Python was used as primary programming language for this project. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- HyperTextMarkup Langugae (HTML) was another programming language used for this project. It was utilised for the main content of the website and as the standard markup language. It was also used because of its ability to be used alongside Cascading Style sheets programming language. [HTML](https://en.wikipedia.org/wiki/HTML)
- Cascading Style Sheets (CSS) was the programming langugae used in conjunction with HTML. It was used to present the markup langugae HTML. CSS was used to put the HTML into a presentable form. [CSS](https://en.wikipedia.org/wiki/CSS)
- Git was the technology used for version control. It is free and open sourced. [Git](https://git-scm.com/)
- GitHub was used as a code hosting site for storing the code for this project online securely. [GitHub](https://github.com/)
- Gitpod is a cloud based IDE which was used to write the code for this project. [Gitpod](https://www.gitpod.io/)
- Heroku is a cloud based application. It was used for deployment of the application. [Heroku](https://www.heroku.com/home)
- Lucidchart is a web based tool that was used to create a flowchart for this project. [Lucidchart](https://bit.ly/3rgpbku)

## Testing

### Code Validation

### Browser Capability

### Responsiveness

### Tested User Stories

- As a site user I can view the current opinions of other users on the latest Magic set posts so that I can select and view one.
- As a user I can register an account so that I can comment and like/dislike set posts.
- As a user I can see the like/dislike ratio of each set post on the site.
- As a user I can register a unique account so I can comment and like on each set.
- As a user I can like or dislike a set post so that I can contribute to the opinion of the fan base on the site.
- As a user I can leave comments on a post so that I can be involved in the conversation.

### Unfixed Bugs

### Deployment

- explain how someone can deploy to Heroku (sign-up, create app with custom name, add config vars/which ones?, add Resources for Postgres DATABASE_URL, etc.)
- explain how someone can get their own Cloudinary API keys (sign-up, where to get the KEY, and how to add to env.py and/or Heroku config vars)
- explain that they need a [Procfile](Procfile)
- explain that they need to install and/or freeze the [requirements.txt](requirements.txt)
    - `pip3 install -r requirements.txt` (install from your [requirements.txt](requirements.txt))
    - `pip3 freeze --local > requirements.txt` (freeze from their own workspace)
- to create an `env.py` file and which KEYs to include:
    - `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`


### Local Deployment

- Procfile, env.py file explain, requirements.txt. 
- python3 manage.py makemigrations, migrations, createsuperuser.

## Credits

### Content

- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- Coolors.co was used to generate a color palette for the site. [Coolors](https://coolors.co/)
- Responsive images were generated on the site Am I Responsive?. [Am I Responsive?](http://ami.responsivedesign.is/)
- Screenshots and images edited using graphic editor Microsoft Paint. [Mircosoft Paint](https://support.microsoft.com/en-us/windows/open-microsoft-paint-ead1dc5c-abc4-fd2c-d81e-ebb013fbc113)

### Media

- Image of Innistrad: Midnight Hunt set icon taken from mtg.cardsrealm.com [MTG Cards Realm](https://mtg.cardsrealm.com/en-us/sets/smid-innistrad--midnight-hunt-substitute-cards)
- Image of Innistrad: Midnight Hunt set taken from mtg wiki [MTG Wiki](https://mtg.fandom.com/wiki/Innistrad:_Midnight_Hunt)
- Image of Adventures in the Forgotten Realms set icon taken from mtg.cardsrealm.com [MTG Cards Realm](https://mtg.cardsrealm.com/en-us/sets/tafr-adventures-in-the-forgotten-realms-tokens)
- Image of Adventures in the Forgotten Realms set taken from Reddit [Reddit](https://www.reddit.com/r/magicTCG/comments/nul0ek/what_are_your_predictions_and_expectations_for/)

### Acknowledgments