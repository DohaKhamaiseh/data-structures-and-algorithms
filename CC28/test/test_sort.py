import sort
import pytest



def test_year():
  moives=[{"title": "The report", "year": 2018,"genres":["Action","Drama"]},
    {"title": "Great Hack", "year": 2020, "genres":["Comedy","Horror"]},
    {"title": "Detective Conan", "year": 2019, "genres":["Fantasy","Mystery"]},
    {"title": "A Beautiful Mind ", "year": 2017, "genres":["Fantasy","Mystery"]},
    {"title": "An Officer and a Gentleman", "year": 2000, "genres":["Fantasy","Mystery"]},]

  actual=sort.sort_by_year(moives)
  expected= [{'title': 'An Officer and a Gentleman', 'year': 2000, 'genres': ['Fantasy', 'Mystery']}, {'title': 'A Beautiful Mind ', 'year': 2017, 'genres': ['Fantasy', 'Mystery']}, {'title': 'The report', 'year': 2018, 'genres': ['Action', 'Drama']}, {'title': 'Detective Conan', 'year': 2019, 'genres': ['Fantasy', 'Mystery']}, {'title': 'Great Hack', 'year': 2020, 'genres': ['Comedy', 'Horror']}]

  assert actual==expected

def test_title():
  moives=[{"title": "The report", "year": 2018,"genres":["Action","Drama"]},
    {"title": "Great Hack", "year": 2020, "genres":["Comedy","Horror"]},
    {"title": "Detective Conan", "year": 2019, "genres":["Fantasy","Mystery"]},
    {"title": "A Beautiful Mind ", "year": 2017, "genres":["Fantasy","Mystery"]},
    {"title": "An Officer and a Gentleman", "year": 2000, "genres":["Fantasy","Mystery"]},]

  actual=sort.sort_by_title(moives)
  expected= [{'title': 'Detective Conan', 'year': 2019, 'genres': ['Fantasy', 'Mystery']}, {'title': 'Great Hack', 'year': 2020, 'genres': ['Comedy', 'Horror']}]

  assert actual==expected