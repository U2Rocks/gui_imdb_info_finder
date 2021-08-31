from tkinter.constants import CENTER
import requests
import tkinter as tk
import re


def reset_text_box():
    movie_search_box.delete(0, 'end')
    movie_search_box.insert(0, "Type your IMDB ID Here")


# function that calls request and prints out movie info
def get_movie_info():
    movie_search_input_text = movie_search_box.get()
    # check for empty/unchanged input
    default_input = "Type your IMDB ID Here"
    if movie_search_input_text == default_input:
        # print("RETURN")
        return

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    # get value of text box and turn into part of query
    imdb_id_text = movie_search_input_text

    imdb_id = imdb_id_text

    querystring = {"i": imdb_id, "r": "json"}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "API_KEY_HERE"
    }
    # pattern to do last check before sending request
    final_check = bool(re.match(r"[a-z]+[0-9]+", imdb_id))
    if final_check == False:
        # print("PATTERN FAIL")
        reset_text_box()
        return
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    response_data = response.json()

    # trasfer info from json to variables for labels and add complementary text for labels
    title_text = response_data["Title"]
    year_text = response_data["Year"]
    rating_text = response_data["Rated"]
    release_text = response_data["Released"]
    runtime_text = response_data["Runtime"]
    genre_text = response_data["Genre"]
    metascore_text = response_data["Metascore"]
    runtime_text_corrected = "Runtime: " + runtime_text
    genre_text_corrected = "Genre: " + genre_text
    metascore_text_corrected = "Metascore: " + metascore_text
    release_text_corrected = "Release Date: " + release_text
    rating_text_corrected = "Rating: " + rating_text

    # change labels with new info
    movie_title.config(text=title_text)
    movie_year.config(text=year_text)
    movie_rating.config(text=rating_text_corrected)
    movie_release.config(text=release_text_corrected)
    movie_runtime.config(text=runtime_text_corrected)
    movie_genre.config(text=genre_text_corrected)
    movie_metascore.config(text=metascore_text_corrected)
    # print(response.text)
    reset_text_box()


# THINGS WE WANT TO GET FROM API: Title, Year, Rated, Released, Runtime, Genre, Metascore

# PLAN: GUI has Entry box for Imdb movie ID and a get information button...
# - get information button initiates the API call and resets the text box
# - after information is retrieved a series of labels that are set at N/A
# - by default are modified by a function
# - depending on the Genre a picture is shown to represent the Genre?
# - pictures are stored in same file as python script?
# - GUI elements: entry, buttons, labels, field(place labels on), image displayer?


# setup tkinter window
root = tk.Tk()
root.geometry("550x550")
root.minsize(550, 500)
root.maxsize(550, 500)
root.config(bg="#7ec4ed")
root.title("IMDB Movie Info Finder")


# initialize components for tkinter GUI Interface
global movie_search_box
global movie_title
global movie_year
global movie_rating
global movie_release
global movie_runtime
global movie_genre
global movie_metascore
movie_search_box = tk.Entry(
    root, text="Enter a Movie ID Here", width=64)
activate_movie_search = tk.Button(
    root, text="Search For Movie Info", justify=CENTER, command=get_movie_info)
movie_search_box.insert(0, "Type your IMDB ID Here")
movie_info_frame = tk.Frame(root, bg="#7e94ed")
movie_title = tk.Label(
    movie_info_frame, text="N/A", justify=CENTER, font="Helvetica 14")
movie_year = tk.Label(movie_info_frame, text="N/A",
                      justify=CENTER, font="Helvetica 14")
movie_rating = tk.Label(movie_info_frame, text="N/A",
                        justify=CENTER, font="Helvetica 14")
movie_release = tk.Label(
    movie_info_frame, text="N/A", justify=CENTER, font="Helvetica 14")
movie_runtime = tk.Label(movie_info_frame, text="N/A",
                         justify=CENTER, font="Helvetica 14")
movie_genre = tk.Label(movie_info_frame, text="N/A",
                       justify=CENTER, font="Helvetica 14")
movie_metascore = tk.Label(movie_info_frame, text="N/A",
                           justify=CENTER, font="Helvetica 14")


# place components on the grid
movie_search_box.grid(row=0, column=0, padx=10, pady=10)
activate_movie_search.grid(row=0, column=1, padx=10, pady=10)
movie_info_frame.grid(row=1, column=0, columnspan=2)
movie_title.grid(row=0, column=0, pady=10)
movie_year.grid(row=1, column=0, pady=10)
movie_rating.grid(row=2, column=0, pady=10)
movie_release.grid(row=3, column=0, pady=10)
movie_runtime.grid(row=4, column=0, pady=10)
movie_genre.grid(row=5, column=0, pady=10)
movie_metascore.grid(row=6, column=0, pady=10)


# initiate tkinter window
root.mainloop()
