from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

resultado_do_request = None

@csrf_exempt
def leitor(request):

  global resultado_do_request
  if request.method == 'POST':
    
      # Obtenha o JSON do corpo da solicitação
      try:
          json_data = json.loads(request.body.decode('utf-8'))
      except json.JSONDecodeError as e:
          return JsonResponse({'error': f'Erro ao decodificar JSON, {e}'}, status=400)

      # Obtenha o valor do atributo 'presença'
      presenca = json_data.get('presença', None)

      if presenca is not None:
          # Faça algo com o valor
          resultado_do_request = presenca
          return JsonResponse({'mensagem': f'Valor de presença: {presenca}'})
      else:
          return JsonResponse({'error': 'Atributo "presença" ausente no JSON'}, status=400)
  return JsonResponse({'error': 'Somente métodos POST são permitidos'}, status=405)

@require_GET
def ilumina(request):
  global resultado_do_request
  if request.method == 'GET':
    if resultado_do_request is not None:
      return JsonResponse({'presença': f'{resultado_do_request}'})
    else:
      return JsonResponse({'error': 'Nenhum valor de presença encontrado'}, status=400)
  return JsonResponse({'error': 'Somente métodos POST são permitidos'}, status=405)