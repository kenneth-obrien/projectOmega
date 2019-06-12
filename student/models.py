# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'department'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    teacher_surname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'student'


class Studentoncourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentoncourses'


