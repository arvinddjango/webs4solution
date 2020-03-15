from django.contrib import admin
# from .models import Blog,IndexDevService,IndexServiceList,IndexAdress,IndexProject,ClientSpeaks,WhyCompany,CarrerPage,JobOpening,OurTeam,DevelopmentProcess,Support,FaqPhpDev,GetStartPhp,ProjectList,DevProcessPhp,AddValuePhp,SolutionExpertisePhp,DevServiceDescPhp,DevServicePhp,PhpDevCompany
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title','publish','blog_created_date','blog_updated_date',]
    prepopulated_fields = {'slug':('blog_title',)}

admin.site.register(Blog,BlogAdmin)

class IndexServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title','service_title_desc']

admin.site.register(IndexDevService,IndexServiceAdmin)

class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['service_name','service_url','service_created_date','service_updated_date']

admin.site.register(IndexServiceList,ServiceListAdmin)

class IndexAddressAdmin(admin.ModelAdmin):
    list_display = ['country_name','state_name','office_address','address_created_date','address_updated_date']

admin.site.register(IndexAdress,IndexAddressAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_head','project_name','project_created_date','project_updated_date',]
    prepopulated_fields = {'slug':('project_head',)}

admin.site.register(IndexProject,ProjectAdmin)

class ClientSpeakAdmin(admin.ModelAdmin):
    list_display = ['client_name','client_company_name','client_comment','client_created_date']

admin.site.register(ClientSpeaks,ClientSpeakAdmin)

class WhyCompanyAdmin(admin.ModelAdmin):
    list_display = ['why_title','why_created_date','why_updated_date']

admin.site.register(WhyCompany,WhyCompanyAdmin)

class CarrerAdmin(admin.ModelAdmin):
    list_display = ['career_title','carrer_created_date','carrer_updated_date']

admin.site.register(CarrerPage,CarrerAdmin)

class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ['technology_language','job_location','job_qulification','job_experience','job_created_date','job_updated_date']

admin.site.register(JobOpening,JobOpeningAdmin)

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['team_name','team_designation','team_created_date','team_updated_date']

admin.site.register(OurTeam,OurTeamAdmin)





class DevProcessAdmin(admin.ModelAdmin):
    list_display = ['dev_process','dev_created_date','dev_updated_date']

admin.site.register(DevelopmentProcess,DevProcessAdmin)

class SupportAdmin(admin.ModelAdmin):
    list_display = ['support_contact_title','support_created_date','support_updated_date']

admin.site.register(Support,SupportAdmin)

#PHP Devlopment Process

class FaqPhpDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqPhpDev,FaqPhpDevAdmin)

class GetStrtPhpAdmin(admin.ModelAdmin):
    list_display = ['php_title','php_desc']

admin.site.register(GetStartPhp,GetStrtPhpAdmin)

class ProjectListAdmin(admin.ModelAdmin):
    list_display = ['project_name',]

admin.site.register(ProjectList,ProjectListAdmin)

class DevProcessPhptAdmin(admin.ModelAdmin):
    list_display = ['dev_title',]

admin.site.register(DevProcessPhp,DevProcessPhptAdmin)

class AddValuePhptAdmin(admin.ModelAdmin):
    list_display = ['add_value_php_title',]

admin.site.register(AddValuePhp,AddValuePhptAdmin)

class SolExperPhptAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_php_title',]

admin.site.register(SolutionExpertisePhp,SolExperPhptAdmin)

class DevServicePhptAdmin(admin.ModelAdmin):
    list_display = ['dev_service_php_title',]

admin.site.register(DevServicePhp,DevServicePhptAdmin)

class DevServiceDescPhptAdmin(admin.ModelAdmin):
    list_display = ['dev_service_php_desc',]

admin.site.register(DevServiceDescPhp,DevServiceDescPhptAdmin)

class PhpDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['php_dev_title',]

admin.site.register(PhpDevCompany,PhpDevCompanyAdmin)

#Django Devlopment Process

class FaqDjangoDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqDjangoDev,FaqDjangoDevAdmin)

class GetStrtDjangoAdmin(admin.ModelAdmin):
    list_display = ['django_title','django_desc']

admin.site.register(GetStartDjango,GetStrtDjangoAdmin)

class DevProcessDjangoAdmin(admin.ModelAdmin):
    list_display = ['dev_django_title',]

admin.site.register(DevProcessDjango,DevProcessDjangoAdmin)

class AddValueDjangoAdmin(admin.ModelAdmin):
    list_display = ['add_value_django_title',]

