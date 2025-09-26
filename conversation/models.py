from django.contrib.auth.models import User
from django.db import models

from item.models import Item

# Model representing a conversation between users about a specific item
class Conversation(models.Model):
     # Link to the item this conversation is about
    # If item is deleted, conversation is also deleted (CASCADE)
    # related_name allows accessing conversations from Item: item.conversations.all()
    item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)
    # Users who are part of this conversation (usually 2: buyer and seller)
    # ManyToManyField allows multiple users per conversation
    # related_name allows accessing user's conversations: user.conversations.all()
    members = models.ManyToManyField(User, related_name='conversations')
    # Timestamp when conversation was first created
    # auto_now_add=True sets this automatically when conversation is created
    created_at = models.DateTimeField(auto_now_add=True)
     # Timestamp when conversation was last updated (when new message is added)
    # auto_now=True updates this automatically whenever conversation is saved
    modified_at  = models.DateTimeField(auto_now=True)

 # Meta class defines additional options for the model
    class Meta:
        # Order conversations by most recently modified first (newest first)
        # The minus sign (-) means descending order
        ordering = ('-modified_at',)

# Model representing individual messages within a conversation
class ConversationMessage(models.Model):
    # Link to which conversation this message belongs to
    # If conversation is deleted, all its messages are deleted too (CASCADE)
    # related_name allows accessing messages: conversation.messages.all()
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    # The actual message text content
    # TextField allows long text (unlike CharField which has length limits)
    content = models.TextField()
    # Timestamp when message was sent
    # auto_now_add=True sets this automatically when message is created
    created_at = models.DateTimeField(auto_now_add=True)
     # Which user sent this message
    # related_name allows accessing user's sent messages: user.created_messages.all()
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

