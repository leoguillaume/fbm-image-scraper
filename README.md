# Facebook messenger photos scraper

A python script to bulk download pictures from your Facebook Messenger account for a specific chat between your account and a friend's or a messenger group.

## Warning

> This script use [fbchat](https://fbchat.readthedocs.io/en/stable/index.html) library. As mentioned in the documentation, mass requests to the Facebook servers can ban your Facebook account. This doesn't seem to be the case with this script (I downloaded several thousands of images on different groups in the same day without any problem). Anyway be careful, I'm not responsible for the use of this script.

## Configuration

Create a `config.ini` file as in the `example-config.ini` to setup local variables.

### Key-value pairs

- `[Local][path]`: Local target path for the images to be downloaded to.
- `[Local][user-agent]`: Your user agent. You can get it by typing "what is my user agent" in google.

## Execution

1. Install python packages in your terminal: `pip install -r requirements.txt`

2. Run fbmscraper.py with python3

Command line: `python3 fbmscraper.py <thread_id> <email>`

`tread_id`:

A thread is a messenger chat for fbchat library. The ID of the thread (group or a specific person) is in the url of the messenger chat. There are two formats of ID (numbers or name):

![](https://github.com/leoguillaume/fbm-image-scraper/blob/master/readme-assets/screenshot-1.png) or
![](https://github.com/leoguillaume/fbm-image-scraper/blob/master/readme-assets/screenshot-2.png)

This script is suitable for both formats. It doesn't work with yourself or if you aren't friends with the person who has the ID. The number of retrievable photos depends on your seniority in the messenger group.

`email`: your facebook account email
