from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, related_name='blog_post',on_delete=models.CASCADE,default='')
    blog_img = models.ImageField(upload_to='blog_imgage/')
    blog_desc = models.TextField()
    blog_sub_title = models.CharField(max_length=100,blank=True,default='')
    blog_sub_desc = models.TextField(blank=True,default='')
    blog_sub_title1 = models.CharField(max_length=100, blank=True, default='')
    blog_sub_desc1 = models.TextField(blank=True, default='')
    blog_sub_title2 = models.CharField(max_length=100, blank=True, default='')
    blog_sub_desc2 = models.TextField(blank=True, default='')
    blog_sub_title3 = models.CharField(max_length=100, blank=True, default='')
    blog_sub_desc3 = models.TextField(blank=True, default='')
    blog_sub_title4 = models.CharField(max_length=100, blank=True, default='')
    blog_sub_desc4 = models.TextField(blank=True, default='')
    blog_sub_title5 = models.CharField(max_length=100, blank=True, default='')
    blog_sub_desc5 = models.TextField(blank=True, default='')
    blog_sub_img = models.ImageField(upload_to='blog_imgage/sub_blog',blank=True, default='')
    blog_sub_img1 = models.ImageField(upload_to='blog_imgage/sub_blog',blank=True, default='')
    publish = models.DateTimeField(default=timezone.now)
    blog_created_date = models.DateTimeField(auto_now_add=True)
    blog_updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog_details',args=[self.slug])

#Index page model create start here--
class IndexDevService(models.Model):
    service_title = models.CharField(max_length=50)
    service_title_desc = models.TextField()

class IndexServiceList(models.Model):
    service_name = models.CharField(max_length=100)
    service_img = models.ImageField(upload_to='index_img/service')
    service_url = models.CharField(max_length=20)
    service_created_date = models.DateTimeField(auto_now_add=True)
    service_updated_date = models.DateTimeField(auto_now=True)

class IndexAdress(models.Model):
    country_name = models.CharField(max_length=30)
    state_name = models.CharField(max_length=50)
    office_address = models.CharField(max_length=200)
    adress_url = models.CharField(max_length=500)
    address_created_date = models.DateTimeField(auto_now_add=True)
    address_updated_date = models.DateTimeField(auto_now=True)

class IndexProject(models.Model):
    project_head = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100)
    project_name = models.CharField(max_length=50)
    language_used1 = models.CharField(max_length=30)
    language_used2 = models.CharField(max_length=30)
    language_used3 = models.CharField(max_length=30)
    language_used4 = models.CharField(max_length=30)
    project_desc1 = models.TextField()
    project_desc2 = models.TextField(default='')
    project_img = models.ImageField(upload_to='project_img/',default='')
    project_created_date = models.DateTimeField(auto_now_add=True)
    project_updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('projects_details',args=[self.slug])

class ClientSpeaks(models.Model):
    client_name = models.CharField(max_length=30)
    client_company_name = models.CharField(max_length=30)
    client_comment = models.CharField(max_length=600)
    client_img = models.ImageField(default='default.png')
    client_created_date = models.DateTimeField(auto_now_add=True)

class WhyCompany(models.Model):
    why_title = models.CharField(max_length=50)
    why_desc = models.TextField()
    why_created_date = models.DateTimeField(auto_now_add=True)
    why_updated_date = models.DateTimeField(auto_now=True)

# Carrer page model creation start here ...

class CarrerPage(models.Model):
    career_title = models.CharField(max_length=100)
    carrer_heading = models.CharField(max_length=100)
    career_title1 = models.CharField(max_length=100)
    carrer_heading1 = models.CharField(max_length=100)
    carrer_desc = models.TextField()
    career_title2 = models.CharField(max_length=100)
    carrer_heading2 = models.CharField(max_length=100)
    carrer_desc1 = models.TextField()
    carrer_img = models.ImageField(upload_to='carrer_img/')
    carrer_img1 = models.ImageField(upload_to='carrer_img/')
    carrer_created_date = models.DateTimeField(auto_now_add=True)
    carrer_updated_date = models.DateTimeField(auto_now=True)

class JobOpening(models.Model):
    technology_language = models.CharField(max_length=100)
    job_desc = models.TextField()
    job_location = models.CharField(max_length=100)
    job_qulification = models.CharField(max_length=100)
    job_experience = models.CharField(max_length=200)
    job_about1 = models.CharField(max_length=200,blank=True)
    job_about2 = models.CharField(max_length=200, blank=True)
    job_about3 = models.CharField(max_length=200, blank=True)
    job_about4 = models.CharField(max_length=200, blank=True)
    job_about5 = models.CharField(max_length=200, blank=True)
    job_about6 = models.CharField(max_length=200, blank=True)
    job_about7 = models.CharField(max_length=200, blank=True)
    job_about8 = models.CharField(max_length=200, blank=True)
    job_about9 = models.CharField(max_length=200, blank=True)
    job_about10 = models.CharField(max_length=200, blank=True)
    job_about11 = models.CharField(max_length=200, blank=True)
    job_about12 = models.CharField(max_length=200, blank=True)
    job_created_date = models.DateTimeField(auto_now_add=True)
    job_updated_date = models.DateTimeField(auto_now=True)

