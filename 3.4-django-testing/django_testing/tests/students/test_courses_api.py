import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user('admin')

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory



@pytest.mark.django_db
def test_first_course(client, course_factory):
    courses = course_factory(_quantity = 5)

    response=client.get('/api/v1/courses/1/')
    data = response.json()


    assert response.status_code==200
    assert data['id'] == courses[0].id
    assert data['name'] == courses[0].name



@pytest.mark.django_db
def test_get_list(client, course_factory):
    courses = course_factory(_quantity = 5)

    response=client.get('/api/v1/courses/')
    data = response.json()

    print(courses)
    for i, m in enumerate(data):
        assert 1==1

@pytest.mark.django_db
def test_get_course_filter_id(client, course_factory):
    courses=course_factory(_quantity=5)
    course_first = Course.objects.order_by('pk')[0]
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data=response.json()
    
    assert response.status_code == 200
    assert data.get('id') == course_first.id

@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    courses=course_factory(_quantity=5)
    course_first = Course.objects.order_by('name')[0]
    response = client.get(f'/api/v1/courses/{course_first.id}/')
    data=response.json()
    
    assert response.status_code == 200
    assert data.get('id') == course_first.id

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    data={'name':'Netology'}
    response = client.post('/api/v1/courses/', data = data)
    assert response.status_code==201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity = 5)

    data_update = {'name':"NAME"}
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data = data_update)

    assert response.status_code==200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses=course_factory(_quantity=5)
    course = Course.objects.first()
    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204