admin.site.register(AddValueDjango,AddValueDjangoAdmin)

class SolExperDjangoAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_django_title',]

admin.site.register(SolutionExpertiseDjango,SolExperDjangoAdmin)

class DevServiceDjangoAdmin(admin.ModelAdmin):
    list_display = ['dev_service_django_title',]

admin.site.register(DevServiceDjango,DevServiceDjangoAdmin)

class DevServiceDescDjangoAdmin(admin.ModelAdmin):
    list_display = ['dev_service_django_desc',]

admin.site.register(DevServiceDescDjango,DevServiceDescDjangoAdmin)

class DjangoDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['django_dev_title',]

admin.site.register(DjangoDevCompany,DjangoDevCompanyAdmin)

#Python Web Devlopment Process

class FaqPythonDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqPythonDev,FaqPythonDevAdmin)

class GetStrtPythonAdmin(admin.ModelAdmin):
    list_display = ['python_title','python_desc']

admin.site.register(GetStartPython,GetStrtPythonAdmin)

class DevProcessPythonAdmin(admin.ModelAdmin):
    list_display = ['dev_python_title',]

admin.site.register(DevProcessPython,DevProcessPythonAdmin)

class AddValuePythonAdmin(admin.ModelAdmin):
    list_display = ['add_value_python_title',]

admin.site.register(AddValuePython,AddValuePythonAdmin)

class SolExperPythonAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_python_title',]

admin.site.register(SolutionExpertisePython,SolExperPythonAdmin)

class DevServicePythonoAdmin(admin.ModelAdmin):
    list_display = ['dev_service_python_title',]

admin.site.register(DevServicePython,DevServicePythonoAdmin)

class DevServiceDescPythonAdmin(admin.ModelAdmin):
    list_display = ['dev_service_python_desc',]

admin.site.register(DevServiceDescPython,DevServiceDescPythonAdmin)

class PythonDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['python_dev_title',]

admin.site.register(PythonDevCompany,PythonDevCompanyAdmin)


#Laravel Web Devlopment Process

class FaqLaravelDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqLaravelDev,FaqLaravelDevAdmin)

class GetStrtLaravelAdmin(admin.ModelAdmin):
    list_display = ['laravel_title','laravel_desc']

admin.site.register(GetStartLaravel,GetStrtLaravelAdmin)

class DevProcessLaravelAdmin(admin.ModelAdmin):
    list_display = ['dev_laravel_title',]

admin.site.register(DevProcessLaravel,DevProcessLaravelAdmin)

class AddValueLaravelAdmin(admin.ModelAdmin):
    list_display = ['add_value_laravel_title',]

admin.site.register(AddValueLaravel,AddValueLaravelAdmin)

class SolExperLaravelAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_laravel_title',]

admin.site.register(SolutionExpertiseLaravel,SolExperLaravelAdmin)

class DevServiceLaravelAdmin(admin.ModelAdmin):
    list_display = ['dev_service_laravel_title',]

admin.site.register(DevServiceLaravel,DevServiceLaravelAdmin)

class DevServiceDescLaravelAdmin(admin.ModelAdmin):
    list_display = ['dev_service_laravel_desc',]

admin.site.register(DevServiceDescLaravel,DevServiceDescLaravelAdmin)

class LaravelDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['laravel_dev_title',]

admin.site.register(LaravelDevCompany,LaravelDevCompanyAdmin)


#Wordpress Web Devlopment Process

class FaqWordpressDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqWordpressDev,FaqWordpressDevAdmin)

class GetStrtWordpressAdmin(admin.ModelAdmin):
    list_display = ['wordpress_title','wordpress_desc']

admin.site.register(GetStartWordpress,GetStrtWordpressAdmin)

class DevProcessWordpressAdmin(admin.ModelAdmin):
    list_display = ['dev_wordpress_title',]

admin.site.register(DevProcessWordpress,DevProcessWordpressAdmin)

class AddValueWordpressAdmin(admin.ModelAdmin):
    list_display = ['add_value_wordpress_title',]

admin.site.register(AddValueWordpress,AddValueWordpressAdmin)

class SolExperWordpressAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_wordpress_title',]

admin.site.register(SolutionExpertiseWordpress,SolExperWordpressAdmin)

class DevServiceWordpressAdmin(admin.ModelAdmin):
    list_display = ['dev_service_wordpress_title',]

admin.site.register(DevServiceWordpress,DevServiceWordpressAdmin)

class DevServiceDescWordpressAdmin(admin.ModelAdmin):
    list_display = ['dev_service_wordpress_desc',]

