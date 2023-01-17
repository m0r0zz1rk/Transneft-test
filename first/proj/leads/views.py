from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404

from leads.models import Lead


class LeadsChangeStatusViewSet(viewsets.ViewSet):
    """Изменение статуса объекта"""
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Смена статуса 'Новый' -> 'В работе'",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                required=True,
                type="integer",
                in_="path",
                description="ID объекта",
            ),
        ],
    )
    def lead_worked(self, request, **kwargs):
        obj = get_object_or_404(
            queryset=Lead.objects.all(),
            pk=self.kwargs['pk']
        )
        message = obj.lead_worked()
        return JsonResponse({'message': message})

    @swagger_auto_schema(
        operation_description="Смена статуса 'Новый' -> 'В работе'",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                required=True,
                type="integer",
                in_="path",
                description="ID объекта",
            ),
        ],
    )
    def lead_paused(self, request, **kwargs):
        obj = get_object_or_404(
            queryset=Lead.objects.all(),
            pk=self.kwargs['pk']
        )
        message = obj.lead_paused()
        return JsonResponse({'message': message})

    @swagger_auto_schema(
        operation_description="Смена статуса 'Новый' -> 'В работе'",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                required=True,
                type="integer",
                in_="path",
                description="ID объекта",
            ),
        ],
    )
    def lead_complete(self, request, **kwargs):
        obj = get_object_or_404(
            queryset=Lead.objects.all(),
            pk=self.kwargs['pk']
        )
        message = obj.lead_complete()
        return JsonResponse({'message': message})

    @swagger_auto_schema(
        operation_description="Смена статуса 'Новый' -> 'В работе'",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                required=True,
                type="integer",
                in_="path",
                description="ID объекта",
            ),
        ],
    )
    def lead_continue(self, request, **kwargs):
        obj = get_object_or_404(
            queryset=Lead.objects.all(),
            pk=self.kwargs['pk']
        )
        message = obj.lead_continue()
        return JsonResponse({'message': message})

    @swagger_auto_schema(
        operation_description="Смена статуса 'Новый' -> 'В работе'",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                required=True,
                type="integer",
                in_="path",
                description="ID объекта",
            ),
        ],
    )
    def lead_stop_complete(self, request, **kwargs):
        obj = get_object_or_404(
            queryset=Lead.objects.all(),
            pk=self.kwargs['pk']
        )
        message = obj.lead_stop_complete()
        return JsonResponse({'message': message})
