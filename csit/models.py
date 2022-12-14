from secrets import choice
from django.urls import reverse
from django.db import models


class Semester(models.Model):
	EASY ="EASY"
	MEDIUM = "MEDIUM"
	HARD = "HARD"
	

	DIFFICULT_LEVEL = [
		(EASY, "Easy"),
		(MEDIUM, "Medium"),
		(HARD, "Hard"),
		
	]
	title = models.CharField(max_length=80)	
	slug = models.SlugField(null = True, unique = True)
	content = models.TextField()
	difficulty = models.CharField(max_length=80, choices=DIFFICULT_LEVEL, default = MEDIUM)


	def __str__(self):
		return 	self.title

	

	
class Subject(models.Model):
	EASY ="EASY"
	MEDIUM = "MEDIUM"
	HARD = "HARD"
	

	DIFFICULT_LEVEL = [
		(EASY, "Easy"),
		(MEDIUM, "Medium"),
		(HARD, "Hard"),
		
	]
	title = models.CharField(max_length=80)
	semester = models.ForeignKey(Semester, on_delete=models.CASCADE ,null=True,related_name='subjects')
	code = models.TextField()
	difficulty = models.CharField(max_length=80, choices=DIFFICULT_LEVEL, default = MEDIUM)
	slug = models.SlugField(null = True, unique = True)
	fullMarks = models.CharField(max_length=90, default="60" , null= False)
	labMarks = models.CharField(max_length=90 , null= True, blank = True, default="20")

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('subject-detail', kwargs={'slug': self.slug})

	
class Category(models.Model):
	name = models.CharField(max_length=80, blank = False)

	def __str__(self):
		return self.name



class NoteFile(models.Model):
	link = models.URLField(blank=False, null = True)
	download_link = models.URLField(blank = False, null= True)
	sem = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="semester" , null =True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="files", null=True)
	category = models.ForeignKey(Category , on_delete=models.SET_NULL, related_name= "categories", null = True)
	name = models.CharField(max_length=80, blank = False, null = True)
	slug = models.SlugField(null= True, unique=True)

	def __str__(self) :
		return f'{self.subject} subject, in {self.category} category with name {self.name} ' 
		
	

class College(models.Model):

	TRIBHUVAN ="Tribhuvan University"
	KATHMANDU ="Kathmandu University"
	POKHARA ="Pokhara University"
	

	AFFILIATE = [
		(TRIBHUVAN, "Tribhuvan University"),
		(KATHMANDU, "Kathmandu University"),
		(POKHARA, "Pokhara University"),
		
	]
	name = models.CharField(max_length =90)
	fee = models.IntegerField()
	map_address = models.URLField()
	website = models.URLField()
	content = models.TextField()
	location = models.CharField(max_length=80, null= True, blank = False)
	phn_one = models.BigIntegerField(null= True, blank = False)
	phn_two = models.BigIntegerField(null= True, blank = True)
	affiliated = models.CharField(max_length =80 , choices = AFFILIATE, default = "Tribhuvan University")

	def __str__(self):
		return self.name