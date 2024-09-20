from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase

class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_events(self):
        adam = User.objects.get(username='adam')
        Event.objects.create(owner=adam, title='event title', event_date='2024-10-20', description="Event description")
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'a title', 'event_date': '2024-10-20', 'description': 'A description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Event.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_create_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post(
            '/events/', {
                'title': 'a title', 
                'event_date': '2024-10-20',
                'description': 'A sample event description',
                'tags': 'tag'
            }
        )
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class EventDetailViewTests(APITestCase):
    """
    Tests for the Event model detail view
    """
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        
        event1 = Event.objects.create(
            owner=adam,
            title='a title',
            description='adams event',
            event_date='2024-09-25'
        )
        event2 = Event.objects.create(
            owner=brian,
            title='another title',
            description='brians event',
            event_date='2024-10-01'
        )
        
        event1.tags.add('tag')
        event2.tags.add('sport')

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/events/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/events/1/', 
            {
                'title': 'an edited title', 
                'event_date': '2024-09-25',
                'description': 'an updated description',
                'tags': ['tag']
            }
        )
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.title, 'an edited title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            '/events/2/', 
            {
                'title': 'an edited title', 
                'event_date': '2024-10-01',
                'description': 'an updated description',
                'tags': ['sport']
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.delete('/events/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someone_elses_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.delete('/events/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

