from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username=form.changed_data.get('username')
#             messages.success(request, f"Welcome {username}, your account is created.")
#             return redirect('users/message.html')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/user-register.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account has been created.")
            return redirect('login')  # Use the name of the URL pattern you want to redirect to
            # return render(request, 'users/message.html')
    else:
        form = RegisterForm()
    return render(request, 'users/user-register.html', {'form': form})


