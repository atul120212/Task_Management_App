import json
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction

def load_users_from_json(sender, **kwargs):
    User = get_user_model()
    json_file_path = os.path.join(os.path.dirname(__file__), '../users.json')

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            users = json.load(file)
            with transaction.atomic():  # Ensures safe insertion
                for user_data in users:
                    if not User.objects.filter(email=user_data['email']).exists():
                        User.objects.create(
                            username=user_data['username'],
                            name=user_data['name'],
                            email=user_data['email'],
                            mobile=user_data['mobile'],
                            password=make_password(user_data['password'])
                        )
            print("✅ Users loaded successfully from JSON.")
