from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Profile, Rate
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.forms import *
from rest_framework import viewsets
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)