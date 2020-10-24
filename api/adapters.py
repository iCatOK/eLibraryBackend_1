from allauth.account.adapter import DefaultAccountAdapter
from api.models import Branch


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        user = super().save_user(request, user, form, False)

        user.full_name = request.data.get('full_name', '')
        user.username = request.data.get('username', '')
        branch_id = request.data.get('branch', '')
        if branch_id:
            branches = Branch.objects.filter(id=branch_id)
            if len(branches) == 0:
                return None
            user.branch = branches[0]
        user.save()
        return user
    

    def respond_email_verification_sent(self, request, user):
        pass