from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment
from .models import Notification


class NotificationModelTests(TestCase):
    def setUp(self):
        
        self.adam = User.objects.create_user(username="adam", password="pass")
        self.brian = User.objects.create_user(username="brian", password="pass")
        
        
        self.post = Post.objects.create(owner=self.adam, content="Adam's post content")

       
        self.comment = Comment.objects.create(owner=self.brian, post=self.post, content="Brian's comment")

    def test_create_comment_notification(self):
        
        notification = Notification.objects.create(
            recipient=self.adam,
            message="Brian commented on your post",
            notification_type="comment",
            related_object_id=self.comment.id,
            related_comment=self.comment
        )
        
        # Assertions
        self.assertEqual(notification.recipient, self.adam)
        self.assertEqual(notification.notification_type, "comment")
        self.assertEqual(notification.related_comment, self.comment)
        self.assertEqual(notification.message, "Brian commented on your post")
        self.assertFalse(notification.read)

    def test_create_like_notification(self):
       
        notification = Notification.objects.create(
            recipient=self.adam,
            message="Brian liked your post",
            notification_type="like",
            related_object_id=self.post.id,
            related_post=self.post
        )
        
        # Assertions
        self.assertEqual(notification.recipient, self.adam)
        self.assertEqual(notification.notification_type, "like")
        self.assertEqual(notification.related_post, self.post)
        self.assertEqual(notification.message, "Brian liked your post")
        self.assertFalse(notification.read)

    def test_create_follower_notification(self):
        
        notification = Notification.objects.create(
            recipient=self.adam,
            message="Brian started following you",
            notification_type="follower",
            related_object_id=self.brian.id,
        )
        
      
        self.assertEqual(notification.recipient, self.adam)
        self.assertEqual(notification.notification_type, "follower")
        self.assertEqual(notification.related_object_id, self.brian.id)
        self.assertEqual(notification.message, "Brian started following you")
        self.assertFalse(notification.read)

    def test_str_representation(self):
       
        notification = Notification.objects.create(
            recipient=self.adam,
            message="Test notification",
            notification_type="like",
            related_object_id=self.post.id,
            related_post=self.post
        )
        self.assertEqual(str(notification), f"{self.adam.username} - like - {notification.created_at}")

    def test_default_ordering(self):
        
        Notification.objects.create(
            recipient=self.adam,
            message="First notification",
            notification_type="comment",
            related_object_id=self.comment.id,
            related_comment=self.comment
        )
        Notification.objects.create(
            recipient=self.adam,
            message="Second notification",
            notification_type="like",
            related_object_id=self.post.id,
            related_post=self.post
        )

        notifications = Notification.objects.filter(recipient=self.adam).order_by('created_at')
        first_notification = notifications.first()
        last_notification = notifications.last()

        self.assertTrue(first_notification.created_at < last_notification.created_at)

