import re
from django.shortcuts import render
from django.http import JsonResponse
from .models import Clinics
from .serializers import ClinicSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


@api_view(["GET", "POST"])
def clinic_list(request):

    if request.method == "GET":
        all_clinics = Clinics.objects.filter(id__isnull=False).values()
        serializer = ClinicSerializer(all_clinics, many=True)
        name = request.GET.get("name", "")
        onclick = request.GET.get("click", None)
        if onclick:
            data = list(Clinics.objects.filter(id=onclick).values())
            if data:
                return Response(data={"clinic_details": data})
            else:
                return Response(data={"clinic_details": "NOT FOUND"})
        if name:
            return Response(
                data={
                    "searched": list(
                        Clinics.objects.filter(name=name).values_list("name", flat=True)
                    )[0]
                    if list(
                        Clinics.objects.filter(name=name).values_list("name", flat=True)
                    )
                    else "NOT FOUND"
                }
            )
        # print(serializer.data)
        # return JsonResponse({"Clinics": serializer.data}, safe=False)
        return JsonResponse({"data": serializer.data}, safe=False)
        return Response(data={"clinics": list(all_clinics)})
    if request.method == "POST":
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)
