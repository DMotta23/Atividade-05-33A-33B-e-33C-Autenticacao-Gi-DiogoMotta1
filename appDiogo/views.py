from django.shortcuts import render, redirect
from .models import PratosMassa, Utensilios, Porcoes


# Create your views here.
def home(request):

    pratos_massa = PratosMassa.objects.all()
    utensilios_cozinha = Utensilios.objects.all()
    porcoes_ingredientes = Porcoes.objects.all()

    return render(request,
                  "home.html",
                  context={
                      "pratos_massa": pratos_massa,
                      "utensilios_cozinha": utensilios_cozinha,
                      "porcoes_ingredientes": porcoes_ingredientes
                  })

########
def create_porcoes(request):
  if request.method == "POST":

    Porcoes.objects.create(
      nome = request.POST["nome"],
      quantidade = request.POST["quantidade"]
    )

    return redirect("home")
  return render(request, "formsPorcoes.html", context={"action":"adicionar"})

def update_porcoes(request,id):
  porcoes = Porcoes.objects.get(id = id)
  if request.method == "POST":
    
      porcoes.nome = request.POST["nome"]
      porcoes.quantidade = request.POST["quantidade"]
      porcoes.save()

      return redirect("home")
  return render(request, "formsPorcoes.html", context={"action":"atualizar","porcoes":porcoes})

def delete_porcoes(request,id):
  porcoes = Porcoes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      porcoes.delete()

    return redirect("home")
  return render(request, "are_you_surePorcoes.html", context={"porcoes":porcoes})

########
def create_pratos(request):
  options = PratosMassa.dificuldade.field.choices
  
  if request.method == "POST":
    
    PratosMassa.objects.create(
      nome = request.POST["nome"],
      tipoMassa = request.POST["tipoMassa"],
      dificuldade = request.POST["dificuldade"],
      numCalorias = request.POST["numCalorias"]
    )

    return redirect("home")
  return render(request, "formsPratos.html", context={"action":"adicionar",'options': options})

def  update_pratos(request,id):
  pratos = PratosMassa.objects.get(id=id)
  options = PratosMassa.dificuldade.field.choices
  
  if request.method == "POST":

      pratos.nome = request.POST["nome"]
      pratos.tipoMassa = request.POST["tipoMassa"]
      pratos.dificuldade = request.POST["dificuldade"]
      pratos.numCalorias = request.POST["numCalorias"]
      pratos.save()

      return redirect("home")
  return render(request, "formsPratos.html", context={"action":"atualizar","pratos":pratos,'options': options})

def  delete_pratos(request,id):
  pratos = PratosMassa.objects.get(id=id)
  options = PratosMassa.dificuldade.field.choices
  
  if request.method == "POST":
    if "confirm" in request.POST:
      pratos.delete()

    return redirect("home")
  return render(request, "are_you_surePratos.html", context={"pratos":pratos,'options': options})
  
########
def create_utensilios(request):
  options = Utensilios.tamanho.field.choices
  
  if request.method == "POST":

    cortante_value = 'cortante' in request.POST
    
    Utensilios.objects.create(
      nome = request.POST["nome"],
      material = request.POST["material"],
      cortante = cortante_value,
      tamanho = request.POST["tamanho"]
    )

    return redirect("home")
  return render(request, "formsUtensilios.html", context={"action":"adicionar",'options': options})

def update_utensilios(request,id):
  utensilios = Utensilios.objects.get(id=id)
  options = Utensilios.tamanho.field.choices
  
  if request.method == "POST":

      cortante_value = 'cortante' in request.POST
    
      utensilios.nome = request.POST["nome"]
      utensilios.material = request.POST["material"]
      utensilios.cortante = cortante_value
      utensilios.tamanho = request.POST["tamanho"]
      utensilios.save()

      return redirect("home")
  return render(request, "formsUtensilios.html", context={"action":"atualizar","utensilios":utensilios,'options': options})

def delete_utensilios(request,id):
  utensilios = Utensilios.objects.get(id=id)
  options = Utensilios.tamanho.field.choices
  
  if request.method == "POST":
    if "confirm" in request.POST:
      utensilios.delete()

    return redirect("home")
  return render(request, "are_you_sureUtensilios.html", context={"utensilios":utensilios,'options': options})
########