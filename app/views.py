from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass


# Create your views here.
def home(
    request: HttpRequest,
) -> HttpResponse:
    teams = ["Management", "Procurement", "Community", "Documentation"]

    context = {"teams": teams}

    return render(
        request,
        "Home.html",
        context,
    )


@dataclass
class team:
    Tname: str
    Tdesc: str
    Tmembers: str


Team_dict = {
    "management": team(
        "Management",
        "Management makes sure supplies are replinished, and the school is clean, and presentable.",
        ["Owen", "Jeremiah", "Nick", "Abigail", "Ab", "Mathew"],
    ),
    "procurement": team(
        "Procurement",
        "Procurement's job is to keep the students fed, and the kitchen stocked. a regular budget is kept, and shopping trips are made by the team weekly.",
        [
            "Adrian",
            "Bryce",
            "Johnathan",
            "Blaine",
            "Wyatt",
        ],
    ),
    "community": team(
        "Community",
        "Community's job is to arrange community events. These events occur every other friday, and can consist of field days, Bowling, Gaming Days, and many more.",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "documentation": team(
        "Documentation",
        "Documentation keeps the people updated on how Basecamp is doing, and what were are working on.",
        ["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah"],
    ),
}


def to_teams(request: HttpRequest, team_num: str) -> HttpResponse:
    if team_num == "Management":
        context1 = {"team": Team_dict["management"]}
        return render(request, "details.html", context1)
    elif team_num == "Procurement":
        context2 = {"team": Team_dict["procurement"]}
        return render(request, "details.html", context2)
    elif team_num == "Community":
        context3 = {"team": Team_dict["community"]}
        return render(request, "details.html", context3)
    elif team_num == "Documentation":
        context4 = {"team": Team_dict["documentation"]}
        return render(request, "details.html", context4)

    else:
        return HttpResponse("no")
    # if team_num.lower() in Team_dict.keys():
    # return render(request, "details.html", context={"team": Team_dict[team_num.lower]})
