def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")

    else:
        form=UserCreationForm()
        return render(request,"registration/register.html",{"form":form,})

def home(request):
    if request.user.is_authenticated:
        return render(request,'introduction/home.html',)
    else:
        return redirect('login')

## authentication check decurator function 
def authentication_decorator(func):
    def function(*args, **kwargs):
        if args[0].user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return redirect('login')
    return function

#*****************************************XSS****************************************************#


def xss(request):
    if request.user.is_authenticated:
        return render(request,"Lab/XSS/xss.html")
    else:
        return redirect('login')

def xss_lab(request):
    if request.user.is_authenticated:
        q=request.GET.get('q','')
        f=FAANG.objects.filter(company=q)
        if f:
            args={"company":f[0].company,"ceo":f[0].info_set.all()[0].ceo,"about":f[0].info_set.all()[0].about}
            return render(request,'Lab/XSS/xss_lab.html',args)
        else:
            return render(request,'Lab/XSS/xss_lab.html', {'query': q})
    else:
        return redirect('login')
        

def xss_lab2(request):
    if request.user.is_authenticated:
        
        username = request.POST.get('username', '')
        if username:
            username = username.strip()
            username = username.replace("<script>", "").replace("</script>", "")
        else:
            username = "Guest"
        context = {
        'username': username
                }
        return render(request, 'Lab/XSS/xss_lab_2.html', context)
    else:
        return redirect('login')

#***********************************SQL****************************************************************#

def sql(request):
    if request.user.is_authenticated:

        return  render(request,'Lab/SQL/sql.html')
    else:
        return redirect('login')

def sql_lab(request):
    if request.user.is_authenticated:

        name=request.POST.get('name')

        password=request.POST.get('pass')

        if name:

            if login.objects.filter(user=name):

                sql_query = "SELECT * FROM introduction_login WHERE user='"+name+"'AND password='"+password+"'"
                print(sql_query)
                try:
                    print("\nin try\n")
                    val=login.objects.raw(sql_query)
                except:
                    print("\nin except\n")
                    return render(
                        request, 
                        'Lab/SQL/sql_lab.html',
                        {
                            "wrongpass":password,
                            "sql_error":sql_query
                        })

                if val:
                    user=val[0].user
                    return render(request, 'Lab/SQL/sql_lab.html',{"user1":user})
                else:
                    return render(
                        request, 
                        'Lab/SQL/sql_lab.html',
                        {
                            "wrongpass":password,
                            "sql_error":sql_query
                        })
            else:
                return render(request, 'Lab/SQL/sql_lab.html',{"no": "User not found"})
        else:
            return render(request, 'Lab/SQL/sql_lab.html')
    else:
        return redirect('login')


#******************************************************  Command Injection  ***********************************************************************#

def cmd(request):
    if request.user.is_authenticated:
        return render(request,'Lab/CMD/cmd.html')
    else:
        return redirect('login')
@csrf_exempt
def cmd_lab(request):
    if request.user.is_authenticated:
        if(request.method=="POST"):
            domain=request.POST.get('domain')
            domain=domain.replace("https://www.",'')
            os=request.POST.get('os')
            print(os)
            if(os=='win'):
                command="nslookup {}".format(domain)
            else:
                command = "dig {}".format(domain)
            
            try:
                # output=subprocess.check_output(command,shell=True,encoding="UTF-8")
                process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                data = stdout.decode('utf-8')
                stderr = stderr.decode('utf-8')
                # res = json.loads(data)
                # print("Stdout\n" + data)
                output = data + stderr
                print(data + stderr)
            except:
                output = "Something went wrong"
                return render(request,'Lab/CMD/cmd_lab.html',{"output":output})
            print(output)
            return render(request,'Lab/CMD/cmd_lab.html',{"output":output})
        else:
            return render(request, 'Lab/CMD/cmd_lab.html')
    else:
        return redirect('login')
