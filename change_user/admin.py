# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class UserAdmin(admin.ModelAdmin):
    ordering = ('username',)
    list_per_page = 500
    actions = ['become', 'delete_selected']

    def become(self, request, queryset):
        if not request.user.is_superuser:
            messages.add_message(request, messages.INFO, 'You are not superuser.')
        user = queryset[0]
        request.session['_auth_user_id'] = user.id
        return HttpResponseRedirect('/')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
