# Facebook messenger photos scraper

A python script to bulk download pictures from your Facebook Messenger account for a specific chat between your account and a friend's or a messenger group.

## Warning

> This script use [fbchat](https://fbchat.readthedocs.io/en/stable/index.html) library. As mentioned in the documentation, mass requests to the Facebook servers can ban your Facebook account. This doesn't seem to be the case with this script (I downloaded several thousands of images on different groups in the same day without any problem). Anyway be careful, I am not responsible for the use of this scri> qsdfpt.

## Configuration

Create a `config.ini` file as in the `example-config.ini`.

### Key-value pairs

- `[Credentials][email]`: Your FB account email used for authentication.
- `[Credentials][password]`: Your FB account password used for authentication.
- `[Credentials][user-agent]`: Your user agent. You can get it by typing "user agent" in google.
- `[Tread][id]`: The URL to your friend's or your group.

A thread is a messenger chat for fbchat library. The id of the thread (group or a specific friend) is in the url of the messenger chat. There are two format of id (numbers or name):

![image](https://github.com/leoguillaume/fbm-image-scraper/readme-assets/screenshot-1.png) or
![image](https://github.com/leoguillaume/fbm-image-scraper/readme-assets/screenshot-2.png)

The number of retrievable photos depends on your seniority in the group.

- `[Download][path]`: Local target path for the images to be downloaded to.

## Execution

1. Install python packages in your terminal: `pip install -r requirements.txt`
2. Two way to run the scraper:

* The first way, you directly run the script with the `main.py` file in your terminal: `python3 main.py`

* The second way is to execute the `fbm-scraper` function in the `fbm-scraper.py` file.
```
Parameters
----------
client:
    fbchat._client.Client object.

messenger_id: str
    Messenger friend id or messenger group id.

out_path: str
    Directory path to save attachments.

gif: bool, default=True
    If True, save gif attachments.
`> `
