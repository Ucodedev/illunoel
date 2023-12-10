import requests

# Remplacez par votre jeton d'authentification
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0NThhMTAwNDExZjM0OGRmYjdiZGZiODA3YzVhNjkwNSIsImlhdCI6MTcwMjIxMjc2MCwiZXhwIjoyMDE3NTcyNzYwfQ.ox5QplvGP6U1JCL4J4x5gj2it_otO0Q7oDAcmsxTNss"

# Entités à allumer
entity_ids = ["switch.prise_bureau_socket_1", "switch.prise_3d_socket_1"]

# URL de l'API Home Assistant
api_url = "http://craftinc.duckdns.org:8123/api/services/switch/turn_off"

# Construire le corps de la requête JSON
data = {
    "entity_id": entity_ids
}

# Construire les en-têtes de la requête
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}

# Effectuer la requête POST
response = requests.post(api_url, json=data, headers=headers)