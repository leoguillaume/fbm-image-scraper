import re, urllib.request, os, fbchat
from fbchat import Client
from fbchat.models import *
from urllib.error import *
from tqdm import tqdm

def fbm_scraper(client, thread_id, outpath, gif = True):

    """
    Scrape and save image from a facebook messenger chat.

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

    """

    if not thread_id.isnumeric(): # If the id isn't numbers, the user id have to be find
        users = client.searchForUsers(thread_id)
        thread_id = None
        for u in users:
                if u.is_friend:
                    answer = input(f"Connection with {u.first_name} {u.last_name} ? y/n\n")
                    if answer.lower() == 'y' or answer.lower() == 'yes':
                        thread_id = u.uid

    if thread_id == None:
        print('The messenger chat cannot be found.')
        return

    else:
        try:
            print(f"Connection to: {client.fetchThreadInfo(thread_id)[thread_id].name}")
        except:
            print(f"Connection to: {client.fetchThreadInfo(thread_id)[thread_id].first_name} "
                  f"{client.fetchThreadInfo(thread_id)[thread_id].last_name}")

        outpath = os.path.join(outpath, thread_id)

        if os.path.exists(outpath):
            print("Images can't save because a output folder for this chat already exist.")
            return
        else:
             os.mkdir(outpath) # create a directory with the thread_id as name

        print('Initialization...')
        images = client.fetchThreadImages(thread_id)
        attachments = list(images)

        print(f"{len(attachments)} objects find.") # attachments are images and videos

        i, e, g, v = 0, 0, 0, 0

        for a in tqdm(attachments):

            if type(a) == fbchat._file.VideoAttachment: # Ignore videos
                v += 1
                continue

            if gif == False and re.search(r".gif\?", a.large_preview_url) != None: # Ignore gifs
                g += 1
                continue

            else:
                try:
                    urllib.request.urlretrieve(a.large_preview_url, os.path.join(outpath, str(i) + '.jpg')) # large_preview_url is the highest resolution
                    i += 1

                except HTTPError:
                    e += 1

        print(f"{i} images have been saved.\n"
              f"{e} ressources have been permanently deleted by Facebook.\n"
              f"{v} videos and {g} gifs have been ignored.")
