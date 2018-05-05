
flight_length = 220
movie_lengths = [120,120]
def findMovie(flight_length, movie_lengths):
    difference = set()
    for i in movie_lengths:
        if i in difference:
            return True
        else:
            difference.add(flight_length-i)
    return False

print (findMovie(flight_length, movie_lengths))
