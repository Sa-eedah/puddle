from django.contrib.auth.decorators import login_required 
# Import decorator to require user login for accessing views
from django.shortcuts import render, get_object_or_404,redirect
# Import shortcuts for rendering templates, getting objects, and redirecting

from item.models import Item # Import Item model from the item app
# Import form and models from this conversation app
from .forms import ConversationMessageForm
from .models import Conversation

# View to start a new conversation about an item

@login_required
def new_conversation(request, item_pk):
# Get the item or show 404 error if it doesn't exist
    item = get_object_or_404(Item, pk=item_pk)
# Prevent users from starting conversations with themselves about their own items
    if item.created_by == request.user:
        return redirect('dashboard:index')
# Check if a conversation already exists between this user and the item owner
    conversations = Conversation.objects.filter(item=item, members__in=[request.user.id])
# If conversation already exists, redirect to that existing conversation
    if conversations.exists():
        return redirect('conversation:detail', pk=conversations.first().id)
# Handle form submission (when user sends first message)
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # Create new conversation
            conversation = Conversation.objects.create(item=item)
            # Add both users as members (current user and item owner)
            conversation.members.add(request.user )
            conversation.members.add(item.created_by)
            conversation.save()
# Create the first message in the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
# Redirect back to the item detail page
            return redirect('item:detail', pk=item_pk)
    else:
        # Show empty form for GET request
        form = ConversationMessageForm()
# Render the new conversation template with the form
    return render(request, 'conversation/new.html', {
        'form': form
    })

# View to show user's inbox with all their conversations
@login_required
def inbox(request):
    # Get all conversations where the current user is a member
    conversations = Conversation.objects.filter(members__in=[request.user.id])
# Render inbox template with user's conversations
    return render(request, 'conversation/inbox.html',{
        'conversations': conversations
    })

# View to show details of a specific conversation and handle new messages
@login_required
def detail(request,pk):
    # Get conversation only if current user is a member (for security)
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
# Handle new message submission
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # Create new message in this conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            # Refresh page to show new message
            return redirect('conversation:detail', pk=pk)
    else:
        # Show empty form for new message
        form = ConversationMessageForm()
# Render conversation detail with all messages and form for new message
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
    })


            

 






