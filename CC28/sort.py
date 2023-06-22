import re
def sort_by_year(lis):
  lis.sort(key=lambda movie: movie["year"])
  return lis


def sort_by_title(lis):
    pattern = r'^(A |An |The )'
    filtered_movies = [movie for movie in lis if not re.match(pattern, movie["title"])]
    sorted_movies = sorted(filtered_movies, key=lambda movie: movie["title"])
    return sorted_movies



moives=[{"title": "The report", "year": 2018,"genres":["Action","Drama"]},
    {"title": "Great Hack", "year": 2020, "genres":["Comedy","Horror"]},
    {"title": "Detective Conan", "year": 2019, "genres":["Fantasy","Mystery"]},
    {"title": "A Beautiful Mind ", "year": 2017, "genres":["Fantasy","Mystery"]},
    {"title": "An Officer and a Gentleman", "year": 2000, "genres":["Fantasy","Mystery"]},]

print(sort_by_year(moives))
print(sort_by_title(moives))
