from django.db import models
from datetime import datetime

states_choices = (
		("1","Andhra Pradesh"),
		("2 ","Arunachal Pradesh "),
		("3","Assam"),
		("Bihar","Bihar"),
		("Chhattisgarh","Chhattisgarh"),
		("Goa","Goa"),
		("Gujarat","Gujarat"),
		("Haryana","Haryana"),
		("Himachal Pradesh","Himachal Pradesh"),
		("Jammu and Kashmir","Jammu and Kashmir"),
		("Jharkhand","Jharkhand"),
		("Karnataka","Karnataka"),
		("Kerala","Kerala"),
		("Madhya Pradesh","Madhya Pradesh"),
		("Maharashtra","Maharashtra"),
		("Manipur","Manipur"),
		("Meghalaya","Meghalaya"),
		("Mizoram","Mizoram"),
		("Nagaland","Nagaland"),
		("Odisha","Odisha"),
		("Punjab","Punjab"),
		("Rajasthan","Rajasthan"),
		("Sikkim","Sikkim"),
		("Tamil Nadu","Tamil Nadu"),
		("Telangana","Telangana"),
		("Tripura","Tripura"),
		("Uttar Pradesh","Uttar Pradesh"),
		("Uttarakhand","Uttarakhand"),
		("West Bengal","West Bengal"),
		("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
		("Chandigarh","Chandigarh"),
		("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
		("Daman and Diu","Daman and Diu"),
		("Lakshadweep","Lakshadweep"),
		("National Capital Territory of Delhi","National Capital Territory of Delhi"),
		("Puducherry","Puducherry")
	)


# Create your models here.
class Orphanage(models.Model):
	orphanage_name = models.CharField(max_length=200)
	image = models.ImageField(upload_to="orphanage/images/")
	establish_date = models.DateField(default=datetime.date(datetime.now()))
	about = models.TextField()
	address = models.TextField()
	state = models.CharField(max_length=35, choices=states_choices)
	contact_no = models.CharField(max_length=15)
	site_url = models.CharField(max_length=200)
	email = models.EmailField(max_length=150)
	children_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.orphanage_name

class Orphan(models.Model):
	gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Other")]
	orphan_name = models.CharField(max_length=200)
	orphan_image = models.ImageField(upload_to="orphan/images/")
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=10, choices=gender_choices)
	admit_to = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.orphan_name


class Event(models.Model):
	event_name = models.CharField(max_length=500)
	event_type = models.CharField(max_length=300)
	poster = models.ImageField(default="", upload_to="events/images")
	description = models.TextField()
	event_date = models.DateField(default=datetime.date(datetime.now()))
	event_time = models.TimeField(default=datetime.time(datetime.now()))
	organised_by = models.ForeignKey(Orphanage, on_delete = models.CASCADE)
	venue = models.TextField()

	def __str__(self):
		return self.event_name


class Feedback(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	review = models.TextField()
	email = models.EmailField()
	mobile_no = models.CharField(max_length=15)
	feedback_for = models.ForeignKey(Orphanage, on_delete=models.CASCADE)

	def  __str__(self):
		return self.title

