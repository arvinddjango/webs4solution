from django.shortcuts import render,redirect,HttpResponse
from django .http import HttpResponse
from .models import *
from django.contrib import messages # for message
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    gem_seller = GemSellerRegister.objects.all()
    bidparticipate = BiddingParticipation.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/')
        #End footer form submission
    development_service = IndexDevService.objects.all()
    service_list = IndexServiceList.objects.all()
    blog_list = Blog.objects.all().order_by('-id')
    address_list = IndexAdress.objects.all()
    project_list = IndexProject.objects.all()
    client_list = ClientSpeaks.objects.all()
    why_company_list = WhyCompany.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    return render(request,'webs4solution/index.html',{'development_service':development_service,'service_list':service_list,'blog_list':blog_list,'address_list':address_list,'project_list':project_list,'client_list':client_list,'why_company_list':why_company_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list,'gem_seller':gem_seller,'bidparticipate':bidparticipate})

def who_we_are(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    whowe_are = WhoWeAre.objects.all()
    whowe_are_desn_process = WhoWeAreDesinProcess.objects.all()
    whowe_are_work = WhoWeAreWork.objects.all()
    whowe_are_work_abt = WhoWeAreWorkAbt.objects.all()
    whowe_are_abt_having = WhoWeAreAbtHaving.objects.all()
    whowe_are_abt_having_dtls = WhoWeAreAbtHavingDetails.objects.all()
    whowe_are_com_value = WhoWeAreCompanyValue.objects.all()
    whowe_are_com_value_imp_pt = WhoWeAreCompanyValueImpPoint.objects.all()
    whowe_are_cul = WhoWeAreCultural.objects.all()
    whowe_are_cul_img = WhoWeAreCulturalImg.objects.all()
    return render(request,'webs4solution/who-we-are.html',{'whowe_are':whowe_are,'whowe_are_desn_process':whowe_are_desn_process,'whowe_are_work':whowe_are_work,'whowe_are_work_abt':whowe_are_work_abt,'whowe_are_abt_having':whowe_are_abt_having,'whowe_are_abt_having_dtls':whowe_are_abt_having_dtls,'whowe_are_com_value':whowe_are_com_value,'whowe_are_com_value_imp_pt':whowe_are_com_value_imp_pt,'whowe_are_cul':whowe_are_cul,'whowe_are_cul_img':whowe_are_cul_img,'contact_detail':contact_detail,'social_fb__list':social_fb__list})


def projects_details(request,slug):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    projects_list_detail = IndexProject.objects.get(slug=slug)
    return render(request,'webs4solution/taxi-on-click.html',{'projects_list_detail':projects_list_detail,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def blog(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    blog_list = Blog.objects.all().order_by('-id')
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    return render(request,'webs4solution/blog.html',{'blog_list':blog_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def blog_details(request,slug):
    blog_list = Blog.objects.all().order_by('-id')[:3]
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list_detail = Blog.objects.get(slug=slug)
    return render(request,'webs4solution/blog-details.html',{'blog_list_detail':blog_list_detail,'contact_detail':contact_detail,'social_fb__list':social_fb__list,'blog_list':blog_list})

def career(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    career_list = CarrerPage.objects.all()
    job_list = JobOpening.objects.all()
    return render(request,'webs4solution/career.html',{'career_list':career_list,'job_list':job_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def team(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    team_list = OurTeam.objects.all()
    return render(request,'webs4solution/team.html',{'team_list':team_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def development_process(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    dev_process_list = DevelopmentProcess.objects.order_by('id')
    return render(request,'webs4solution/development-process.html',{'dev_process_list':dev_process_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def support(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    support_list = Support.objects.all()
    return render(request,'webs4solution/support.html',{'support_list':support_list,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def portfolio(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    our_work = OurWork.objects.all()
    return render(request,'webs4solution/portfolio.html',{'our_work':our_work,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def portfolio_details(request,slug):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    portfolio_list_detail = OurWork.objects.get(slug=slug)
    return render(request,'webs4solution/portfolio-project-detail.html',{'portfolio_list_detail':portfolio_list_detail,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def contact_us(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #for message display
    #messages.success(request, 'We received your message, Our experts will contact you soon!')
    contact_detail = ContactUs.objects.all()
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/contactus')
    return render(request,'webs4solution/contactus.html',{'contact_detail':contact_detail,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

# def contact_us_base(request):
#     #for message display
#     #messages.success(request, 'We received your message, Our experts will contact you soon!')
#     contact_detail = ContactUs.objects.all()
#     if request.method=='POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         service_name = request.POST['service_name']
#         email_id = request.POST['email_id']
#         phone_num = request.POST['phone_num']
#         desc = request.POST['desc']
#         #print(first_name,last_name,service_name,email_id,phone_num,desc)
#         if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
#             messages.error(request,'please fill the form correctly')
#         else:
#             contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
#             contact_us.save()
#             messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
#             return redirect('/contactus')
#     return render(request,'includes/footer.html',{'contact_detail':contact_detail})

def php_development(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    faq_list = FaqPhpDev.objects.all()
    start_php = GetStartPhp.objects.all()
    project_list = IndexProject.objects.all()
    #project_list = ProjectList.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    sol_expertise = SolutionExpertisePhp.objects.all()
    php_service = DevServicePhp.objects.all()
    php_service_desc = DevServiceDescPhp.objects.all()
    php_dev_company = PhpDevCompany.objects.all()
    return render(request,'webs4solution/php-development.html',{'blog_list':blog_list,'faq_list':faq_list,'start_php':start_php,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'sol_expertise':sol_expertise,'php_service':php_service,'php_service_desc':php_service_desc,'php_dev_company':php_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Django Devlopment Service start

def django_development(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    django_faq_list = FaqDjangoDev.objects.all()
    django_php = GetStartDjango.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    #project_list = ProjectList.objects.all()
    # django_dev_process = DevProcessDjango.objects.all()
    # add_value_django = AddValueDjango.objects.all()
    django_sol_expertise = SolutionExpertiseDjango.objects.all()
    django_service = DevServiceDjango.objects.all()
    djago_service_desc = DevServiceDescDjango.objects.all()
    django_dev_company = DjangoDevCompany.objects.all()
    return render(request,'webs4solution/django-web-development-services.html',{'blog_list':blog_list,'django_faq_list':django_faq_list,'django_php':django_php,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'django_sol_expertise':django_sol_expertise,'django_service':django_service,'djago_service_desc':djago_service_desc,'django_dev_company':django_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Python Web Devlopment Service start

def python_development(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    python_faq_list = FaqPythonDev.objects.all()
    start_python = GetStartPython.objects.all()
    # project_list = ProjectList.objects.all()
    # python_dev_process = DevProcessPython.objects.all()
    # add_value_python = AddValuePython.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    python_sol_expertise = SolutionExpertisePython.objects.all()
    python_service = DevServicePython.objects.all()
    python_service_desc = DevServiceDescPython.objects.all()
    python_dev_company = PythonDevCompany.objects.all()
    return render(request,'webs4solution/python-web-development.html',{'blog_list':blog_list,'python_faq_list':python_faq_list,'start_python':start_python,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'python_sol_expertise':python_sol_expertise,'python_service':python_service,'python_service_desc':python_service_desc,'python_dev_company':python_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Laravel Web Devlopment Service start

def laravel_development(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    laravel_faq_list = FaqLaravelDev.objects.all()
    start_laravel = GetStartLaravel.objects.all()
    # project_list = ProjectList.objects.all()
    # laravel_dev_process = DevProcessLaravel.objects.all()
    # add_value_laravel = AddValueLaravel.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    laravel_sol_expertise = SolutionExpertiseLaravel.objects.all()
    laravel_service = DevServiceLaravel.objects.all()
    laravel_service_desc = DevServiceDescLaravel.objects.all()
    laravel_dev_company = LaravelDevCompany.objects.all()
    return render(request,'webs4solution/laravel-development.html',{'blog_list':blog_list,'laravel_faq_list':laravel_faq_list,'start_laravel':start_laravel,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'laravel_sol_expertise':laravel_sol_expertise,'laravel_service':laravel_service,'laravel_service_desc':laravel_service_desc,'laravel_dev_company':laravel_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Wordpress Web Devlopment Service start

def wordpress_development(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    wordpress_faq_list = FaqWordpressDev.objects.all()
    start_wordpress = GetStartWordpress.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    # project_list = ProjectList.objects.all()
    # wordpress_dev_process = DevProcessWordpress.objects.all()
    # add_value_wordpress = AddValueWordpress.objects.all()
    wordpress_sol_expertise = SolutionExpertiseWordpress.objects.all()
    wordpress_service = DevServiceWordpress.objects.all()
    wordpress_service_desc = DevServiceDescWordpress.objects.all()
    wordpress_dev_company = WordpressDevCompany.objects.all()
    return render(request,'webs4solution/wordpress-development.html',{'blog_list':blog_list,'wordpress_faq_list':wordpress_faq_list,'start_wordpress':start_wordpress,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'wordpress_sol_expertise':wordpress_sol_expertise,'wordpress_service':wordpress_service,'wordpress_service_desc':wordpress_service_desc,'wordpress_dev_company':wordpress_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#IOS App Development start

def ios_app(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    ios_faq_list = FaqIosAPPDev.objects.all()
    start_php = GetStartPhp.objects.all()
    #project_list = ProjectList.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    #ios_dev_process = DevProcessIosAPP.objects.all()
    #add_value_ios = AddValueIosAPP.objects.all()
    ios_sol_expertise = SolutionExpertiseIosAPP.objects.all()
    ios_service = DevServiceIosAPP.objects.all()
    ios_service_desc = DevServiceDescIosAPP.objects.all()
    ios_dev_company = IosAPPDevCompany.objects.all()
    return render(request,'webs4solution/ios-app-development-services.html',{'blog_list':blog_list,'ios_faq_list':ios_faq_list,'start_php':start_php,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'ios_sol_expertise':ios_sol_expertise,'ios_service':ios_service,'ios_service_desc':ios_service_desc,'ios_dev_company':ios_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Android App Development start
def android_app(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    android_faq_list = FaqAndroidAPPDev.objects.all()
    start_android = GetStartAndroidAPP.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    # android_dev_process = DevProcessAndroidAPP.objects.all()
    # add_value_android = AddValueAndroidAPP.objects.all()
    android_sol_expertise = SolutionExpertiseAndroidAPP.objects.all()
    android_service = DevServiceAndroidAPP.objects.all()
    android_service_desc = DevServiceDescAndroidAPP.objects.all()
    android_dev_company = AndroidAPPDevCompany.objects.all()
    return render(request,'webs4solution/android-app-development.html',{'blog_list':blog_list,'android_faq_list':android_faq_list,'start_android':start_android,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'android_sol_expertise':android_sol_expertise,'android_service':android_service,'android_service_desc':android_service_desc,'android_dev_company':android_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Drupal App Development start
def drupal_app(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    drupal_faq_list = FaqDrupalDev.objects.all()
    start_drupal = GetStartDrupal.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    # project_list = ProjectList.objects.all()
    # drupal_dev_process = DevProcessMagento.objects.all()
    # add_value_drupal = AddValueDrupal.objects.all()
    drupal_sol_expertise = SolutionExpertiseDrupal.objects.all()
    drupal_service = DevProcessDrupal.objects.all()
    drupal_service_desc = DevServiceDescDrupal.objects.all()
    drupal_dev_company = DrupalDevCompany.objects.all()
    return render(request,'webs4solution/drupal-development.html',{'blog_list':blog_list,'drupal_faq_list':drupal_faq_list,'start_drupal':start_drupal,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'drupal_sol_expertise':drupal_sol_expertise,'drupal_service':drupal_service,'drupal_service_desc':drupal_service_desc,'drupal_dev_company':drupal_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

#Magento App Development start
def magento_app(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    blog_list = Blog.objects.all().order_by('-id')
    magento_faq_list = FaqMagentoDev.objects.all()
    start_magento = GetStartMagento.objects.all()
    project_list = IndexProject.objects.all()
    php_dev_process = DevProcessPhp.objects.all()
    add_value_php = AddValuePhp.objects.all()
    # project_list = ProjectList.objects.all()
    # magento_dev_process = DevProcessMagento.objects.all()
    # add_value_magento = AddValueMagento.objects.all()
    magento_sol_expertise = SolutionExpertiseMagento.objects.all()
    magento_service = DevProcessMagento.objects.all()
    magento_service_desc = DevServiceDescMagento.objects.all()
    magento_dev_company = MagentoDevCompany.objects.all()
    return render(request,'webs4solution/magento-development.html',{'blog_list':blog_list,'magento_faq_list':magento_faq_list,'start_magento':start_magento,'project_list':project_list,'php_dev_process':php_dev_process,'add_value_php':add_value_php,'magento_sol_expertise':magento_sol_expertise,'magento_service':magento_service,'magento_service_desc':magento_service_desc,'magento_dev_company':magento_dev_company,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def poit_checklist(request):
    return render(request,'webs4solution/7-point-checklist-to-choose-your-technology-partner.html')

def ui_ux_design(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    uititle = UiTitle.objects.all()
    our_design_brief = OurDesignBerief.objects.all()
    spantitle = SpanTitle.objects.all()
    soldesign = SolutionDesign.objects.all()
    soldesigntitle = SolutionDesignTitle.objects.all()
    soldesignbrnd = SolutionDesignBrand.objects.all()
    solweb = solutionWebsite.objects.all()
    appdesign = ApplicationDesign.objects.all()
    appdesignui = ApplicationDesignUi.objects.all()
    socialmedia = SocialMedia.objects.all()
    smimg = SocialMediaImg.objects.all()
    techtool = TechnologyTool.objects.all()
    techtoolimg = TechnologyToolImg.objects.all()
    return render(request,'webs4solution/ui-ux-design.html',{'uititle':uititle,'our_design_brief':our_design_brief,'spantitle':spantitle,'soldesign':soldesign,'soldesigntitle':soldesigntitle,'soldesignbrnd':soldesignbrnd,'solweb':solweb,'appdesign':appdesign,'appdesignui':appdesignui,'socialmedia':socialmedia,'smimg':smimg,'techtool':techtool,'techtoolimg':techtoolimg,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def web_development_services(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    return render(request,'webs4solution/web-development-services.html',{'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def government_e_marketplace(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    gemtitle = GemTitle.objects.all()
    gemtitle1 = GemTitle1.objects.all()
    gemtitle2 = GemTitle2.objects.all()
    gemtitledesc = GemTitleDesc.objects.all()
    gem_breif = GeMBreif.objects.all()
    gem_seller = GemSellerRegister.objects.all()
    gem_seller_advantage = GemSellerAdvantage.objects.all()
    gem_buyer = GemBuyerAdvantage.objects.all()
    gem_buyer_adv = GemBuyerAdvantageDesc.objects.all()
    return render(request,'webs4solution/government-e-marketplace.html',{'gemtitle':gemtitle,'gemtitle1':gemtitle1,'gemtitle2':gemtitle2,'gemtitledesc':gemtitledesc,'gem_breif':gem_breif,'gem_seller':gem_seller,'gem_seller_advantage':gem_seller_advantage,'gem_buyer':gem_buyer,'gem_buyer_adv':gem_buyer_adv,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def digital_signature_certificate(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    dsctitle = DscTitle.objects.all()
    dsctitle1 = DscTitle1.objects.all()
    dsctitle2 = DscTitle2.objects.all()
    dsctitledesc = DscTitleDesc.objects.all()
    dsc_class2 = DscClass2.objects.all()
    dsc_class2_use = DscClass2Use.objects.all()
    dsc_class3 = DscClass3.objects.all()
    dsc_class3_use = DscClass3Use.objects.all()
    return render(request,'webs4solution/digital-signature-certificate.html',{'dsctitle':dsctitle,'dsctitle1':dsctitle1,'dsctitle2':dsctitle2,'dsctitledesc':dsctitledesc,'dsc_class2':dsc_class2,'dsc_class2_use':dsc_class2_use,'dsc_class3':dsc_class3,'dsc_class3_use':dsc_class3_use,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def bid_particiaption(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    bidtitle = BiddingTitle.objects.all()
    bidtitle1 = BiddingTitle1.objects.all()
    bidtitle2 = BiddingTitle2.objects.all()
    bidtitledesc = BiddingTitleDesc.objects.all()
    bidparticipate = BiddingParticipation.objects.all()
    bidpartipatehead = BidParticiaptionHead.objects.all()
    return render(request,'webs4solution/bid-particiaption.html',{'bidtitle':bidtitle,'bidtitle1':bidtitle1,'bidtitle2':bidtitle2,'bidtitledesc':bidtitledesc,'bidparticipate':bidparticipate,'bidpartipatehead':bidpartipatehead,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def packages(request):
    contact_detail = ContactUs.objects.all()
    social_fb__list = FooterSocialFollow.objects.all()
    #Footer form submission
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        service_name = request.POST['service_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        desc = request.POST['desc']
        #print(first_name,last_name,service_name,email_id,phone_num,desc)
        if len(first_name)<2 or len(last_name)<2 or len(email_id)<3 or len(phone_num)<10 or len(desc)<4:
            messages.error(request,'please fill the form correctly')
        else:
            contact_us = ContactUsForm(first_name=first_name,last_name=last_name,service_name=service_name,email_id=email_id,phone_num=phone_num,desc=desc)
            contact_us.save()
            messages.success(request, 'Thank You, We received your message, Our experts will contact you soon!')
            return redirect('/blog')
        #End footer form submission
    package_heading = packageHeading.objects.all()
    gem_package_head = GempackageHead.objects.all()
    gem_package = GemPackage.objects.all()
    tender_package = TenderPackage.objects.all()
    tender_package_head = TenderpackageHead.objects.all()
    web_package = WebPackage.objects.all()
    web_package_head = WebpackageHead.objects.all()

    return  render(request,'webs4solution/packages.html',{'package_heading':package_heading,'gem_package_head':gem_package_head,'gem_package':gem_package,'tender_package':tender_package,'tender_package_head':tender_package_head,'web_package':web_package,'web_package_head':web_package_head,'contact_detail':contact_detail,'social_fb__list':social_fb__list})

def handlesignup(request):
    if request.method=='POST':
        username =request.POST['username']
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        # check for errornous input or validation
        if len(username) > 10:
            messages.error(request,'Username must be under 10 character')
            return redirect('/blog')
        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and number')
            return redirect('/blog')
        if pass1 != pass2:
            messages.error(request, 'Password donot match ')
            return redirect('/blog')


        # create user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your accound has been created')
        return redirect('/blog')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        loginusername =request.POST['loginusername']
        loginpass =request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/blog')
        else:
            messages.error(request,'Invalid credential, Pz try again')
            return redirect('/blog')

    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/blog')


# for counter even odd template code

# {% for entry in blog.entries %}
#   <div class="{% if forloop.counter|divisibleby:2 %}even{% else %}odd{% endif %}" id="{{ entry.id }}">
#     {{ entry.text }}
#   </div>
# {% endfor %}