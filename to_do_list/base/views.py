from django.shortcuts import render, redirect
import datetime

id = 1

tasks = [
    {
        'id': 0,
        'title': 'Fix Bugs'
    }
]

def get_today_date_and_day():
  """Gets today's date and day.

  Returns:
    A tuple of today's date and day.
  """

  today = datetime.date.today()
  day = today.strftime("%A")

  return today, day

# Create your views here.
def homePage(request):
    global id
    if request.method == 'POST':
        newTask = request.POST['new_task']
        if newTask != '':
            tasks.append({'id': id, 'title': newTask})
            id += 1
    
    today, day = get_today_date_and_day()
    context = {'tasks': tasks, 'today': today, 'day': day}
    return render(request, 'base/index.html', context)

def deleteTask(request, delID):
    for index, task in enumerate(tasks):
        if task["id"] == delID:
            break
    del(tasks[index])
    return redirect('home-page')

def editTask(request, editID):
    if request.method == "POST":
        newTitle = request.POST['new_title']
        if newTitle != '':
            for index, task in enumerate(tasks):
                if task["id"] == editID:
                    tasks[index]['title'] = newTitle
                    break
        return redirect("home-page")


    for index, task in enumerate(tasks):
        if task["id"] == editID:
            break
    context = {'task': task}
    return render(request, 'base/edit.html', context)