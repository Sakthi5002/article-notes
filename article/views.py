from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Link
from .forms import GroupForm, LinkForm

# Create your views here.
def home(request):
    groups = Group.objects.all()
    return render(request, 'article/home.html', {'groups':groups})

def group(request, pk):
    # links = Link.objects.filter(group_id=1)
    group = get_object_or_404(Group, pk=pk)
    links = Link.objects.filter(group_id=pk)
    return render(request, 'article/group.html', {'links':links, 'group':group})

def new_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('home')
    else:
        form = GroupForm()
    return render(request, 'article/new_group.html', {'form':form})

def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('home')
    else:
        form = GroupForm(instance=group)
    return render(request, 'article/new_group.html', {'form':form})

def del_group(request,pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('home')

def new_link(request, pk):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            group = Group.objects.filter(id=pk)
            link.group_id = group[0]
            link.save()
            return redirect('group', pk=pk)
    else:
        form = LinkForm()
    return render(request, 'article/new_group.html', {'form':form})

def del_link(request,pk, g_pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('group', pk=g_pk)