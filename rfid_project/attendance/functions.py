from .models import User


def add_user(number):
	max_id = User.objects.all().order_by('-card_id').first().card_id
	start_id = max_id + 1
	for user_index in range(number):
		User.objects.create(card_id=start_id)
		start_id += 1
