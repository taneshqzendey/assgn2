from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError

# Custom User Model

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, balance, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if int(balance)<0:
            raise ValueError("balance invalid")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            balance=balance
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email,balance, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if int(balance)<0:
            raise ValueError("balance invalid")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, primary_key=True)
    balance=models.PositiveBigIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def __str__(this):
        return this.transactid 
       
    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)
        # if CustomUser.objects.filter(email=self.email).exists():
        #     raise ValidationError({
        #         'email': 'This email is already in use. Please use a different email.'
        #     })
        # if CustomUser.objects.filter(username=self.username).exists():
        #     raise ValidationError({
        #         'username': 'This username is already in use. Please use a different username.'
        #     })
    
    def save(self, *args, **kwargs):
        self.validate_unique()
        super().save(*args, **kwargs)


class transactManager(models.Manager):
    def create_transact(payer,payee,amount,transactid):
        if not CustomUser.objects.filter(username=payee).exists():
            raise ValueError("invalid payee")
        if not CustomUser.objects.filter(username=payer).exists():
            raise ValueError("invalid payer")
        payee=CustomUser.objects.get(username=payee)
        payer=CustomUser.objects.get(username=payer)
        if payer.balance<amount:
            raise ValueError("Balance insufficient")
        if transact.objects.filter(transactid=transactid).exists():
            raise ValueError("Transaction id already used")
        payee.balance+=amount
        payer.balance-=amount
        transact= this.model()
        transact.payee=payee
        transact.payer=payer
        transact.amount=amount
        transact.saveit(using=this._db)
        return transact

class transact():
    payer=models.CharField(max_length=50)
    payee=models.CharField(max_length=50)
    amount=models.BigIntegerField()
    #transactid=payer + str(CustomUser.objects.get(payer).tr) + payee + str(CustomUser.objects.get(payee).tr) #(primary_key="True") 
    transactid=models.CharField(max_length=100,primary_key=True,unique=True)
    objects=transactManager()
    
    def saveit(self, *args,**kwargs):
        super(transact,self).save(*args,**kwargs)

