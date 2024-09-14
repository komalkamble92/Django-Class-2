'''

from django.db.models import Avg

average_age = Student.objects.aggregate(Avg('age'))

from django.db.models import Count

tudents = models.ManyToManyField(Student, related_name='courses')

students_with_course_count = Student.objects.annotate(course_count=Count('courses')) #Todo

students = Student.objects.order_by('age')
students_desc = Student.objects.order_by('-age')

duplicate remove = Student.objects.distinct()

students_info = Student.objects.values('name', 'age')

student_names = Student.objects.values_list('name', flat=True)

FK

students = Student.objects.select_related('course')
students = Student.objects.prefetch_related('courses')

Student.objects.filter(age=20).update(age=21)

Student.objects.filter(age=21).delete()

student_count = Student.objects.filter(age=20).count()

first_student = Student.objects.first()
last_student = Student.objects.last()
has_students = Student.objects.filter(age=20).exists()

'''