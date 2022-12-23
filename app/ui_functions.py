from call_api import call_genre
def display_genre(movieName):
    data={
        "userId" : 0,
        "moviename" : movieName,
    }
    movies=call_genre(data)
    return movies