admin.site.register(DevServiceDescWordpress,DevServiceDescWordpressAdmin)

class WordpressDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['wordpress_dev_title',]

admin.site.register(WordpressDevCompany,WordpressDevCompanyAdmin)


#IOS APP Web Devlopment Process

class FaqIosDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqIosAPPDev,FaqIosDevAdmin)

class GetStrtIosAdmin(admin.ModelAdmin):
    list_display = ['iosapp_title','iosapp_desc']

admin.site.register(GetStartIosAPP,GetStrtIosAdmin)

class DevProcessIosAdmin(admin.ModelAdmin):
    list_display = ['dev_iosapp_title',]

admin.site.register(DevProcessIosAPP,DevProcessIosAdmin)

class AddValueIosAdmin(admin.ModelAdmin):
    list_display = ['add_value_iosapp_title',]

admin.site.register(AddValueIosAPP,AddValueIosAdmin)

class SolExperIosAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_iosapp_title',]

admin.site.register(SolutionExpertiseIosAPP,SolExperIosAdmin)

class DevServiceIosAdmin(admin.ModelAdmin):
    list_display = ['dev_service_iosapp_title',]

admin.site.register(DevServiceIosAPP,DevServiceIosAdmin)

class DevServiceDescIosAdmin(admin.ModelAdmin):
    list_display = ['dev_service_iosapp_desc',]

admin.site.register(DevServiceDescIosAPP,DevServiceDescIosAdmin)

class IosDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['iosapp_dev_title',]

admin.site.register(IosAPPDevCompany,IosDevCompanyAdmin)



#Andriod APP Web Devlopment Process

class FaqAndriodDevAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqAndroidAPPDev,FaqAndriodDevAdmin)

class GetStrtAndriodAdmin(admin.ModelAdmin):
    list_display = ['android_title','android_desc']

admin.site.register(GetStartAndroidAPP,GetStrtAndriodAdmin)

class DevProcessAndriodAdmin(admin.ModelAdmin):
    list_display = ['dev_android_title',]

admin.site.register(DevProcessAndroidAPP,DevProcessAndriodAdmin)

class AddValueAndriodAdmin(admin.ModelAdmin):
    list_display = ['add_value_android_title',]

admin.site.register(AddValueAndroidAPP,AddValueAndriodAdmin)

class SolExperAndriodAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_android_title',]

admin.site.register(SolutionExpertiseAndroidAPP,SolExperAndriodAdmin)

class DevServiceAndriodAdmin(admin.ModelAdmin):
    list_display = ['dev_service_android_title',]

admin.site.register(DevServiceAndroidAPP,DevServiceAndriodAdmin)

class DevServiceDescAndriodAdmin(admin.ModelAdmin):
    list_display = ['dev_service_android_desc',]

admin.site.register(DevServiceDescAndroidAPP,DevServiceDescAndriodAdmin)

class AndriodDevCompanyAdmin(admin.ModelAdmin):
    list_display = ['android_dev_title',]

admin.site.register(AndroidAPPDevCompany,AndriodDevCompanyAdmin)

#Magento APP Web Devlopment Process

class FaqMagentoAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqMagentoDev,FaqMagentoAdmin)

class GetStrtMagentoAdmin(admin.ModelAdmin):
    list_display = ['magento_title','magento_desc']

admin.site.register(GetStartMagento,GetStrtMagentoAdmin)

class DevProcessMagentoAdmin(admin.ModelAdmin):
    list_display = ['dev_magento_title',]

admin.site.register(DevProcessMagento,DevProcessMagentoAdmin)

class AddValueMagentoAdmin(admin.ModelAdmin):
    list_display = ['add_value_magento_title',]

admin.site.register(AddValueMagento,AddValueMagentoAdmin)

class SolExperMagentoAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_magento_title',]

admin.site.register(SolutionExpertiseMagento,SolExperMagentoAdmin)

class DevServiceMagentoAdmin(admin.ModelAdmin):
    list_display = ['dev_service_magento_title',]

admin.site.register(DevServiceMagento,DevServiceMagentoAdmin)

class DevServiceDescMagentoAdmin(admin.ModelAdmin):
    list_display = ['dev_service_magento_desc',]

admin.site.register(DevServiceDescMagento,DevServiceDescMagentoAdmin)

class MagentoCompanyAdmin(admin.ModelAdmin):
    list_display = ['magento_dev_title',]

admin.site.register(MagentoDevCompany,MagentoCompanyAdmin)

#Drupal APP Web Devlopment Process

