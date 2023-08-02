from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phon_number, email, full_name, password):
        if not phon_number:
            raise ValueError('شماره تلفن را باید بفرستید')
        if not email:
            raise ValueError('ایمیل را باید بفرستید')
        if not full_name:
            raise ValueError('اسم کامل را باید بفرستید')

        user = self.model(phone_number=phon_number, email=self.normalize_email(email),
                          full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user
