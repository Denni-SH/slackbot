from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from slackclient import SlackClient
from .models import Team, Message, Comment, CustUser
from .forms import UserCreation
from django.contrib.auth.models import User

def index(request):
    client_id = "280003673011.280124081140"
    return render(request, 'landing.html', {'client_id': client_id})

def slack_oauth(request):
    code = request.GET['code']
    # user = request.GET.get('event')

    # print(user)
    params = {
        'code': code,
        'client_id': "280003673011.280124081140",
        "client_secret": "b6ea12f5f0adfb110b2dca132ed11c28"
    }
    url = 'https://slack.com/api/oauth.access'
    json_response = requests.get(url, params)
    data = json.loads(json_response.text)
    workspace = Team.objects.get_or_create(
        name = data['team_name'],
        team_id = data['team_id'],
        bot_user_id = data['bot']['bot_user_id'],
        bot_access_token = data['bot']['bot_access_token'],
        channel_id = data['incoming_webhook']['channel_id']
    )
    # CustUser.objects.update_or_create(
    #             user=user,
    #             workspace=workspace.team_id,
    #             is_admin=True,
    #         )
    return redirect('/')

def message_save(request_resp, message_resp):
    Message.objects.get_or_create(
        ts = message_resp['ts'],
        text = message_resp['message']['text'],
        user_id = request_resp['user_id'],
        channel = message_resp['channel'],
        user_name = request_resp['user_name'],
        workspace = request_resp['team_id']
    )

def thread_save(data,res):
    Comment.objects.get_or_create(
        message=res,
        ts=data['event']['ts'],
        text=data['event']['text'],
        user_id=data['event']['user']
    )

@csrf_exempt
def post_message(request):
    request_resp = request.POST
    workspace = Team.objects.get(team_id=request_resp.get('team_id'))
    slack_client = SlackClient(workspace.bot_access_token)
    message_resp = slack_client.api_call(
                        'chat.postMessage',
                         channel=workspace.channel_id,
                         text="Пользователю <@%s> нужно отлучиться: `%s`" %(request_resp['user_name'],
                                                                        request_resp['text'])
                    )
    message_save(request_resp, message_resp)
    return HttpResponse('Sended!')

@csrf_exempt
def thread_event(request):
    data = json.loads(request.body.decode())
    print(data)
    if data.get('event').get('thread_ts'):
        res = Message.objects.get(ts=data['event']['thread_ts'])
        workspace = Team.objects.get(team_id=data['team_id'])
        slack_client = SlackClient(workspace.bot_access_token)
        message_resp = slack_client.api_call(
            'chat.postMessage',
            channel=res.user_id,
            text="<@%s> ответил: `%s`" %(data['event']['user'],
                                         data['event']['text'])
        )
        thread_save(data,res)
        return HttpResponse()
    else:
        return HttpResponseForbidden()


class TeamsListView(ListView):
   template_name = 'slackbot/index.html'
   model = Team
   context_object_name = 'workspaces'


def statistic(request,slug):
    messages = Message.objects.filter(workspace=slug)
    threads = Comment.objects.all()
    return render(request, 'slackbot/statistic.html', {'messages':messages, 'comments':threads})

def settings(request,slug):
    messages = Message.objects.filter(workspace=slug)
    threads = Comment.objects.all()
    return render(request, 'slackbot/manage.html', {'messages':messages, 'comments':threads})

# def add(request):
#     # messages = Message.objects.filter(workspace=slug)
#     # threads = Comment.objects.all()
#     return render(request, 'slackbot/add_app.html')

class SignUp(CreateView):
    template_name = "registration/register.html"
    model = User
    form_class = UserCreation
    success_url = "/"


class SignIn(LoginView):
    template_name = 'registration/login.html'

