import json


def get_friend(path):
    '''
    Function reads the json file and gets the information from it
    '''
    with open(path, 'r') as file:
        friend_structure = json.load(file)
    return friend_structure


# Working with 'STATUS' sector
def get_friend_status(path):
    '''
    Function gets friends' status
    '''
    friend_structure = get_friend(path)
    return friend_structure.get('status')


def get_friend_status_text(path):
    '''
    Function gets friends' status text
    '''
    status = get_friend_status(path)
    if status is not None:
        return status.get('text')
    return None


def get_friend_place_country(path):
    '''
    Function gets friends' country
    '''
    status = get_friend_status(path)
    place = status.get('place')
    if place is not None:
        return place.get('country')
    return None


def get_friend_description(path):
    '''
    Function gets friends' description
    '''
    friend_structure = get_friend(path)
    description = friend_structure.get('description')
    if description is not None:
        return description
    return None


def get_friend_name(path):
    '''
    Function gets friends' name
    '''
    friend_structure = get_friend(path)
    name = friend_structure.get('name')
    if name is not None:
        return name
    return None


def get_friend_screen_name(path):
    '''
    Function gets friends' screen name
    '''
    friend_structure = get_friend(path)
    screen_name = friend_structure.get('screen_name')
    if screen_name is not None:
        return screen_name
    return None


def get_friend_location(path):
    '''
    Function gets friends' location
    '''
    friend_structure = get_friend(path)
    location = friend_structure.get('location')
    if location is not None:
        return location
    return None


def get_friend_id(path):
    '''
    Function gets friends' id
    '''
    friend_structure = get_friend(path)
    id = friend_structure.get('id')
    if id is not None:
        return id
    return None


def get_friend_followers_count(path):
    '''
    Function gets friends' followers count
    '''
    friend_structure = get_friend(path)
    followers_count = friend_structure.get('followers_count')
    if followers_count is not None:
        return followers_count
    return None


def get_friend_friends_count(path):
    '''
    Function gets friends' friends count
    '''
    friend_structure = get_friend(path)
    friends_count = friend_structure.get('friends_count')
    if friends_count is not None:
        return friends_count
    return None


def get_friend_listed_count(path):
    '''
    Function gets friends' listed count
    '''
    friend_structure = get_friend(path)
    listed_count = friend_structure.get('listed_count')
    if listed_count is not None:
        return listed_count
    return None


def get_friend_created_at(path):
    '''
    Function gets friends' data of account creation
    '''
    friend_structure = get_friend(path)
    created_at = friend_structure.get('created_at')
    if created_at is not None:
        return created_at
    return None


def get_friend_favourites_count(path):
    '''
    Function gets friends' favourites count
    '''
    friend_structure = get_friend(path)
    favourites_count = friend_structure.get('favourites_count')
    if favourites_count is not None:
        return favourites_count
    return None


def get_friend_statuses_count(path):
    '''
    Function gets friends' statuses count
    '''
    friend_structure = get_friend(path)
    statuses_count = friend_structure.get('statuses_count')
    if statuses_count is not None:
        return statuses_count
    return None


def get_friend_lang(path):
    '''
    Function gets friends' language of a page
    '''
    friend_structure = get_friend(path)
    lang = friend_structure.get('lang')
    if lang is not None:
        return lang
    return None


def get_friend_profile_background_color(path):
    '''
    Function gets friends' profile background color
    '''
    friend_structure = get_friend(path)
    background_color = friend_structure.get('profile_background_color')
    if background_color is not None:
        return background_color
    return None


def get_friend_profile_background_image_url(path):
    '''
    Function gets friends' profile background image url
    '''
    friend_structure = get_friend(path)
    background_image_url = friend_structure.get('profile_background_image_url')
    if background_image_url is not None:
        return background_image_url
    return None


def get_friend_profile_image_url(path):
    '''
    Function gets friends' profile image url
    '''
    friend_structure = get_friend(path)
    profile_image_url = friend_structure.get('profile_image_url')
    if profile_image_url is not None:
        return profile_image_url
    return None


def get_friend_profile_banner_url(path):
    '''
    Function gets friends' profile banner url
    '''
    friend_structure = get_friend(path)
    profile_banner_url = friend_structure.get('profile_banner_url')
    if profile_banner_url is not None:
        return profile_banner_url
    return None


def get_friend_profile_link_color(path):
    '''
    Function gets friends' profile link color
    '''
    friend_structure = get_friend(path)
    profile_link_color = friend_structure.get('profile_link_color')
    if profile_link_color is not None:
        return profile_link_color
    return None


def get_friend_profile_sidebar_border_color(path):
    '''
    Function gets friends' profile sidebar border color
    '''
    friend_structure = get_friend(path)
    profile_sidebar_border_color = friend_structure.get('profile_sidebar_border_color')
    if profile_sidebar_border_color is not None:
        return profile_sidebar_border_color
    return None


def get_friend_profile_sidebar_fill_color(path):
    '''
    Function gets friends' profile sidebar fill color
    '''
    friend_structure = get_friend(path)
    profile_sidebar_fill_color = friend_structure.get('profile_sidebar_fill_color')
    if profile_sidebar_fill_color is not None:
        return profile_sidebar_fill_color
    return None


def get_friend_profile_text_color(path):
    '''
    Function gets friends' profile text color
    '''
    friend_structure = get_friend(path)
    profile_text_color = friend_structure.get('profile_text_color')
    if profile_text_color is not None:
        return profile_text_color
    return None


def get_friend_translator_type(path):
    '''
    Function gets friends' translator type
    '''
    friend_structure = get_friend(path)
    translator_type = friend_structure.get('translator_type')
    if translator_type is not None:
        return translator_type
    return None
