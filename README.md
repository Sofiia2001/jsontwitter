This module is created to let programmers to get data from .json format file created with Twitter API.
With calling specific function, it returns a specific part of a file.

HELP:

    get_friend(path*) -> Function reads the json file and gets the information from it

    get_friend_status(path) -> Function gets friends' status

    get_friend_status_text(path) -> Function gets friends' status text

    get_friend_place_country(path) -> Function gets friends' country

    get_friend_description(path) -> Function gets friends' description

    get_friend_name(path) -> Function gets friends' name

    get_friend_screen_name(path) -> Function gets friends' screen name

    get_friend_location(path) -> Function gets friends' location

    get_friend_id(path) -> Function gets friends' id

    get_friend_followers_count(path) -> Function gets friends' followers count

    get_friend_friends_count(path) -> Function gets friends' friends count

    get_friend_listed_count(path) -> Function gets friends' listed count

    get_friend_created_at(path) -> Function gets friends' data of account creation

    get_friend_favourites_count(path) -> Function gets friends' favourites count

    get_friend_statuses_count(path) -> Function gets friends' statuses count

    get_friend_lang(path) -> Function gets friends' language of a page

    get_friend_profile_background_color(path) -> Function gets friends' profile background color

    get_friend_profile_background_image_url(path) -> Function gets friends' profile background image url

    get_friend_profile_image_url(path) -> Function gets friends' profile image url

    get_friend_profile_banner_url(path) -> Function gets friends' profile banner url

    get_friend_profile_link_color(path) -> Function gets friends' profile link color

    get_friend_profile_sidebar_border_color(path) -> Function gets friends' profile sidebar border color

    get_friend_profile_sidebar_fill_color(path) -> Function gets friends' profile sidebar fill color

    get_friend_profile_text_color(path) -> Function gets friends' profile text color

    get_friend_translator_type(path) -> Function gets friends' translator type

    *path - the name of .json format file
    e.g. 'friends.json'

EXAMPLE OF USE:

    import friend_json


    print(friend_json.get_friend_lang('user_friends.json'))

    This part of code will print out 'uk'
