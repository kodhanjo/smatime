from flask  import Blueprint
from flask import Flask


employes=Blueprint('employes',__name__)



from . import views,forms