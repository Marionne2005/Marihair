from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first

from hairstyle_app.forms import DemandePersoForm, ReservationForm
from hairstyle_app.models import NewsletterSubscriber


def home(request):
    if request.method == "POST":
        mail = request.POST.get('mail')
        if mail:
            # Sauvegarder l'email dans la base de données
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=mail)

            # Envoyer l'email de confirmation
            try:
                send_mail(
                    'Merci pour votre abonnement à Marihair !',
                    f"Bonjour,\n\nMerci de vous être abonné(e) à la newsletter de Marihair ! Vous recevrez désormais nos dernières actualités et promotions.\n\nL’équipe de Marihair",
                    settings.DEFAULT_FROM_EMAIL,
                    [mail],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Erreur lors de l\'envoi de l\'email : {str(e)}')

    return render(request,'index.html')

def service(request):
    return render(request,'services.html')

def story(request):
     return  render(request,'story.html')

def reservation_us(request):
    return render(request,'reservation.html')

def add_new_service(request):
    if request.method == "POST":
        form = DemandePersoForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            try:
                # Sauvegarde du formulaire
                form.save()
                instance=form.instance
                image_url=request.build_absolute_uri(instance.picture.url)

                # Email de confirmation au client
                send_mail(
                    'Confirmation de votre demande',
                    f"Merci {form.cleaned_data['first_name']} {form.cleaned_data['last_name']},\n\n"
                    f"Nous avons bien reçu votre demande. Merci de nous avoir contactés ! "
                    f"Nous reviendrons vers vous très prochainement pour discuter des détails.\n\n"
                    f"Au plaisir de vous servir,\nL’équipe de Marihair",
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned_data['email']]
                )

                send_mail(
                    'Nouvelle demande personnalisée reçue',
                    f"Nouvelle demande personnalisée de {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}\n"
                    f"Téléphone : {form.cleaned_data['phone']}\n"
                    f"Email : {form.cleaned_data['email']}\n"
                    f"Photo : {image_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    ['marionnegannavi@gmail.com']
                )

            except BadHeaderError:
                return HttpResponse('En-tête de mail invalide.')
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'envoi de l'email : {str(e)}")

        else:
            print(form.errors)

        return render(request, 'services.html')
    else:
        form = DemandePersoForm()
    return render(request, 'services.html',{'form':form})

def reserver_service(request):
    if request.method == 'POST':
        print(request.POST)
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    'Confirmation de réservation',
                    f"Merci {form.cleaned_data['nom_client']} {form.cleaned_data['nom_famille']},\n\nNous avons bien reçu votre demande.",
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned_data['email']]
                )

                send_mail(
                    'Nouvelle réservation',
                    f"Nouvelle réservation de {form.cleaned_data['nom_client']} {form.cleaned_data['nom_famille']}\n"
                    f"Service : {form.cleaned_data['service_choice']}\n"
                    f"Numéro : {form.cleaned_data['num_phone']}\n"
                    f"Email : {form.cleaned_data['email']}",
                    settings.DEFAULT_FROM_EMAIL,
                    ['marionnegannavi@gmail.com']
                )
                print('Apres envoie : sa marche !!!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Erreur lors de l\'envoi de l\'email : {str(e)}')

            return render(request, 'services.html')
        else:
            print(form.errors)
    else:
        form = ReservationForm()
    return render(request, 'services.html',{'form':form})


