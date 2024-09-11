from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment
from followers.models import Follower
from likes.models import Like
from .models import Notification

def create_notification(sender, recipient, message, notification_type, related_object_id=None, related_post=None, related_comment=None):
    if sender != recipient:
        Notification.objects.create(
            recipient=recipient,
            message=message,
            notification_type=notification_type,
            related_object_id=related_object_id,
            related_post=related_post,
            related_comment=related_comment
        )


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
        create_notification(
            sender=instance.owner,
            recipient=instance.post.owner,
            message=f"You got a comment on your post by {instance.owner.username}",
            notification_type="comment",
            related_object_id=instance.post.id,
            related_comment=instance
        )

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        create_notification(
            sender=instance.owner,
            recipient=instance.post.owner,
            message=f"You got a like on your by {instance.owner.username}",
            notification_type="like",
            related_object_id=instance.post.id,
        )



@receiver(post_save, sender=Follower)
def create_follower_notification(sender, instance, created, **kwargs):
    if created:
        create_notification(
            sender=instance.owner,
            recipient=instance.followed,
            message=f"You got a new follower: {instance.owner.username}",
            notification_type="follower",
            related_object_id=instance.owner.id,
        )
