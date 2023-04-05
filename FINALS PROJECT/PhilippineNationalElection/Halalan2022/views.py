from django.shortcuts import render, redirect, get_object_or_404
# Add the rest of the Class below \/ \/ \/
from .models import User, Candidates, Vote
from django.contrib import messages


# Create your views here.
def homepage(request):
    candidate_objects = Candidates.objects.all()
    return render(request, 'Halalan2022/homepage.html', {'x':candidate_objects})

if(len(User.objects.all()) > 0 ):
    loggedInUser = User.objects.all()[0]

userNameLogged = "" #Username of the latest logged in user.

def loginpage(request):
    if (request.method == "POST"):
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        global userNameLogged
        userNameLogged = usern # Saves the username of the latest logged in user.

        accountList = User.objects.filter(username = usern)

        if(len(accountList) > 0):
            authenticateUser = accountList[0]

            if(authenticateUser.getPassword() == passw):
                global loggedInUser
                loggedInUser = authenticateUser
                return redirect('homepage')
            else:
                messages.info(request, 'Incorrect Username/Password')
                return render(request, 'Halalan2022/loginpage.html')
        else:
            messages.info(request, 'Incorrect Username/Password')
            return render(request, 'Halalan2022/loginpage.html')
    else:
        return render(request, 'Halalan2022/loginpage.html')

def signuppage(request):
    if (request.method == "POST"):
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        passw2 = request.POST.get('password2')
        Sex = request.POST.get('sex')
        birth = request.POST.get('birthday')

        accountList = User.objects.filter(username = usern)
        if passw == passw2:
            if(len(accountList) > 0):
                messages.info(request, 'USERNAME IS ALREADY TAKEN')
                return redirect('signuppage')
            else:
                User.objects.create(first_name = first, last_name = last, username = usern, password = passw, birthday = birth, sex = Sex)
                messages.info(request, 'ACCOUNT SUCCESSFULLY CREATED')
                return render(request, 'Halalan2022/loginpage.html')
        else:
            messages.info(request, 'PASSWORDS NOT MATCH')
            return render(request, 'Halalan2022/signuppage.html')
    else:
        return render(request, 'Halalan2022/signuppage.html')

def userspage(request):
    global userNameLogged
    user_objects = get_object_or_404(User, username = userNameLogged)
    return render(request, 'Halalan2022/userspage.html', {'user': user_objects})

def candidatespage(request):
    candidate_objects = Candidates.objects.all()
    return render(request, 'Halalan2022/candidatespage.html', {'x':candidate_objects})

def votespage(request):
    vote_objects_pres = Candidates.objects.filter(position_id='1' )
    vote_objects_vice = Candidates.objects.filter(position_id='2')
    vote_objects_sen = Candidates.objects.filter(position_id='3' )

    global loggedInUser
    # user_objects_pk = User.objects.get(pk=loggedInUser)
    # user_objects_pk = get_object_or_404(User, pk = loggedInUser)
    user_objects_pk = loggedInUser.pk

    if (request.method == "POST"):
        # userID = request.POST.get(pk = user_objects_pk)
        candidateID = request.POST.get("test")
        candidate = Candidates.objects.get(pk = candidateID)
        cmmnt = request.POST.get("comments")

        Vote.objects.create(user_id = loggedInUser, candidate_id = candidate, comment = cmmnt)

    else:
        return render(request, 'Halalan2022/votespage.html', {'presidents':vote_objects_pres, 'vice_presidents':vote_objects_vice, 'senator':vote_objects_sen})

def aboutpage(request):
    return render(request, 'Halalan2022/aboutpage.html')

def base(request):
    return render(request, 'Halalan2022/base.html')

def updateuserpage(request):
    global userNameLogged

    if (request.method == "POST"):
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        Sex = request.POST.get('sex')
        birth = request.POST.get('birthday')

        User.objects.filter(username = userNameLogged).update(first_name = first, last_name = last, username = usern, password = passw, birthday = birth, sex = Sex)

        return redirect('loginpage')

    else:
        return render(request, 'Halalan2022/updateuserspage.html')