class OurTeam(models.Model):
    team_name = models.CharField(max_length=55)
    team_designation = models.CharField(max_length=55)
    team_image = models.ImageField(upload_to='team_img/')
    team_created_date = models.DateTimeField(auto_now_add=True)
    team_updated_date = models.DateTimeField(auto_now=True)

class DevelopmentProcess(models.Model):
    dev_process = models.CharField(max_length=55)
    dev_desc = models.TextField()
    dev_image = models.ImageField(upload_to='dev_img/')
    dev_created_date = models.DateTimeField(auto_now_add=True)
    dev_updated_date = models.DateTimeField(auto_now=True)

class Support(models.Model):
    support_desc = models.TextField()
    support_image = models.ImageField(upload_to='support_img/')
    support_contact_titledesc = models.CharField(max_length=251,default='')
    support_contact_name = models.CharField(max_length=51)
    support_contact_designation = models.CharField(max_length=51)
    support_contact_title = models.CharField(max_length=251)
    support_contact_image = models.ImageField(upload_to='support_img/contact_img')
    support_contact_skypeid = models.CharField(max_length=51,default='')
    support_contact_emailid = models.CharField(max_length=51,default='')
    support_contact_name1 = models.CharField(max_length=51)
    support_contact_designation1 = models.CharField(max_length=51)
    support_contact_title1 = models.CharField(max_length=251)
    support_contact_image1 = models.ImageField(upload_to='support_img/contact_img')
    support_contact_skypeid1 = models.CharField(max_length=51,default='')
    support_contact_emailid1 = models.CharField(max_length=51,default='')
    support_created_date = models.DateTimeField(auto_now_add=True)
    support_updated_date = models.DateTimeField(auto_now=True)

#PHP Development Page Model

class FaqPhpDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class FaqIosDev1(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()

class GetStartPhp(models.Model):
    php_title = models.CharField(max_length=251)
    php_desc = models.CharField(max_length=551)
    php_img1 = models.ImageField(upload_to='Php_ico_img/')
    php_img_title1 = models.CharField(max_length=151)
    php_img2 = models.ImageField(upload_to='Php_ico_img/')
    php_img_title2 = models.CharField(max_length=151)
    php_img3 = models.ImageField(upload_to='Php_ico_img/')
    php_img_title3 = models.CharField(max_length=151)
    php_img4 = models.ImageField(upload_to='Php_ico_img/')
    php_img_title4 = models.CharField(max_length=151)

class ProjectList(models.Model):
    project_sort_desc = models.CharField(max_length=552)
    project_name = models.CharField(max_length=151)
    project_name_app = models.CharField(max_length=151)
    project_technology_used1 = models.CharField(max_length=51, blank=True)
    project_technology_used2 = models.CharField(max_length=51, blank=True)
    project_technology_used3 = models.CharField(max_length=51, blank=True)
    project_technology_used4 = models.CharField(max_length=51, blank=True)
    project_technology_used5 = models.CharField(max_length=51, blank=True)
    project_technology_used6 = models.CharField(max_length=51, blank=True)
    project_desc = models.TextField()
    project_img = models.ImageField(upload_to='Project_Img/')

class DevProcessPhp(models.Model):
    dev_title = models.CharField(max_length=51)
    dev_img = models.ImageField(upload_to='PHP_img/')
    dev_desc = models.TextField()
    dev_img_screen = models.ImageField(upload_to='PHP_img/laptop_screen')

class AddValuePhp(models.Model):
    add_value_php_title = models.CharField(max_length=51)
    add_value_php_img = models.ImageField(upload_to='PHP_img/add_value')
    add_value_php_desc = models.TextField()

class SolutionExpertisePhp(models.Model):
    sol_exper_php_title = models.CharField(max_length=51)
    sol_exper_php_img = models.ImageField(upload_to='PHP_img/solution_expertise')

class DevServicePhp(models.Model):
    dev_service_php_title = models.CharField(max_length=51)
    dev_servic_php_img = models.ImageField(upload_to='PHP_img/dev_service')

class DevServiceDescPhp(models.Model):
    dev_service_php_desc = models.CharField(max_length=551)

class PhpDevCompany(models.Model):
    php_dev_title = models.CharField(max_length=51)
    php_dev_desc = models.TextField()
    php_dev_img = models.ImageField(upload_to='PHP_img/php_dev_company')

#Django Web Devlopment Service

class FaqDjangoDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartDjango(models.Model):
    django_title = models.CharField(max_length=251)
    django_desc = models.CharField(max_length=551)
    django_img1 = models.ImageField(upload_to='django_ico_img/')
    django_img_title1 = models.CharField(max_length=151)
    django_img2 = models.ImageField(upload_to='django_ico_img/')
    django_img_title2 = models.CharField(max_length=151)
    django_img3 = models.ImageField(upload_to='django_ico_img/')
    django_img_title3 = models.CharField(max_length=151)
    django_img4 = models.ImageField(upload_to='django_ico_img/')
    django_img_title4 = models.CharField(max_length=151)

class DevProcessDjango(models.Model):
    dev_django_title = models.CharField(max_length=51)
    dev_django_img = models.ImageField(upload_to='Django_img/')
    dev_django_desc = models.TextField()
    dev_django_img_screen = models.ImageField(upload_to='Django_img/laptop_screen')

class AddValueDjango(models.Model):
    add_value_django_title = models.CharField(max_length=51)
    add_value_django_img = models.ImageField(upload_to='Django_img/add_value')
    add_value_django_desc = models.TextField()

class SolutionExpertiseDjango(models.Model):
    sol_exper_django_title = models.CharField(max_length=51)
    sol_exper_django_img = models.ImageField(upload_to='Django_img/solution_expertise')

class DevServiceDjango(models.Model):
    dev_service_django_title = models.CharField(max_length=51)
    dev_servic_django_img = models.ImageField(upload_to='Django_img/dev_service')

class DevServiceDescDjango(models.Model):
    dev_service_django_desc = models.CharField(max_length=551)

class DjangoDevCompany(models.Model):
    django_dev_title = models.CharField(max_length=51)
    django_dev_desc = models.TextField()
    django_dev_img = models.ImageField(upload_to='Django_img/django_dev_company')


#Python Web Devlopment Service

class FaqPythonDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartPython(models.Model):
    python_title = models.CharField(max_length=251)
    python_desc = models.CharField(max_length=551)
    python_img1 = models.ImageField(upload_to='python_ico_img/')
    python_img_title1 = models.CharField(max_length=151)
    python_img2 = models.ImageField(upload_to='python_ico_img/')
    python_img_title2 = models.CharField(max_length=151)
    python_img3 = models.ImageField(upload_to='python_ico_img/')
    python_img_title3 = models.CharField(max_length=151)
    python_img4 = models.ImageField(upload_to='python_ico_img/')
    python_img_title4 = models.CharField(max_length=151)

class DevProcessPython(models.Model):
    dev_python_title = models.CharField(max_length=51)
    dev_python_img = models.ImageField(upload_to='python_img/')
    dev_python_desc = models.TextField()
    dev_python_img_screen = models.ImageField(upload_to='python_img/laptop_screen')

class AddValuePython(models.Model):
    add_value_python_title = models.CharField(max_length=51)
    add_value_python_img = models.ImageField(upload_to='python_img/add_value')
    add_value_python_desc = models.TextField()

class SolutionExpertisePython(models.Model):
    sol_exper_python_title = models.CharField(max_length=51)
    sol_exper_python_img = models.ImageField(upload_to='python_img/solution_expertise')

class DevServicePython(models.Model):
    dev_service_python_title = models.CharField(max_length=51)
    dev_servic_python_img = models.ImageField(upload_to='python_img/dev_service')

class DevServiceDescPython(models.Model):
    dev_service_python_desc = models.CharField(max_length=551)

class PythonDevCompany(models.Model):
    python_dev_title = models.CharField(max_length=51)
    python_dev_desc = models.TextField()
    python_dev_img = models.ImageField(upload_to='python_img/django_dev_company')



#Laravel Web Devlopment Service

class FaqLaravelDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartLaravel(models.Model):
    laravel_title = models.CharField(max_length=251)
    laravel_desc = models.CharField(max_length=551)
    laravel_img1 = models.ImageField(upload_to='laravel_ico_img/')
    laravel_img_title1 = models.CharField(max_length=151)
    laravel_img2 = models.ImageField(upload_to='laravel_ico_img/')
    laravel_img_title2 = models.CharField(max_length=151)
    laravel_img3 = models.ImageField(upload_to='laravel_ico_img/')
    laravel_img_title3 = models.CharField(max_length=151)
    laravel_img4 = models.ImageField(upload_to='laravel_ico_img/')
    laravel_img_title4 = models.CharField(max_length=151)

class DevProcessLaravel(models.Model):
    dev_laravel_title = models.CharField(max_length=51)
    dev_laravel_img = models.ImageField(upload_to='laravel_img/')
    dev_laravel_desc = models.TextField()
    dev_laravel_img_screen = models.ImageField(upload_to='laravel_img/laptop_screen')

class AddValueLaravel(models.Model):
    add_value_laravel_title = models.CharField(max_length=51)
    add_value_laravel_img = models.ImageField(upload_to='laravel_img/add_value')
    add_value_laravel_desc = models.TextField()

class SolutionExpertiseLaravel(models.Model):
    sol_exper_laravel_title = models.CharField(max_length=51)
    sol_exper_laravel_img = models.ImageField(upload_to='laravel_img/solution_expertise')

class DevServiceLaravel(models.Model):
    dev_service_laravel_title = models.CharField(max_length=51)
    dev_servic_laravel_img = models.ImageField(upload_to='laravel_img/dev_service')

class DevServiceDescLaravel(models.Model):
    dev_service_laravel_desc = models.CharField(max_length=551)

class LaravelDevCompany(models.Model):
    laravel_dev_title = models.CharField(max_length=51)
    laravel_dev_desc = models.TextField()
    laravel_dev_img = models.ImageField(upload_to='laravel_img/django_dev_company')


#Wordpress Web Devlopment Service

class FaqWordpressDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartWordpress(models.Model):
    wordpress_title = models.CharField(max_length=251)
    wordpress_desc = models.CharField(max_length=551)
    wordpress_img1 = models.ImageField(upload_to='wordpress_ico_img/')
    wordpress_img_title1 = models.CharField(max_length=151)
    wordpress_img2 = models.ImageField(upload_to='wordpress_ico_img/')
    wordpress_img_title2 = models.CharField(max_length=151)
    wordpress_img3 = models.ImageField(upload_to='wordpress_ico_img/')
    wordpress_img_title3 = models.CharField(max_length=151)
    wordpress_img4 = models.ImageField(upload_to='wordpress_ico_img/')
    wordpress_img_title4 = models.CharField(max_length=151)

class DevProcessWordpress(models.Model):
    dev_wordpress_title = models.CharField(max_length=51)
    dev_wordpress_img = models.ImageField(upload_to='wordpress_img/')
    dev_wordpress_desc = models.TextField()
    dev_wordpress_img_screen = models.ImageField(upload_to='laravel_img/laptop_screen')

class AddValueWordpress(models.Model):
    add_value_wordpress_title = models.CharField(max_length=51)
    add_value_wordpress_img = models.ImageField(upload_to='wordpress_img/add_value')
    add_value_wordpress_desc = models.TextField()

class SolutionExpertiseWordpress(models.Model):
    sol_exper_wordpress_title = models.CharField(max_length=51)
    sol_exper_wordpress_img = models.ImageField(upload_to='wordpress_img/solution_expertise')

class DevServiceWordpress(models.Model):
    dev_service_wordpress_title = models.CharField(max_length=51)
    dev_servic_wordpress_img = models.ImageField(upload_to='wordpress_img/dev_service')

class DevServiceDescWordpress(models.Model):
    dev_service_wordpress_desc = models.CharField(max_length=551)

class WordpressDevCompany(models.Model):
    wordpress_dev_title = models.CharField(max_length=51)
    wordpress_dev_desc = models.TextField()
    wordpress_dev_img = models.ImageField(upload_to='wordpress_img/django_dev_company')


#IOS App Development Web Devlopment Service

class FaqIosAPPDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartIosAPP(models.Model):
    iosapp_title = models.CharField(max_length=251)
    iosapp_desc = models.CharField(max_length=551)
    iosapp_img1 = models.ImageField(upload_to='iosapp_ico_img/')
    iosapp_img_title1 = models.CharField(max_length=151)
    iosapp_img2 = models.ImageField(upload_to='iosapp_ico_img/')
    iosapp_img_title2 = models.CharField(max_length=151)
    iosapp_img3 = models.ImageField(upload_to='iosapp_ico_img/')
    iosapp_img_title3 = models.CharField(max_length=151)
    iosapp_img4 = models.ImageField(upload_to='iosapp_ico_img/')
    iosapp_img_title4 = models.CharField(max_length=151)

class DevProcessIosAPP(models.Model):
    dev_iosapp_title = models.CharField(max_length=51)
    dev_iosapp_img = models.ImageField(upload_to='iosapp_img/')
    dev_iosapp_desc = models.TextField()
    dev_iosapp_img_screen = models.ImageField(upload_to='iosapp_img/laptop_screen')

class AddValueIosAPP(models.Model):
    add_value_iosapp_title = models.CharField(max_length=51)
    add_value_iosapp_img = models.ImageField(upload_to='iosapp_img/add_value')
    add_value_iosapp_desc = models.TextField()

class SolutionExpertiseIosAPP(models.Model):
    sol_exper_iosapp_title = models.CharField(max_length=51)
    sol_exper_iosapp_img = models.ImageField(upload_to='iosapp_img/solution_expertise')

class DevServiceIosAPP(models.Model):
    dev_service_iosapp_title = models.CharField(max_length=51)
    dev_servic_iosapp_img = models.ImageField(upload_to='iosapp_img/dev_service')

class DevServiceDescIosAPP(models.Model):
    dev_service_iosapp_desc = models.CharField(max_length=551)

class IosAPPDevCompany(models.Model):
    iosapp_dev_title = models.CharField(max_length=51)
    iosapp_dev_desc = models.TextField()
    iosapp_dev_img = models.ImageField(upload_to='iosapp_img/django_dev_company')


#Android App Development Web Devlopment Service

class FaqAndroidAPPDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartAndroidAPP(models.Model):
    android_title = models.CharField(max_length=251)
    android_desc = models.CharField(max_length=551)
    android_img1 = models.ImageField(upload_to='android_ico_img/')
    android_img_title1 = models.CharField(max_length=151)
    android_img2 = models.ImageField(upload_to='android_ico_img/')
    android_img_title2 = models.CharField(max_length=151)
    android_img3 = models.ImageField(upload_to='android_ico_img/')
    android_img_title3 = models.CharField(max_length=151)
    android_img4 = models.ImageField(upload_to='android_ico_img/')
    android_img_title4 = models.CharField(max_length=151)

class DevProcessAndroidAPP(models.Model):
    dev_android_title = models.CharField(max_length=51)
    dev_android_img = models.ImageField(upload_to='android_img/')
    dev_android_desc = models.TextField()
    dev_android_img_screen = models.ImageField(upload_to='android_img/laptop_screen')

class AddValueAndroidAPP(models.Model):
    add_value_android_title = models.CharField(max_length=51)
    add_value_android_img = models.ImageField(upload_to='android_img/add_value')
    add_value_android_desc = models.TextField()

class SolutionExpertiseAndroidAPP(models.Model):
    sol_exper_android_title = models.CharField(max_length=51)
    sol_exper_android_img = models.ImageField(upload_to='android_img/solution_expertise')

class DevServiceAndroidAPP(models.Model):
    dev_service_android_title = models.CharField(max_length=51)
    dev_servic_android_img = models.ImageField(upload_to='android_img/dev_service')

class DevServiceDescAndroidAPP(models.Model):
    dev_service_android_desc = models.CharField(max_length=551)

class AndroidAPPDevCompany(models.Model):
    android_dev_title = models.CharField(max_length=51)
    android_dev_desc = models.TextField()
    android_dev_img = models.ImageField(upload_to='android_img/django_dev_company')

#Magento App Development Web Devlopment Service

class FaqMagentoDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartMagento(models.Model):
    magento_title = models.CharField(max_length=251)
    magento_desc = models.CharField(max_length=551)
    magento_img1 = models.ImageField(upload_to='magento_ico_img/')
    magento_img_title1 = models.CharField(max_length=151)
    magento_img2 = models.ImageField(upload_to='magento_ico_img/')
    magento_img_title2 = models.CharField(max_length=151)
    magento_img3 = models.ImageField(upload_to='magento_ico_img/')
    magento_img_title3 = models.CharField(max_length=151)
    magento_img4 = models.ImageField(upload_to='magento_ico_img/')
    magento_img_title4 = models.CharField(max_length=151)

class DevProcessMagento(models.Model):
    dev_magento_title = models.CharField(max_length=51)
    dev_magento_img = models.ImageField(upload_to='magento_img/')
    dev_magento_desc = models.TextField()
    dev_magento_img_screen = models.ImageField(upload_to='magento_img/laptop_screen')

class AddValueMagento(models.Model):
    add_value_magento_title = models.CharField(max_length=51)
    add_value_magento_img = models.ImageField(upload_to='magento_img/add_value')
    add_value_magento_desc = models.TextField()

class SolutionExpertiseMagento(models.Model):
    sol_exper_magento_title = models.CharField(max_length=51)
    sol_exper_magento_img = models.ImageField(upload_to='magento_img/solution_expertise')

class DevServiceMagento(models.Model):
    dev_service_magento_title = models.CharField(max_length=51)
    dev_servic_magento_img = models.ImageField(upload_to='magento_img/dev_service')

class DevServiceDescMagento(models.Model):
    dev_service_magento_desc = models.CharField(max_length=551)

class MagentoDevCompany(models.Model):
    magento_dev_title = models.CharField(max_length=51)
    magento_dev_desc = models.TextField()
    magento_dev_img = models.ImageField(upload_to='magento_img/django_dev_company')

#Drupal App Development Web Devlopment Service

class FaqDrupalDev(models.Model):
    question1 =models.CharField(max_length=250)
    answer1 =models.TextField()
    question2 =models.CharField(max_length=250)
    answer2 =models.TextField()
    question3 =models.CharField(max_length=250)
    answer3 =models.TextField()
    question4 =models.CharField(max_length=250)
    answer4 =models.TextField()

class GetStartDrupal(models.Model):
    drupal_title = models.CharField(max_length=251)
    drupal_desc = models.CharField(max_length=551)
    drupal_img1 = models.ImageField(upload_to='drupal_ico_img/')
    drupal_img_title1 = models.CharField(max_length=151)
    drupal_img2 = models.ImageField(upload_to='drupal_ico_img/')
    drupal_img_title2 = models.CharField(max_length=151)
    drupal_img3 = models.ImageField(upload_to='drupal_ico_img/')
    drupal_img_title3 = models.CharField(max_length=151)
    drupal_img4 = models.ImageField(upload_to='drupal_ico_img/')
    drupal_img_title4 = models.CharField(max_length=151)

class DevProcessDrupal(models.Model):
    dev_drupal_title = models.CharField(max_length=51)
    dev_drupal_img = models.ImageField(upload_to='drupal_img/')
    dev_drupal_desc = models.TextField()
    dev_drupal_img_screen = models.ImageField(upload_to='drupal_img/laptop_screen')

class AddValueDrupal(models.Model):
    add_value_drupal_title = models.CharField(max_length=51)
    add_value_drupal_img = models.ImageField(upload_to='drupal_img/add_value')
    add_value_drupal_desc = models.TextField()

class SolutionExpertiseDrupal(models.Model):
    sol_exper_drupal_title = models.CharField(max_length=51)
    sol_exper_drupal_img = models.ImageField(upload_to='drupal_img/solution_expertise')

class DevServiceDrupal(models.Model):
    dev_service_drupal_title = models.CharField(max_length=51)
    dev_servic_drupal_img = models.ImageField(upload_to='drupal_img/dev_service')

class DevServiceDescDrupal(models.Model):
    dev_service_drupal_desc = models.CharField(max_length=551)

class DrupalDevCompany(models.Model):
    drupal_dev_title = models.CharField(max_length=51)
    drupal_dev_desc = models.TextField()
    drupal_dev_img = models.ImageField(upload_to='drupal_img/django_dev_company')

#UI Desing Page Model
class UiTitle(models.Model):
    ui_title = models.CharField(max_length=251)

class OurDesignBerief(models.Model):
    our_design_title = models.CharField(max_length=251)
    our_design_desc = models.TextField()
    dev_servic_drupal_img = models.ImageField(upload_to='our_design_img')

class SpanTitle(models.Model):
    span_title1 = models.CharField(max_length=251)
    span_sol_desc = models.TextField()
    span_sol_img = models.ImageField(upload_to='our_design_img')

class SolutionDesign(models.Model):
    solution_heading = models.CharField(max_length=21)

class SolutionDesignTitle(models.Model):
    solution_span = models.CharField(max_length=151)

class SolutionDesignBrand(models.Model):
    sol_design_brand_img = models.ImageField(upload_to='our_design_img')
    sol_design_brand_title = models.CharField(max_length=151)
    sol_design_brand_heading = models.CharField(max_length=151)
    sol_design_brand_desc = models.TextField()

class solutionWebsite(models.Model):
    sol_web_title = models.CharField(max_length=151)
    sol_web_desc = models.TextField()
    sol_web_img = models.ImageField(upload_to='our_design_img')

class ApplicationDesign(models.Model):
    application_head = models.CharField(max_length=151)
    application_title = models.CharField(max_length=151)

class ApplicationDesignUi(models.Model):
    application_ui_head = models.CharField(max_length=151)
    application_ui_title = models.CharField(max_length=151)
    application_ui_desc = models.TextField()

class SocialMedia(models.Model):
    sm_title = models.CharField(max_length=151)
    sm_desc = models.TextField()
    sm_img = models.ImageField(upload_to='our_design_img')

class SocialMediaImg(models.Model):
    smg_img = models.ImageField(upload_to='our_design_img')

class TechnologyTool(models.Model):
    tool_title = models.CharField(max_length=151)

class TechnologyToolImg(models.Model):
    tool_img = models.ImageField(upload_to='our_design_img/tool_img')

#Who We Are Model start
class WhoWeAre(models.Model):
    title = models.CharField(max_length=101)
    heading = models.CharField(max_length=151)
    desc = models.TextField()
    about_img1 = models.ImageField(upload_to='who_we_are_img')
    about_img2 = models.ImageField(upload_to='who_we_are_img')
    about_img3 = models.ImageField(upload_to='who_we_are_img')
    about_img4 = models.ImageField(upload_to='who_we_are_img')
    about_img5 = models.ImageField(upload_to='who_we_are_img')


class WhoWeAreDesinProcess(models.Model):
    dev_process_img = models.ImageField(upload_to='who_we_are_img/dev_process_img')
    dev_process_title = models.CharField(max_length=101)
    dev_process_head = models.CharField(max_length=151)
    dev_process_desc = models.TextField()

class WhoWeAreWork(models.Model):
    work_title = models.CharField(max_length=101)
    work_head = models.CharField(max_length=151)

class WhoWeAreWorkAbt(models.Model):
    abt_work_img = models.ImageField(upload_to='who_we_are_img/work_img')
    abt_wrok_title = models.CharField(max_length=151)
    abt_work_desc = models.TextField()

class WhoWeAreAbtHaving(models.Model):
    abt_having_title = models.CharField(max_length=151)

class WhoWeAreAbtHavingDetails(models.Model):
    abt_having_details_img = models.ImageField(upload_to='who_we_are_img/abt_having_details_img')
    abt_having_details_head = models.CharField(max_length=151)
    abt_having_details_desc = models.TextField()

class WhoWeAreCompanyValue(models.Model):
    abt_company_value_img = models.ImageField(upload_to='who_we_are_img/abt_company_value_img')
    abt_company_value_title = models.CharField(max_length=151)
    abt_company_value_head = models.CharField(max_length=151)
    abt_company_value_desc = models.TextField()

class WhoWeAreCompanyValueImpPoint(models.Model):
    abt_com_value_imp_pt = models.CharField(max_length=151)

class WhoWeAreCultural(models.Model):
    cul_title = models.CharField(max_length=101)
    cul_head = models.TextField()

class WhoWeAreCulturalImg(models.Model):
    cul_img = models.ImageField(upload_to='who_we_are_img/cul_img')

#Government e Marketplace Model
class GemTitle(models.Model):
    gem_title = models.CharField(max_length=101)

class GemTitle1(models.Model):
    gem_title_heading = models.CharField(max_length=21)

class GemTitle2(models.Model):
    gem_title_span = models.CharField(max_length=151)

class GemTitleDesc(models.Model):
    gem_title_desc = models.TextField()
    gem_title_img = models.ImageField(upload_to='gem_title/gem_title_img')

class GeMBreif(models.Model):
    gem_brief_title = models.CharField(max_length=101)
    gem_brief_desc = models.TextField()
    gem_brief_title1 = models.CharField(max_length=101)
    gem_brief_desc1 = models.TextField()

class GemSellerRegister(models.Model):
    seller_head = models.CharField(max_length=51)
    gem_title_reg = models.CharField(max_length=51)
    gem_seller_desc = models.TextField()
    gem_seller_contact = models.CharField(max_length=251)
    gem_seller_contact_no = models.CharField(max_length=251)
    gem_seller_advantage = models.CharField(max_length=251)
    gem_seller_advantage_title = models.CharField(max_length=251)

class GemSellerAdvantage(models.Model):
    advantage_title = models.CharField(max_length=251)

class GemBuyerAdvantageDesc(models.Model):
    buyer_title = models.CharField(max_length=51)
    buyer_desc = models.CharField(max_length=251)

class GemBuyerAdvantage(models.Model):
    buyer_advantage_title = models.CharField(max_length=251)

# Digital Signare Certificate(DSC) Model
class DscTitle(models.Model):
    dsc_title = models.CharField(max_length=101)

class DscTitle1(models.Model):
    dsc_title_heading = models.CharField(max_length=21)

class DscTitle2(models.Model):
    dsc_title_span = models.CharField(max_length=151)

class DscTitleDesc(models.Model):
    dsc_title_desc = models.TextField()
    dsc_title_img = models.ImageField(upload_to='dsc_title/dsc_title_img')

class DscClass2(models.Model):
    dsc_class2_title = models.CharField(max_length=151)
    dsc_class2_head1 = models.CharField(max_length=151)
    dsc_class2_desc1 = models.TextField()
    dsc_class2_head2 = models.CharField(max_length=151)
    dsc_class2_desc2 = models.TextField()
    dsc_class2_use_title = models.CharField(max_length=151)
    dsc_class2_use_desc = models.TextField()

class DscClass2Use(models.Model):
    dsc_class2_use_title = models.CharField(max_length=251)

class DscClass3(models.Model):
    dsc_class3_title = models.CharField(max_length=151)
    dsc_class3_head1 = models.CharField(max_length=151)
    dsc_class3_desc1 = models.TextField()
    dsc_class3_head2 = models.CharField(max_length=151)
    dsc_class3_desc2 = models.TextField()
    dsc_class3_contact = models.CharField(max_length=251)
    dsc_class3_contact_no = models.CharField(max_length=251)
    dsc_class3_use_title = models.CharField(max_length=151)
    dsc_class3_use_desc = models.TextField()

class DscClass3Use(models.Model):
    dsc_class3_use_title = models.CharField(max_length=251)

# Bid Participation Model
class BiddingTitle(models.Model):
    bidding_title = models.CharField(max_length=101)

class BiddingTitle1(models.Model):
    bidding_title_heading = models.CharField(max_length=21)

class BiddingTitle2(models.Model):
    bidding_title_span = models.CharField(max_length=151)

class BiddingTitleDesc(models.Model):
    bidding_title_desc = models.TextField()
    bidding_title_img = models.ImageField(upload_to='bidding_title/bidding_title_img')

class BiddingParticipation(models.Model):
    bidding_part_title = models.CharField(max_length=151)
    bidding_part_desc = models.TextField()
    bidding_part_title1 = models.CharField(max_length=151)
    bidding_part_desc1 = models.TextField()

class BidParticiaptionHead(models.Model):
    bidding_part_head = models.CharField(max_length=151)

#Packages Model for GeM(Governemnt e Marketplace)
class GempackageHead(models.Model):
    gem_head = models.CharField(max_length=151)
    gem_title = models.CharField(max_length=351)

class GemPackage(models.Model):
    gem_package_title = models.CharField(max_length=25)
    gem_package_price = models.IntegerField()
    gem_package_title_list1 = models.CharField(max_length=55,blank=True)
    gem_package_title_list2 = models.CharField(max_length=55,blank=True)
    gem_package_title_list3 = models.CharField(max_length=55,blank=True)
    gem_package_title_list4 = models.CharField(max_length=55,blank=True)
    gem_package_title_list5 = models.CharField(max_length=55,blank=True)

#Packages Model for Tender Bidding
class TenderpackageHead(models.Model):
    tender_head = models.CharField(max_length=151)
    tender_title = models.CharField(max_length=351)

class TenderPackage(models.Model):
    tender_package_title = models.CharField(max_length=25)
    tender_package_price = models.IntegerField()
    tender_package_title_list1 = models.CharField(max_length=55,blank=True)
    tender_package_title_list2 = models.CharField(max_length=55,blank=True)
    tender_package_title_list3 = models.CharField(max_length=55,blank=True)
    tender_package_title_list4 = models.CharField(max_length=55,blank=True)
    tender_package_title_list5 = models.CharField(max_length=55,blank=True)

#Packages Model for Web Development
class WebpackageHead(models.Model):
    web_head = models.CharField(max_length=151)
    web_title = models.CharField(max_length=351)

class WebPackage(models.Model):
    web_package_title = models.CharField(max_length=25)
    web_package_price = models.IntegerField()
    web_package_title_list1 = models.CharField(max_length=55,blank=True)
    web_package_title_list2 = models.CharField(max_length=55,blank=True)
    web_package_title_list3 = models.CharField(max_length=55,blank=True)
    web_package_title_list4 = models.CharField(max_length=55,blank=True)
    web_package_title_list5 = models.CharField(max_length=55,blank=True)

class packageHeading(models.Model):
    pack_title = models.CharField(max_length=55)
    pack_desc = models.TextField()

#Our Work(Portfolio) Model
class OurWork(models.Model):
    project_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    language_used1 = models.CharField(max_length=30)
    language_used2 = models.CharField(max_length=30)
    language_used3 = models.CharField(max_length=30,blank=True)
    language_used4 = models.CharField(max_length=30,blank=True)
    language_used5 = models.CharField(max_length=30, blank=True)
    project_desc1 = models.TextField(blank=True)
    project_img1 = models.ImageField(upload_to='work_project_img/')
    project_img2 = models.ImageField(upload_to='work_project_img/')
    project_img3 = models.ImageField(upload_to='work_project_img/',blank=True)
    project_img4 = models.ImageField(upload_to='work_project_img/',blank=True)
    project_created_date = models.DateTimeField(auto_now_add=True)
    project_updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('portfolio_details',args=[self.slug])

#Contact Us page Model
class ContactUs(models.Model):
    contact_form_heading = models.CharField(max_length=151)
    contact_title = models.TextField()
    contact_form_img = models.ImageField(upload_to='contact_us_img/')
    contact_addres = models.CharField(max_length=501)
    contact_num = models.CharField(max_length=16)
    contact_email = models.EmailField()
    contact_map = models.CharField(max_length=5000)

#Contact Form page Model
class ContactUsForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=101)
    phone_num = models.CharField(max_length=15)
    desc = models.TextField()
    submission_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message from' + self.first_name

class FooterSocialFollow(models.Model):
    li_class = models.CharField(max_length=21)
    social_link = models.CharField(max_length=151)
    social_icon = models.CharField(max_length=21)
    social_title = models.CharField(max_length=31)

    def __str__(self):
        return self.social_icon




