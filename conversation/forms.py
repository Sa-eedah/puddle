from django import forms

from .models import ConversationMessage

# Form for creating new messages in a conversation
# ModelForm automatically creates form fields based on the model
class ConversationMessageForm(forms.ModelForm):
    # Meta class defines which model and fields to use for this form
    class Meta:
        # Base this form on the ConversationMessage model
        model = ConversationMessage
         # Only include the 'content' field in the form
        # Other fields like conversation, created_by, created_at are set in the view
        fields = ('content',)
        # Customize how the form fields look in HTML
        widgets = {
            # Style the content field as a single-line text input instead of textarea
            # Apply Tailwind CSS classes for styling: full width, padding, rounded corners, border
            'content': forms.TextInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl border'
            }),     
        } 
