# Python-based-automated-bot
A simple class which can login in facebook and do some activity
---
## Available functions:
    
    * Login to a Facebook account given ID and Password.
    * Add 1 friend from the same location as the location of the ID.
    * Update account status (text based).
    * Open timeline of a random friend and comment on the most recent post.
    
## Basic usage example:
```
from bot import facebook
fb=facebook("email-id","password")
fb.addFriend()
fb.updateStatus("put sataus text")
fb.comment("add comment")
```
## Dependencies:

    * Python 3.7

    * Selenium
    
    * make sure u install chrome selenium driver and copy to Environment variable
