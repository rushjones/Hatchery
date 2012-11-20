from django.template.response import templateresponse

import models

def team_list(request):

"""
list all teams in database
"""
teams = models.Team.objects.all().order_by('name')
return TemplateResponse(request, 'softball/teams/list.html', {
	'teams': teams,
})