# class FaqDrupalDAdmin(admin.ModelAdmin):
#     list_display = ['question1',]
#
# admin.site.register(FaqDrupalDev,FaqDrupalDAdmin)

class FaqDrupalDAdmin(admin.ModelAdmin):
    list_display = ['question1',]

admin.site.register(FaqDrupalDev,FaqDrupalDAdmin)

class GetStrtDrupalAdmin(admin.ModelAdmin):
    list_display = ['drupal_title','drupal_desc']

admin.site.register(GetStartDrupal,GetStrtDrupalAdmin)

class DevProcessDrupalAdmin(admin.ModelAdmin):
    list_display = ['dev_drupal_title',]

admin.site.register(DevProcessDrupal,DevProcessDrupalAdmin)

class AddValueDrupalAdmin(admin.ModelAdmin):
    list_display = ['add_value_drupal_title',]

admin.site.register(AddValueDrupal,AddValueDrupalAdmin)

class SolExperDrupalAdmin(admin.ModelAdmin):
    list_display = ['sol_exper_drupal_title',]

admin.site.register(SolutionExpertiseDrupal,SolExperDrupalAdmin)

class DevServiceDrupalAdmin(admin.ModelAdmin):
    list_display = ['dev_service_drupal_title',]

admin.site.register(DevServiceDrupal,DevServiceDrupalAdmin)

class DevServiceDescDrupalAdmin(admin.ModelAdmin):
    list_display = ['dev_service_drupal_desc',]

admin.site.register(DevServiceDescDrupal,DevServiceDescDrupalAdmin)

class DrupalCompanyAdmin(admin.ModelAdmin):
    list_display = ['drupal_dev_title',]

admin.site.register(DrupalDevCompany,DrupalCompanyAdmin)

#UI Design Model
admin.site.register(UiTitle)
admin.site.register(OurDesignBerief)
admin.site.register(SpanTitle)
admin.site.register(SolutionDesign)
admin.site.register(SolutionDesignTitle)
admin.site.register(SolutionDesignBrand)
admin.site.register(solutionWebsite)
admin.site.register(ApplicationDesign)
admin.site.register(ApplicationDesignUi)
admin.site.register(SocialMedia)
admin.site.register(SocialMediaImg)
admin.site.register(TechnologyTool)
admin.site.register(TechnologyToolImg)

#WhoWeAre Model
admin.site.register(WhoWeAre)
admin.site.register(WhoWeAreDesinProcess)
admin.site.register(WhoWeAreWork)
admin.site.register(WhoWeAreWorkAbt)
admin.site.register(WhoWeAreAbtHaving)
admin.site.register(WhoWeAreAbtHavingDetails)
admin.site.register(WhoWeAreCompanyValue)
admin.site.register(WhoWeAreCompanyValueImpPoint)
admin.site.register(WhoWeAreCultural)
admin.site.register(WhoWeAreCulturalImg)

#Governmet e Marketplace Model
admin.site.register(GemTitle)
admin.site.register(GemTitle1)
admin.site.register(GemTitle2)
admin.site.register(GemTitleDesc)
admin.site.register(GeMBreif)
admin.site.register(GemSellerRegister)
admin.site.register(GemSellerAdvantage)
admin.site.register(GemBuyerAdvantageDesc)
admin.site.register(GemBuyerAdvantage)

#DSC Model
admin.site.register(DscTitle)
admin.site.register(DscTitle1)
admin.site.register(DscTitle2)
admin.site.register(DscTitleDesc)
admin.site.register(DscClass2)
admin.site.register(DscClass2Use)
admin.site.register(DscClass3)
admin.site.register(DscClass3Use)

#Bidding Model
admin.site.register(BiddingTitle)
admin.site.register(BiddingTitle1)
admin.site.register(BiddingTitle2)
admin.site.register(BiddingTitleDesc)
admin.site.register(BiddingParticipation)
admin.site.register(BidParticiaptionHead)

#Package Model
admin.site.register(GempackageHead)
admin.site.register(GemPackage)
admin.site.register(TenderPackage)
admin.site.register(TenderpackageHead)
admin.site.register(WebpackageHead)
admin.site.register(WebPackage)
admin.site.register(packageHeading)

#Our Work Model
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ['project_name','project_created_date','project_updated_date',]
    prepopulated_fields = {'slug':('project_name',)}

admin.site.register(OurWork,OurWorkAdmin)

#contact Us Model
admin.site.register(ContactUs)

#COntact FOrm Model
admin.site.register(ContactUsForm)

admin.site.register(FooterSocialFollow)

admin.site.register(FaqIosDev1)